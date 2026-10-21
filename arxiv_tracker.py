"""arXiv 每周追踪：QKD / 集成光子芯片 / 相干光通信

每周运行一次，按 TOPICS 里的检索式分主题抓取 arXiv 新论文，
用大模型翻译摘要、提炼创新点，生成一份 Markdown 周报。

本地试跑（不调用大模型）：  python arxiv_tracker.py --dry-run
"""
import argparse
import glob
import os
import re
import time
from datetime import datetime, timedelta, timezone

import arxiv

# ================= 配置区 =================
# 读取你在 GitHub Secrets 里存的 API KEY
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = "https://api.deepseek.com/v1"
MODEL_NAME = "deepseek-chat"

# 抓取窗口（天）。arXiv 从提交到 API 可见有 1–3 天延迟，
# 只取 7 天会漏掉周末提交的论文；这里放宽到 10 天，再用历史周报去重。
DAYS_BACK = 10

# 周报文件名前缀；去重时会扫描 REPORT_DIR 里所有 .md 文件
REPORT_PREFIX = "arXiv_Weekly"

# 周报存放目录
REPORT_DIR = "reports"

# 每个主题一条 arXiv 检索式。一篇论文同时命中多个主题时，只放在排在前面的主题里。
# 检索式语法见 https://info.arxiv.org/help/api/user-manual.html#query_details
TOPICS = [
    {
        "key": "qkd",
        "name": "量子密钥分发 (QKD)",
        "query": 'all:"quantum key distribution" OR all:QKD',
        "max_results": 150,
        "relevance": False,
    },
    {
        "key": "chip",
        "name": "集成光子芯片",
        "query": (
            '(abs:"silicon photonic" OR abs:"silicon photonics" OR abs:"photonic integrated circuit" '
            'OR abs:"integrated photonic" OR abs:"integrated photonics" OR abs:"thin-film lithium niobate" '
            'OR abs:"silicon nitride" OR abs:"heterogeneous integration") '
            'AND (abs:receiver OR abs:transceiver OR abs:transmitter OR abs:modulator OR abs:photodetector '
            'OR abs:photodiode OR abs:homodyne OR abs:heterodyne OR abs:coherent OR abs:quantum '
            'OR abs:"optical hybrid" OR abs:"polarization")'
        ),
        "max_results": 200,
        "relevance": True,
    },
    {
        "key": "coherent",
        "name": "相干光通信",
        "query": (
            '(abs:"coherent optical" OR abs:"coherent receiver" OR abs:"coherent detection" '
            'OR abs:"coherent transmission" OR abs:"coherent transceiver" OR abs:intradyne '
            'OR abs:"self-coherent" OR abs:"carrier phase recovery" OR abs:"carrier recovery" '
            'OR abs:"probabilistic shaping" OR abs:"probabilistically shaped" OR abs:"digital backpropagation" '
            'OR abs:"single-sideband" OR abs:"Kramers-Kronig") '
            'AND (cat:physics.optics OR cat:eess.SP OR cat:cs.IT OR cat:cs.NI OR cat:physics.app-ph)'
        ),
        "max_results": 150,
        "relevance": True,
    },
]

# QKD 主题内部再按关键词把连续变量 (CV) 论文单独列在前面
CV_PATTERN = re.compile(
    r"continuous[- ]variable|CV-?QKD|CVQKD|homodyne|heterodyne|local oscillator|coherent[- ]state",
    re.I,
)
# ==========================================


def base_id(entry_id):
    """'http://arxiv.org/abs/2610.13090v2' -> '2610.13090'"""
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", entry_id)
    return m.group(1) if m else entry_id


def load_seen_ids(folder=".", exclude=None):
    """从已有周报中收集出现过的 arXiv 编号，用于跨周去重。"""
    seen = set()
    for path in glob.glob(os.path.join(folder, "*.md")):
        if exclude and os.path.abspath(path) == os.path.abspath(exclude):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                seen.update(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", f.read()))
        except OSError:
            pass
    return seen


def fetch_topic(client, topic, start_date):
    search = arxiv.Search(
        query=topic["query"],
        max_results=topic["max_results"],
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    results = list(client.results(search))
    papers = [p for p in results if p.published > start_date]
    if results and len(results) == topic["max_results"] and results[-1].published > start_date:
        print(f"⚠️ 主题「{topic['name']}」结果可能被截断，请调大 max_results")
    return papers


def build_prompt(abstract_text, with_relevance):
    relevance = ""
    if with_relevance:
        relevance = """
    3. 用一句话说明这篇工作对"连续变量量子密钥分发（CV-QKD）或硅光相干接收机"有什么可借鉴之处；没有直接关联就写"无直接关联"。"""
    relevance_fmt = """

    **【对CV-QKD的启发】**：
    [一句话]""" if with_relevance else ""
    return f"""
    你是一个专业的光通信、集成光子学和量子密码学学术助手。处理这篇英文摘要：
    1. 翻译成流畅的中文（保持学术术语准确，如QKD、Decoy-state、PIC、DSP等）。
    2. 用一句话（加粗）高度概括核心创新点或结论。{relevance}

    原文：{abstract_text}

    严格按此格式输出：
    **【中文摘要】**：
    [翻译内容]

    **【核心创新点】**：
    [一句话总结]{relevance_fmt}
    """


def translate_and_summarize(client_llm, abstract_text, with_relevance):
    if client_llm is None:
        return f"**【英文原文】** (未调用大模型): {abstract_text}"
    try:
        response = client_llm.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": build_prompt(abstract_text, with_relevance)}],
            temperature=0.3,
            timeout=60,
        )
        return response.choices[0].message.content
    except Exception:
        return f"**【英文原文】** (AI分析失败): {abstract_text}"


def write_paper(f, idx, paper, analysis):
    authors = ", ".join(a.name for a in paper.authors)
    f.write(f"### {idx}. {paper.title}\n\n")
    f.write(f"- **👨‍🔬 作者:** {authors}\n")
    f.write(f"- **📅 时间:** {paper.published.strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n")
    f.write(f"- **🏷️ 分类:** {', '.join(paper.categories)}\n")
    f.write(f"- **🔗 链接:** [arXiv 页面]({paper.entry_id}) | [PDF直达]({paper.pdf_url})\n\n")
    f.write(f"{analysis}\n\n---\n\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="不调用大模型，只输出英文摘要")
    parser.add_argument("--days", type=int, default=DAYS_BACK)
    args = parser.parse_args()

    client_llm = None
    if not args.dry_run:
        from openai import OpenAI
        client_llm = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    start_date = datetime.now(timezone.utc) - timedelta(days=args.days)
    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=5)
    os.makedirs(REPORT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(REPORT_DIR, f"{REPORT_PREFIX}_{date_str}.md")
    # 去重时排除今天这份周报本身，同一天重复运行会重新生成而不是变成空报告
    seen = load_seen_ids(REPORT_DIR, exclude=filename)

    # 分主题抓取；同一篇论文只归入第一个命中的主题，并跳过以往周报已收录的论文
    grouped = {}
    for topic in TOPICS:
        kept = []
        for p in fetch_topic(client, topic, start_date):
            pid = base_id(p.entry_id)
            if pid in seen:
                continue
            seen.add(pid)
            kept.append(p)
        grouped[topic["key"]] = kept

    # QKD 主题内：CV 论文排在前面
    qkd = grouped.get("qkd", [])
    cv = [p for p in qkd if CV_PATTERN.search(p.title + " " + p.summary)]
    other = [p for p in qkd if p not in cv]

    total = sum(len(v) for v in grouped.values())

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 🔐 arXiv 每周追踪：QKD / 集成光子芯片 / 相干光通信\n\n")
        counts = f"QKD {len(qkd)}（其中 CV-QKD {len(cv)}）· 芯片 {len(grouped.get('chip', []))} · 相干光通信 {len(grouped.get('coherent', []))}"
        f.write(f"> **生成日期:** {date_str} | **本周新增:** {total} 篇（{counts}）\n\n---\n\n")
        if total == 0:
            f.write("本周 arXiv 上没有找到新的相关论文。\n")

        sections = [
            ("🌀 连续变量 QKD (CV-QKD)", cv, False),
            ("🔑 其他 QKD", other, False),
        ]
        for topic in TOPICS[1:]:
            icon = "🧩" if topic["key"] == "chip" else "📡"
            sections.append((f"{icon} {topic['name']}", grouped[topic["key"]], topic["relevance"]))

        idx = 0
        for title, papers, with_relevance in sections:
            if not papers:
                continue
            f.write(f"## {title}（{len(papers)} 篇）\n\n")
            for paper in papers:
                idx += 1
                analysis = translate_and_summarize(
                    client_llm, paper.summary.replace("\n", " "), with_relevance
                )
                write_paper(f, idx, paper, analysis)
                if client_llm is not None:
                    time.sleep(1)  # 防封禁延迟

    print(f"✅ 成功！已生成文件：{filename}（共 {total} 篇）")


if __name__ == "__main__":
    main()

# arXiv 每周追踪：QKD / 集成光子芯片 / 相干光通信

每周一自动检索 arXiv 新论文，用大模型（默认 DeepSeek）翻译摘要、提炼创新点，生成一份 Markdown 周报，存到 `reports/` 目录。

周报分四个板块：

| 板块 | 内容 |
|---|---|
| 🌀 连续变量 QKD | QKD 论文中与 CV 相关的部分，单独排在最前面 |
| 🔑 其他 QKD | 其余 QKD 论文 |
| 🧩 集成光子芯片 | 硅光、PIC、薄膜铌酸锂、氮化硅等平台上的接收机、调制器、探测器、相干和量子器件 |
| 📡 相干光通信 | 相干接收、载波恢复、概率整形、单边带、Kramers-Kronig 等 |

芯片和相干光通信两个板块，每篇会额外给出一句"对 CV-QKD 的启发"。

## 部署步骤

1. **新建仓库**：在 GitHub 上新建一个仓库（公开或私有都可以），把本项目的全部文件上传上去，注意要包括 `.github/workflows/run.yml`。
   - 网页上传时，`.github` 是隐藏文件夹，可能被漏掉。更稳妥的做法是用命令行：
     ```bash
     cd arxiv-weekly-tracker
     git init
     git add .
     git commit -m "init"
     git branch -M main
     git remote add origin https://github.com/<你的用户名>/<仓库名>.git
     git push -u origin main
     ```
2. **添加大模型密钥**：仓库 → Settings → Secrets and variables → Actions → New repository secret，名称填 `LLM_API_KEY`，值填你的 DeepSeek API Key。
3. **打开写权限**：仓库 → Settings → Actions → General → Workflow permissions，选择 "Read and write permissions" 并保存。不打开的话，Actions 生成周报后提交不回仓库。
4. **手动试跑一次**：仓库 → Actions → 左侧选 "arXiv Weekly Report" → Run workflow。几分钟后 `reports/` 下会出现第一份周报。之后每周一自动运行。

## 调整

所有配置都在 `arxiv_tracker.py` 顶部的配置区：

- `TOPICS`：每个主题的 arXiv 检索式和 `max_results`。结果太多太杂就收紧关键词；运行日志出现"可能被截断"的提示时，调大该主题的 `max_results`。检索式语法见 [arXiv API 文档](https://info.arxiv.org/help/api/user-manual.html#query_details)。
- `DAYS_BACK`：抓取窗口，默认 10 天。arXiv 从提交到可检索有 1–3 天延迟，窗口留得比一周宽一些，再按 arXiv 编号和历史周报去重，就不会漏掉也不会重复。
- `BASE_URL` / `MODEL_NAME`：换成其他兼容 OpenAI 接口的大模型时修改这两项。
- 运行时间在 `.github/workflows/run.yml` 的 `cron` 里修改（UTC 时间）。

## 本地运行

```bash
pip install -r requirements.txt
python arxiv_tracker.py --dry-run          # 不调用大模型，只输出英文摘要，用于检查检索结果
LLM_API_KEY=你的密钥 python arxiv_tracker.py  # 完整运行
python arxiv_tracker.py --days 30 --dry-run # 临时放宽窗口，比如补抓过去一个月
```

## 说明

- 同一篇论文同时命中多个主题时，只放在排在前面的主题里（QKD 优先，其次芯片，再次相干光通信）。
- 已在以往周报中出现过的论文会自动跳过。
- 芯片和相干光通信两块每周可能有几十篇，大模型调用量会相应增加。
- 如果仓库连续 60 天没有任何提交，GitHub 会自动停用定时任务。本项目每周都会提交周报，正常情况下不会触发。

# 🔐 arXiv 每周追踪：QKD / 集成光子芯片 / 相干光通信

> **生成日期:** 2026-10-29 | **本周新增:** 8 篇（QKD 4（其中 CV-QKD 1）· 芯片 3 · 相干光通信 1）

---

## 🌀 连续变量 QKD (CV-QKD)（1 篇）

### 1. Multimode continuous-variable quantum key distribution with CMOS-compatible photonic-electronic integration

- **👨‍🔬 作者:** Yiming Bian, Sarah Bastiaens, Saeed Hakimi, Huy Quang Nguyen, Aboobackkar Sidhique, Cédric Bruynsteen, Govind J. Wanjalkar, Ali Al Hadi Amhaz, Jasper Jans, Axl Bomhals, Ulrik L. Andersen, Tobias Gehring, Xin Yin, Adnan A. E. Hajomer
- **📅 时间:** 2026-10-26 13:22:32 (UTC)
- **🏷️ 分类:** quant-ph
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.35410v1) | [PDF直达](https://arxiv.org/pdf/2610.35410v1)

**【中文摘要】**：
多路复用与光子-电子集成通过并行传输和适合规模化制造的紧凑型硬件，为实现可扩展、高吞吐量的量子密钥分发（QKD）网络提供了一条路径。实现这一路径需要多通道发射机和接收机，以及考虑模式耦合的安全性分析。本文提出了一种CMOS兼容的光子-电子多模连续变量QKD架构，并以偏振复用作为双模示例。硅光子发射机和接收机芯片并行制备和探测两个偏振模式。接收机与双通道28 nm CMOS跨阻放大器共集成，在两个通道中均提供超过20 dB的散粒噪声裕度。导频辅助的酉数字恢复消除了对主动光学偏振控制的需求，而多模安全性分析则考虑了模式串扰。在2%残余串扰下，多模分析将仿真安全距离从39 km扩展至84 km，接近89 km的无串扰极限。在10 km已部署光纤上，平均总有限码长密钥率估计为6.69 Mbit/s，比来自同一数字恢复数据的单模分析高12%。这些结果确立了一条通往可扩展多模量子安全网络的路径，该网络建立在适合大规模生产的技术之上。

**【核心创新点】**：
本文提出并实验验证了一种CMOS兼容的硅光子-电子多模连续变量QKD架构，通过偏振复用双模并行收发、导频辅助数字偏振恢复及考虑模式串扰的多模安全性分析，在2%残余串扰下将安全距离从39 km扩展至84 km，并在10 km部署光纤上实现6.69 Mbit/s的有限码长密钥率。

---

## 🔑 其他 QKD（3 篇）

### 2. Security Analysis of Ekert-type QKD Protocol Coming Under Cloning Attacks

- **👨‍🔬 作者:** Kaushiki Mukherjee, Sumana Karmakar
- **📅 时间:** 2026-10-27 14:43:11 (UTC)
- **🏷️ 分类:** quant-ph
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.37337v1) | [PDF直达](https://arxiv.org/pdf/2610.37337v1)

**【中文摘要】**：
我们分析了一种Ekert型双方密钥分发协议在不可信观察者实施克隆攻击下的安全性。具体而言，假设窃听者拦截由认证源通过公共信道传输给可信方的量子比特，并对其中一个或两个量子比特施加非对称的、相位变化的克隆操作。我们从设计QKD协议的角度对双量子比特态进行了部分表征，使得该协议即使在此类克隆攻击下仍能在可信用户之间生成可蒸馏的密钥。我们依据Devetak-Winter框架计算密钥率，以识别在协议中使用时可蒸馏出密钥的态。纠缠态在设计成功QKD协议中的效用从单量子比特克隆攻击到双量子比特克隆攻击会发生变化。有趣的是，当传输的量子比特中仅有一个被恶意第三方克隆时，我们能够区分出若干有用的双量子比特纠缠态族。

**【核心创新点】**：
本文在Devetak-Winter框架下分析了Ekert型QKD协议在非对称相位变化克隆攻击下的安全性，揭示了纠缠态效用随单/双量子比特克隆攻击的转变规律，并识别出仅单量子比特被克隆时仍可蒸馏密钥的有用纠缠态族。

---

### 3. Prepare-and-measure quantum key distribution from a bound on information leakage

- **👨‍🔬 作者:** Abhishek Mishra, Michele Masini, Maria Balanzó-Juandó, Armin Tavakoli, Stefano Pironio
- **📅 时间:** 2026-10-27 14:16:59 (UTC)
- **🏷️ 分类:** quant-ph
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.37296v1) | [PDF直达](https://arxiv.org/pdf/2610.37296v1)

**【中文摘要】**：
每一个量子密钥分发（QKD）协议都必须限制用户实验室之外可获得的信息。在设备无关QKD中，这实质上是对设备所做的唯一假设。在制备-测量场景中，这一要求无法被严格施加，因为发送方的设备必须发出依赖于其私有输入信号。自然而然的替代方案——也是最小化的方案——是泄漏界：即关于输入信息通过预期信号或任何侧信道从发送方实验室泄漏出去的信息量的上界。我们追问这一不可避免的要求能在多大程度上替代对源的详细模型。我们证明，以从源所发射的一切信息中猜测输入的概率来量化的这一单一界限，足以证明对集体攻击的安全性。在我们的分析中，除了接收方测量设备不泄漏Bob数据的标准要求外，对发射态的具体形式、维度、能量或纯度以及接收方的测量设备均不作任何假设。标准的B92和BB84协议在这一最小泄漏界假设下无法认证任何密钥。但密切相关的协议可以做到，并且在理想极限下，每轮密钥可实现一个秘密比特。对于有噪声的实现，我们使用半定规划松弛来计算密钥率。我们最好的协议可容忍低至0.84的可见度，对应8%的量子比特错误率，而标准设备相关BB84的阈值为11%。

**【核心创新点】**：
提出以“猜测概率”量化的最小泄漏界替代源设备的详细模型，证明其足以保证对集体攻击的安全性，并据此设计出在理想极限下每轮产生一个秘密比特、且可容忍8%量子比特错误率的实用QKD协议。

---

### 4. Deployed entanglement-based BBM92 quantum key distribution using frequency-converted photons emitted by a quantum dot

- **👨‍🔬 作者:** Michal Vyvlecka, Raphael Joos, Benjamin Breiholz, Emma Marmasse, Ilenia Neureuther, Timo Schnieber, Anna Frederike Köhler, Tim Strobel, Andreas Berg, Sebastian Kiesel, Tobias Bauer, Marlon Schäfer, Nand Lal Sharma, Caspar Hopfmann, Simone Luca Portalupi, Christoph Becher, Peter Michler
- **📅 时间:** 2026-10-27 14:01:58 (UTC)
- **🏷️ 分类:** quant-ph
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.37268v1) | [PDF直达](https://arxiv.org/pdf/2610.37268v1)

**【中文摘要】**：
建立安全通信是现有和未来网络的一项重要需求。尽管当前的解决方案依赖于经典方法，但量子力学提供了从计算安全性向信息论安全性转变的可能性。量子密钥分发（QKD）作为实现此类安全性的手段已被广泛研究。近年来，外延量子点开始被研究和应用于量子密码学，因为其快速发展使其成为迄今为止最亮的量子光源之一。特别地，它们被认为是偏振纠缠光子对的优异光源，尤其是在约780 nm波长下工作的液滴刻蚀量子点。本文中，我们采用这样一种量子点，在1 GHz激发速率下产生纠缠光子对。利用量子频率转换，我们将发射的光子与电信波长范围进行接口，同时保持其偏振纠缠特性。这使得我们能够在斯图加特大学Vaihingen校区一条1.59 km的实地部署光纤链路上，使用BBM92协议实现量子密钥分发：我们在19小时的稳定运行中实现了206 Hz的安全密钥率，总安全密钥长度达14.2 Mbit。该密钥结合进一步的纠错和隐私放大，能够实现对彩色图像的安全加密和解密。这些结果展示了将高激发速率运行的高质量纠缠光子源、高效频率转换模块以及皮秒级时间同步相结合并应用于实际部署网络中的重要进展，朝着混合量子网络迈出了重要步伐。

**【核心创新点】**：
**本文利用约780 nm液滴刻蚀量子点在高激发速率下产生偏振纠缠光子对，经量子频率转换至电信波段后在1.59 km实地光纤链路上实现BBM92协议QKD，19小时内生成14.2 Mbit安全密钥并完成图像加解密，展示了混合量子网络的关键技术集成。**

---

## 🧩 集成光子芯片（3 篇）

### 5. Rubidium-Referenced Frequency-Doubled Pockels Laser with High-Speed Electro-Optic Tuning

- **👨‍🔬 作者:** Xu Chen, Michael Li, Xiaodong Shi, Lin Zhou, Ran Yang, Mengyao Zhao, Veerendra Dhyani, Sakthi Sanjeev Mohanraj, Guangxing Wu, Hao Hao, Xia Yu, Di Zhu
- **📅 时间:** 2026-10-27 14:07:57 (UTC)
- **🏷️ 分类:** physics.optics
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.37279v1) | [PDF直达](https://arxiv.org/pdf/2610.37279v1)

**【中文摘要】**：
具有快速频率控制能力的窄线宽激光器对原子物理和量子技术至关重要，然而在可见光波段将上述能力集成于芯片光源中仍具挑战性。本文报道了一种混合集成的InP/薄膜铌酸锂普克尔斯激光器，通过腔内二次谐波产生在780 nm处发射激光，并支持吉赫兹带宽的频率调谐。激光腔中嵌入周期性极化铌酸锂波导，腔的一端为扩展分布式布拉格反射镜，仅在1560 nm基频波长处提供电光可调谐反馈。该设计形成单共振腔，既增强了频率转换效率，又使二次谐波输出能够跟随快速调谐而无需共振对准。该激光器在1560 nm和780 nm处的本征线宽分别为2.7 kHz和9.0 kHz，两个波长处的电光调谐带宽均超过1 GHz。在780 nm处实现6.48 GHz的无跳模调谐范围，可直接对铷D2跃迁进行光谱测量。将二次谐波输出锁定至该跃迁后，其频率波动的标准差从135 MHz降至8 MHz，并将原子频率参考传递至基频。这些结果确立了集成倍频普克尔斯激光器作为紧凑、快速可调谐光源的地位，有望简化未来原子与量子光子系统的光学架构。

**【核心创新点】**：
**本文首次在芯片上实现了混合集成InP/薄膜铌酸锂倍频普克尔斯激光器，通过单共振腔设计在780 nm处同时获得千赫兹级本征线宽与超过1 GHz的电光调谐带宽，并演示了无跳模调谐及原子跃迁锁定。**

**【对CV-QKD的启发】**：
该工作中窄线宽、快速电光调谐的集成激光器方案及单共振腔设计思路，可为CV-QKD系统中本振光与信号光的低噪声快速频率控制及光子集成化收发架构提供借鉴。

---

### 6. Optically gated transduction enables silicon electrical readout of mid-infrared light

- **👨‍🔬 作者:** Shutao Zhang, Jiaqing Shen, Chongwu Wang, Jiahui Xu, Wei Chen, Qing Yang Steve Wu, Yan Liu, Xie Yuen Gok, Febiana Tjiptoharsono, Xiaogang Liu, Qi Jie Wang, Joel K. W. Yang, Jinfeng Zhu, Zhaogang Dong
- **📅 时间:** 2026-10-27 01:33:02 (UTC)
- **🏷️ 分类:** physics.optics
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.36475v1) | [PDF直达](https://arxiv.org/pdf/2610.36475v1)

**【中文摘要】**：
硅是集成光子学的主导平台，但其1.1 eV的宽电子带隙从根本上阻碍了通过直接价带到导带激发实现对中红外（MIR）光子的高效探测。因此，现有方法致力于增强亚带隙吸收或引入外部红外吸收体。本文展示了一种截然不同的探测策略——基于光门控转导，其中MIR光子调制预先建立的激发态而非直接产生光生载流子。该器件将Nd³⁺掺杂镧系纳米颗粒与支持双共振的逆向设计Al/p-Si超表面集成，同时增强近红外光门控并共振耦合入射MIR辐射。MIR光照重新分布Nd³⁺的发射路径，产生光学态变化，并通过硅肖特基结转换为电信号。该器件在6.8 μm波长处实现室温零偏压探测，调制响应度为103 μA/W，并将门控与MIR组合输入解析为三个电学可区分的电流态。本工作并非将硅的吸收扩展至红外，而是确立了门控光转导作为在硅平台上读取MIR光学信息的途径，为集成红外传感、信号处理和可编程光子系统开辟了机遇。

**【核心创新点】**：
提出“光门控转导”探测策略，利用MIR光子调制Nd³⁺预激发态而非直接激发硅的带间跃迁，结合逆向设计Al/p-Si双共振超表面，在硅平台上实现室温零偏压6.8 μm中红外探测。

**【对CV-QKD的启发】**：
该工作中硅基零偏压肖特基结探测与双共振超表面增强光耦合的设计思路，可为硅光相干接收机在极低暗电流条件下的信号读出与片上光场增强提供借鉴。

---

### 7. Electro-optic comb-driven massive data transmission on monolithically integrated lithium niobate photonic circuits

- **👨‍🔬 作者:** Yikun Chen, Chuang Xu, Ke Zhang, Xiong Wu, Kangping Zhong, Xiangzhi Xie, Hanke Feng, Yifan Wu, Chao Lu, Alan Pak Tao Lau, Cheng Wang
- **📅 时间:** 2026-10-26 04:12:06 (UTC)
- **🏷️ 分类:** physics.optics
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.34821v1) | [PDF直达](https://arxiv.org/pdf/2610.34821v1)

**【中文摘要】**：
在大型AI模型的驱动下，数据中心互连的需求正超越传统的缩放定律。这要求数据中心环境向密集复用技术转型，例如波分复用（WDM），将长距频谱效率迁移至短距高带宽应用。集成光学频率梳为未来数据中心WDM互连提供了紧凑、低成本的光源。然而，现有的克尔光梳和锁模激光器实现方案在功率效率、光谱平坦度和相位噪声方面存在不足。其固定的、器件特定的信道间隔往往与标准WDM网格冲突，且与高速调制器的共集成仍具挑战性。本文通过在薄膜铌酸锂（TFLN）平台上演示使用平顶电光频率梳的高容量数据传输，克服了上述限制。该平台具有平坦光谱、可调波长和梳齿间距，并天然兼容（解）复用器和高速调制器。我们利用来自两个激光器的46个波长信道和一个50 GHz片上电光频率梳，在香港两所大学和两个数据中心之间一条98.84 km的已部署光纤链路上实现了16.56 Tb/s的相干传输，验证了其用于数据中心间连接的适用性。为突出网格可重构性，我们通过片上解复用器将频率梳重构为100 GHz间距，并演示了10信道、80 GBaud的相干传输，速率达6.4 Tb/s。我们进一步报道了一个概念验证的单片WDM发射机，集成了频率梳和高速调制器，实现了19信道、45 GBaud的IM/DD传输，速率达1.71 Tb/s。我们的工作验证了TFLN电光频率梳作为灵活、紧凑且可扩展的WDM引擎，可同时服务于相干和IM/DD数据中心链路，以满足快速增长的带宽需求。

**【核心创新点】**：
**本文在薄膜铌酸锂平台上实现了平顶电光频率梳，具备平坦光谱、可调波长与梳齿间距、以及与复用器/高速调制器的原生兼容性，并在香港真实部署光纤链路上完成了16.56 Tb/s相干传输及单片WDM发射机的概念验证。**

**【对CV-QKD的启发】**：
TFLN电光频率梳的平坦光谱、可调梳齿间距及与高速调制器的单片集成能力，可为CV-QKD系统提供多信道并行、网格可重构的紧凑光源方案，并借鉴其相干传输验证方法评估量子信号与经典信道共纤传输的兼容性。

---

## 📡 相干光通信（1 篇）

### 8. Ultrafast light-electron modulation for free-electron quantum optics: fundamentals and applications

- **👨‍🔬 作者:** Zirui Zhao, Ruoyu Chen, Changying Li, Yongcheng Ding, Zhaopin Chen, Xinbing Song, Shuaishuai Sun, Ye Tian, Kangpeng Wang, Yiming Pan
- **📅 时间:** 2026-10-26 19:17:04 (UTC)
- **🏷️ 分类:** physics.optics, quant-ph
- **🔗 链接:** [arXiv 页面](http://arxiv.org/abs/2610.36182v1) | [PDF直达](https://arxiv.org/pdf/2610.36182v1)

**【中文摘要】**：
自由电子波包的光学相干调制为实现超快光束偏转、能量交换、时间压缩和量子态整形提供了一条途径。光子诱导近场电子显微镜（PINEM）、超快Kapitza-Dirac效应（KDE）和介质激光加速（DLA）的最新进展已展示了强光-电子耦合，但纵向能量调制、横向动量转移和波包依赖衍射通常仍用各自独立的模型来描述。在此，我们建立了一个统一的光-电子调制（LEM）框架，将光学近场视为自由电子波包的可编程相位调制器。在该框架内，我们识别出纵向和横向调制通道，分别类似于光的电光相位调制和声光衍射，并展示了它们的运行如何依赖于波包范围、反冲、相位匹配和光场几何构型。这一表述将PINEM、Raman-Nath和Bragg衍射、类DLA加速以及反常PINEM组织为共同调制图像的极限区域。由此产生的框架为自由电子调制器提供了设计原则，能够控制能谱、时间密度、横向波前和电子-光子量子界面，从而确立LEM作为可编程飞秒至阿秒物质波控制的器件级平台。

**【核心创新点】**：
**提出了统一的光-电子调制（LEM）框架，将光学近场视为自由电子波包的可编程相位调制器，并把PINEM、Raman-Nath/Bragg衍射、类DLA加速和反常PINEM统一为同一调制图像的不同极限区域。**

**【对CV-QKD的启发】**：
无直接关联。

---


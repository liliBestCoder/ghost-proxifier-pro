# Ghost Proxifier Pro (幽灵代理器 专业版)

**Ghost Proxifier Pro** 是一款专为解决「进程不走系统代理」与「多 VPN 路由冲突」而打造的 Windows 高性能进程级代理引擎。

它彻底抛弃了笨重的 TUN/TAP 虚拟网卡方案，通过直接拦截应用层的网络请求，实现真正的 **透明代理** 与 **零路由侵入**。

---

## 🚀 核心定位：什么是 Ghost Proxifier？

如果您曾遇到以下困扰，Ghost Proxifier Pro 是您的终极解决方案：
- **进程级细粒度控制**：特定应用（如 Chrome、Telegram、Antigravity）不走系统代理？直接定向劫持， 强制它走系统代理。
- **VPN 完美共存**：正在使用公司私有 VPN，但又需要同时开启科学上网？Ghost Proxifier 实现零全局路由表侵入，让两者和谐共存。
- **无感透明转发**：基于 **MinHook** 深度拦截 Winsock API，配合独创的 **Lazy Handshake (延迟握手)** 机制，完美兼容现代异步 IO 程序，流量透明转发至 HTTP 代理。

---

## 💎 Pro 版 专属特性 (Premium Features)

相较于开源版本，Pro 版在性能与体验上进行了全面重构：

### 🧠 智能探测与“全家桶”接管 (Smart Injection & Tracking)
这是 Pro 版最人性化的功能改进，让您告别复杂的父子进程配置。
- **“全家桶”自动识别**：只需选中一个主要目标（如游戏启动器或浏览器），Pro 版会自动识别并追踪由该程序启动的**所有关联子进程**，实现真正的“一键点击，全量接管”。
- **即启即用，零干预**：毫秒级完成新应用的接入。只要代理开关开启，Pro 引擎便在后台静默完成注入，真正做到“即装即用”。
- **高级兼容性支持 (ConnectEx)**：针对现代 Windows 应用（如 Xshell、UWP 应用等）的特殊网络连接模式进行全方位优化，网络穿透力与稳定性提升 200%。
- **状态稳定性看门狗**：内置 Watchdog 实时检测代理状态。当发生网络波动导致 Hook 状态异常时，系统会自动尝试重连并修复，确保代理链不轻易断开。

![Process Management](process.png)

### 🎨 现代化酷炫 UI
采用了全新的 **玻璃拟态 (Glassmorphism)** 设计规范，支持动态暗黑模式：
- **可视化流量看板**：实时动画展示各进程的网络拓扑与流量峰值。
- **平滑微交互**：每一次状态切换都伴随精致的过场动画。

![Traffic Flow Visual](flow.png)

### 🛡️ 高级安全与分流
- **内置 DNS 防污染**：集成 Local DNS 修复与 **DoH (DNS over HTTPS) 阻断**机制。
- **精准流量画像**：确保上游 GeoIP/GeoSite 智能分流逻辑绝对精准，杜绝流量“侧漏”。

![Safe DNS & DoH](safe_dns.png)

---

## 📥 下载与安装

您可以在本仓库直接获取预编译的安装包：

👉 **[下载 Ghost Proxifier Pro Installer (MSI)](https://github.com/liliBestCoder/ghost-proxifier-pro/raw/master/GhostProxifier-Pro-Installer.msi)**

### 安装步骤
1. 下载 `.msi` 安装包。
2. 双击运行，根据安装向导完成部署。
3. 软件会自动检测系统环境并完成最优配置初始化。

![Upstream Settings](upstream.png)

---

## 🛠 技术深度

- **Hook 引擎**：基于成熟的 MinHook 框架。
- **IO 兼容性**：Lazy Handshake 技术确保在高并发、异步场景下的零延迟表现。
- **架构设计**：采用 C++17 编写，追求极致的执行效率与极地的内存占用。

---

## 🛡 FAQ & 反馈

**Q: Pro 版是否收费？**
A: **是的，Pro 版为付费授权软件。** 具体的授权费用标准请参考软件内部的激活说明，或直接联系开发者进行咨询。

![License Management](license.png)

**Q: 如何反馈 Bug？**
A: 请在 [Issues](https://github.com/liliBestCoder/ghost-proxifier-pro/issues) 页面提交您的问题，Pro 版用户将获得优先级支持。

---

**✈️ 官方社群**
- **Telegram 频道**: [Ghost Proxifier](https://t.me/ghostproxifier)
- **Telegram 群组**: [Ghost Proxifier](https://t.me/+SCVIJJFocWAxN2Y9)

---

Developed with ❤️ by the **GhostTeam**.

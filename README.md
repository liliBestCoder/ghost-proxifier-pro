# Ghost Proxifier Pro

🌐 **[www.ghostproxifier.com](https://www.ghostproxifier.com)**

**进程级透明代理引擎 — 不装虚拟网卡，不改路由表，DLL 注入到目标进程内部，在 Winsock 层面接管所有网络流量，代理节点对应用完全不可见。**

和 TUN/TAP 方案不同，Ghost Proxifier 不碰系统网络配置。VPN、内网、代理可以同时在线，互不干扰。拖入一个窗口，Chrome 的 Network Service、GPU 进程、Utility 进程自动全部覆盖。毫秒级注入，极低内存占用。

---

## 已支持应用

Chrome &nbsp;·&nbsp; MS Edge &nbsp;·&nbsp; Claude Code &nbsp;·&nbsp; Codex &nbsp;·&nbsp; FinalShell &nbsp;·&nbsp; Xshell &nbsp;·&nbsp; Antigravity &nbsp;·&nbsp; MySQL Workbench &nbsp;·&nbsp; CMD &nbsp;·&nbsp; PowerShell

> 理论上支持所有使用 Winsock 的 Windows 应用。以上为测试验证过的应用列表，更多应用持续验证中。

---

## 解决了什么问题？

三个最常见的痛点：

- **应用不走系统代理。** Chrome 还算听话，但 Telegram、Antigravity、各种游戏启动器——它们根本不理 Windows 的代理设置。Ghost Proxifier 直接进入进程内部，在 Winsock 层面接管网络请求，强制走你指定的代理。

- **VPN 和代理不能同时开。** 公司 VPN 连着内网，Clash 想翻墙——路由表打架，总有一个断。Ghost Proxifier 只代理你选中的进程，其它流量纹丝不动。VPN 和代理和平共处。

- **子进程裸奔。** 你拖入了启动器，它 spawn 出十个子窗口——那些子窗口的流量直接走真实 IP，代理形同虚设。Pro 版自动追踪进程树，一次拖入，整个进程家族全部接管。

---

## 怎么做到的？

不装 TUN/TAP 虚拟网卡——那会被风控系统检测。不走 WFP 内核驱动——那需要 EV 证书签名。我们的路径是 **用户态 API Hook**：

```
目标进程发起网络请求
    │
    ▼
connect("google.com:443")
    │
    └── [MinHook 拦截] → 重定向到代理 → HTTP CONNECT 隧道 → 落地节点
```

基于 MinHook 深度拦截 Winsock API（`connect`、`send`、`WSASend` 等 25+ 个函数），配合 **Lazy Handshake（延迟握手）** 机制——`connect()` 阶段非阻塞返回，首次 `send()` 才完成代理握手。Chrome 的非阻塞 IO 完全无感知，不会触发卡死检测。

C++17 编写，极低内存占用，毫秒级注入完成。

---

## Pro 版专属

### 进程树自动追踪

拖入一个主进程，引擎自动识别并注入它创建的所有子进程。Chrome 的 Network Service、GPU Process、Utility Process——全部自动覆盖，不需要手动配置 PID。

内置 Watchdog 实时检测 Hook 状态，网络波动导致代理断开时自动重连。

<img src="process.png" width="680" alt="Process Management" />

### 流量可视化

玻璃拟态 UI + 暗黑模式。实时流量图表、进程级网络拓扑、状态指示灯（绿/黄/红）。每 2 秒刷新，流畅不抖动。

<img src="flow.png" width="680" alt="Traffic Flow" />

### DNS 防污染 + DoH 阻断

内置 Local DNS，DNS 查询走加密隧道，杜绝 ISP 投毒。同时阻断 Chrome 等浏览器的 DoH 直连，强制所有 DNS 走本地代理，确保上游的 GeoIP/GeoSite 分流规则拿到的是真实 IP。

<img src="safe_dns.png" width="680" alt="Safe DNS" />

---

## 下载

👉 **[Ghost Proxifier Pro Installer (MSI)](https://github.com/liliBestCoder/ghost-proxifier-pro/releases)**

双击安装，自动配置。桌面快捷方式、开始菜单、控制面板卸载——该有的都有。支持静默安装（`msiexec /i /qn`），B 端批量部署无压力。

<img src="upstream.png" width="680" alt="Upstream Settings" />

---

## FAQ

**Pro 版收费吗？**

是的，Pro 版为付费授权软件。具体费用见软件内激活说明，或直接联系开发者。

**如何反馈问题？**

[提交 Issue](https://github.com/liliBestCoder/ghost-proxifier-pro/issues)，Pro 版用户优先响应。

---

**社群**

- Telegram 频道: [@ghostproxifier](https://t.me/ghostproxifier)
- Telegram 群组: [Ghost Proxifier](https://t.me/+SCVIJJFocWAxN2Y9)

---

Developed by **GhostTeam**.

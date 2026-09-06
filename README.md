<!-- LOGO & CONTACT -->
<p align="right">
  <a href="https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info" target="_blank">QQ群</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/ghostproxifier" target="_blank">TG频道</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/+SCVIJJFocWAxN2Y9" target="_blank">TG群组</a>
</p>

<p align="center"><img src="app_icon.ico" alt="Logo" width="64"></p>

<h1 align="center">Ghost Proxifier Pro</h1>

<p align="center">
  <a href="README-EN.md">🇬🇧 English</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/liliBestCoder/ghost-proxifier-pro/releases" target="_blank">下载</a>
  &nbsp;·&nbsp;
  <a href="https://ghostproxifier.com" target="_blank">官网</a>
</p>

<p align="center">
  <a href="#核心特性">核心特性</a>
  &nbsp;·&nbsp;
  <a href="#已支持应用">支持应用</a>
  &nbsp;·&nbsp;
  <a href="#快速使用">快速使用</a>
  &nbsp;·&nbsp;
  <a href="#架构概览">架构</a>
  &nbsp;·&nbsp;
  <a href="#适用场景">适用场景</a>
  &nbsp;·&nbsp;
  <a href="#与同类工具对比">工具对比</a>
  &nbsp;·&nbsp;
  <a href="#运行截图">截图</a>
  &nbsp;·&nbsp;
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  Windows 进程级透明代理工具：通过 DLL 注入和 Winsock API Hook，让指定应用及其子进程的网络流量自动转发到 HTTP / SOCKS5 代理，无需修改路由表或安装虚拟网卡。
</p>

<p align="center">
  🔧 <a href="https://github.com/liliBestCoder/ghost-proxifier" target="_blank"><b>Ghost Proxifier 开源版</b></a> — 纯命令行工具，MIT 开源
</p>

<p align="center">
  <b>🎬 使用视频：Ghost Proxifier 基础使用演示</b>
</p>

<p align="center">
  <a href="https://www.bilibili.com/video/BV1TkTP61Eyb/" target="_blank">
    <img src="bilibili-cover.png" alt="观看 Ghost Proxifier 使用介绍视频" width="640">
  </a>
</p>

### ⚠️ 使用注意
<blockquote>
<p><font color="#d93025"><b>关于 Windows 安全提示：</b></font><br>目前项目尚未购买微软代码签名证书，因此使用 Microsoft Edge 下载安装包时，部分杀毒软件可能会误报，Windows SmartScreen 也可能弹出拦截提示。</p>
<p>如果 Edge 阻止下载，可在 Edge 中进入：<code>设置 → 隐私、搜索和服务 → 安全性</code>，暂时关闭“防止有害网站和下载”，完成安装包下载后建议立即恢复该设置。</p>
<p>如果运行安装包时仍被 SmartScreen 拦截，在蓝色提示窗口中点击：<code>更多信息 → 仍要运行</code>。</p>
<p>请仅在确认安装包来自本项目官方 Releases 页面，并核对文件来源后再进行上述操作。</p>
<p><font color="#d93025"><b>注入前请确保目标程序及其子进程已经完全退出。</b></font><br>若程序已经在后台运行，注入可能不会生效。请先完全退出程序，再将快捷方式或 <code>.exe</code> 文件拖入窗口。</p>
</blockquote>

## 适用场景

- AI 编程，例如 Codex、Claude Desktop、Claude Code、Antigravity、Cursor 等等。
- 多个 VPN/代理软件混用时，只代理指定应用，减少虚拟网卡和路由规则之间的冲突。
- 为不遵循系统代理的命令行工具、开发工具和游戏客户端配置独立代理。
- 为不同应用或账号分配不同代理节点，实现网络 IP 层面的隔离。

## 核心特性

- **拖拽即用**：把快捷方式或 `.exe` 往软件里一拖，秒级开启代理。
- **子进程自动追踪**：自动接管目标程序创建的所有子进程（如浏览器子进程），无需手动配置 PID。
- **支持 HTTP / SOCKS5 协议**：全面兼容主流代理软件，支持配置账号与密码认证，满足各种网络代理环境。
- **UDP 转发与 QUIC 防绕过**：支持 UDP 流量代理转发，自动阻止浏览器走 QUIC 协议绕过代理，确保网络流量 100% 走代理。
- **WinStore 应用原生支持**：完美代理 ChatGPT、Claude 等 WinStore 应用；WinStore 应用自动更新后能自动感知适应，无需重新配置。
- **防泄露 DNS 解析机制**：DNS 查询自动通过代理转发，内置 DoH 阻断防止浏览器绕过代理；提供 DNS 严格模式，代理解析失败时拒绝明文外发，彻底防止域名泄露。
- **一键排障诊断包**：可在设置中一键导出排障诊断包，方便提交反馈与快速排查问题。
- **个性化设置与多语言**：支持自定义关闭窗口时的行为（如最小化到系统托盘后台运行）；界面原生支持**简体中文与英文**一键切换。
- **实时流量监控与稳定守护**：直观查看各个进程的实时网络速率与流量统计，内置后台守护机制保证长久稳定运行。

## 已支持应用

<table width="100%" style="table-layout: fixed;">
  <tr>
    <td align="center" width="10%"><img src="icons/chrome.exe.png" width="40" alt="Chrome"><br><sub>Chrome</sub></td>
    <td align="center" width="10%"><img src="icons/msedge.exe.png" width="40" alt="MS Edge"><br><sub>MS Edge</sub></td>
    <td align="center" width="10%"><img src="icons/firefox.exe.png" width="40" alt="Firefox"><br><sub>Firefox</sub></td>
    <td align="center" width="10%"><img src="icons/claude_desktop.png" width="40" alt="Claude Desktop"><br><sub>Claude Desktop</sub></td>
    <td align="center" width="10%"><img src="icons/claude.exe.png" width="40" alt="Claude Code"><br><sub>Claude Code</sub></td>
    <td align="center" width="10%"><img src="icons/Codex.png" width="40" alt="Codex"><br><sub>Codex</sub></td>
    <td align="center" width="10%"><img src="icons/antigravity.exe.png" width="40" alt="Antigravity"><br><sub>Antigravity</sub></td>
    <td align="center" width="10%"><img src="icons/node.png" width="40" alt="Node.js"><br><sub>Node.js</sub></td>
    <td align="center" width="10%"><img src="icons/python.exe.png" width="40" alt="Python"><br><sub>Python</sub></td>
    <td align="center" width="10%"><img src="icons/ssh.png" width="40" alt="SSH"><br><sub>SSH</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="icons/finalshell.exe.png" width="40" alt="FinalShell"><br><sub>FinalShell</sub></td>
    <td align="center"><img src="icons/xshell.exe.png" width="40" alt="Xshell"><br><sub>Xshell</sub></td>
    <td align="center"><img src="icons/mysqlworkbench.exe.png" width="40" alt="MySQL Workbench"><br><sub>MySQL Workbench</sub></td>
    <td align="center"><img src="icons/bluestacks_x.png" width="40" alt="BlueStacks X"><br><sub>BlueStacks X</sub></td>
    <td align="center"><img src="icons/cmd.exe.png" width="40" alt="CMD"><br><sub>CMD</sub></td>
    <td align="center"><img src="icons/powershell.exe.png" width="40" alt="PowerShell"><br><sub>PowerShell</sub></td>
    <td align="center"><img src="icons/cf.exe.png" width="40" alt="CF (穿越火线)"><br><sub>CF</sub></td>
    <td align="center"><img src="icons/hyperdown.png" width="40" alt="HyperDown"><br><sub>HyperDown</sub></td>
    <td align="center"><img src="icons/mstsc.exe.png" width="40" alt="MSTSC (远程桌面)"><br><sub>MSTSC</sub></td>
    <td align="center"><img src="icons/multilogin.exe.png" width="40" alt="Multilogin"><br><sub>Multilogin</sub></td>
  </tr>
</table>

> 理论上支持所有使用 Winsock 的 Windows 应用，以上为已测试和验证过的应用。

## 快速使用

1. 从 [Releases](https://github.com/liliBestCoder/ghost-proxifier-pro/releases) 下载并启动 Ghost Proxifier Pro。
2. 在界面中配置上游 HTTP / SOCKS5 代理和 DNS 设置。
3. 将目标程序的快捷方式或 `.exe` 文件拖入窗口，启动代理进程。

## 架构概览

```text
                           Ghost Proxifier Pro 架构
┌─────────────────────────────────────────────────────────────────────────────┐
│                         目标进程 (e.g. Chrome / ChatGPT)                    │
│                                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────────────────┐  │
│  │ DNS 查询  │   │ TCP 连接  │   │ UDP 发送  │   │ 8.8.8.8:53              │  │
│  │          │   │          │   │          │   │                         │  │
│  │ getaddrinfo│   │ connect()│   │ sendto() │   │ sendto(53)              │  │
│  │GetAddrInfoW│   │ConnectEx()│  │WSASendTo()│  │WSASendTo()              │  │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬────────────────────┘  │
│       │              │              │              │                       │
│       └──────┬───────┘              │              │                       │
│              │                      │              │                       │
│         ┌────┴─────────────┐   ┌────┴─────────────┐ ┌────┴─────────────┐   │
│         │ 共享内存 DNS 缓存│   │ 重定向到代理通道 │ │ UDP ASSOCIATE   │   │
│         │ IOCP 线程池      │   │ HTTP / SOCKS5    │ │ STUN 连通性探针 │   │
│         │ Strict 模式防泄露│   │ 用户名密码认证   │ │ QUIC 降级阻断   │   │
│         └──────────────────┘   └──────────────────┘ └─────────────────┘   │
│                                                                             │
│                    ghost_core.dll (注入到目标进程)                            │
└─────────────────────────────────────────────────────────────────────────────┘
                   │                       │
                   │   127.0.0.1:2080      │
                   │                       │
            ┌──────┴───────┐      ┌────────┴────────┐
            │ 上游 HTTP /  │      │ Watchdog 守护   │
            │ SOCKS5 代理  │      │ 崩溃Dump/权限回收│
            │ (Clash/v2ray)│      │ 事件日志镜像    │
            └──────────────┘      └─────────────────┘
```

不装 TUN/TAP 虚拟网卡，不走 WFP 内核驱动。Ghost Proxifier 使用基于 MinHook 的用户态 API Hook，拦截 Winsock 函数，只接管用户选中的进程及其子进程。

## 与同类工具对比

| 特性 | Ghost Proxifier Pro | Proxifier | ProxyBridge | Antigravity-Proxy |
| :--- | :---: | :---: | :---: | :---: |
| 图形界面与拖拽操作 | ✅ | ⚠️ 需配置规则 | ⚠️ 需配置规则 | ❌ |
| 子进程自动追踪 | ✅ | ⚠️ 规则匹配 | ⚠️ 规则匹配 | ❌ |
| 是否需要虚拟网卡/驱动 | ❌ | ⚠️ WFP 驱动 | ⚠️ WinDivert 驱动 | ❌ |
| 适用范围 | ✅ 通用多应用 | ✅ 通用多应用 | ✅ 通用多应用 | ⚠️ 主要面向单一应用 |
| DNS / DoH / QUIC 处理 | ✅ 内置处理 | ⚠️ 需额外配置 | ⚠️ 需额外配置 | ❌ |

## 运行截图

<img src="process.png" width="880" alt="进程管理" />

<img src="flow.png" width="880" alt="流量监控" />

<img src="safe_dns.png" width="880" alt="安全 DNS" />

<img src="upstream.png" width="880" alt="上游代理设置" />

## FAQ

**Ghost Proxifier Pro 收费吗？**

Ghost Proxifier Pro 现已**完全免费开放（FREE & UNLOCKED）**。¥0.00 无需注册或激活，即可无限制使用拖拽注入、无限应用代理、SOCKS5 / UDP 转发、进程树追踪等全部高级功能。

**Pro 版和开源版有什么区别？**

Pro 版提供图形界面、进程规则管理、流量监控、子进程自动追踪、SOCKS5 认证支持、Watchdog 自动重连和 MSI 安装包。开源版是纯命令行工具。

**如果上游节点页面不能新增节点或编辑节点怎么办？**

多半是软件安装目录配置文件损坏或权限异常导致的。解决方法非常简单：重新点击运行下载的 `.msi` 安装文件，在弹出的安装界面中选择 **Repair (修复)**，完成自动修复后重启 Ghost Proxifier Pro 即可恢复正常。

**启动 ChatGPT / Claude WinStore 程序遇到 `create process error 5` 异常？**

出现 `create process error 5` 错误多半是因为 Windows 当前登录账户不在管理员组、缺乏某些底层 API 调用权限导致的。只需右键桌面或开始菜单中的 **Ghost Proxifier Pro 快捷方式**，选择 **“以管理员身份运行”** 重新启动软件即可。

**如何反馈问题？**

您可以在软件的“设置”页面点击 **【导出排障包】** 生成脱敏诊断文件，然后通过 [GitHub Issue](https://github.com/liliBestCoder/ghost-proxifier-pro/issues) 或官方社群发给开发者排查。

## 企业合作与社群

如果您的企业在出海运营、跨境电商、游戏代理、研发办公或合规审计等场景下，需要更强大的集中管理功能（如全局配置下发、访问审计与监控、动态访问阻断、专有驱动与协议定制），欢迎联系我们探讨合作。

- [QQ 交流群 945138408](https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info)
- [Telegram 频道 @ghostproxifier](https://t.me/ghostproxifier)
- [Telegram 群组](https://t.me/+SCVIJJFocWAxN2Y9)

## 支持项目

如果 Ghost Proxifier 对你有帮助，欢迎通过微信或 PayPal 支持项目。你的支持将用于软件的持续更新、维护和日常运营：

<table><tr>
  <td align="center"><img src="weixin-pay.jpg" alt="微信支付捐助二维码" width="240" height="240" style="object-fit: contain;"></td>
  <td align="center"><img src="palpay-pay.jpg" alt="PayPal 捐助二维码" width="240" height="240" style="object-fit: contain;"></td>
</tr></table>

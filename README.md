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
  Windows 进程级透明代理工具：通过 DLL 注入和 Winsock API Hook，让指定应用及其子进程的网络流量自动转发到 HTTP 代理，无需修改路由表或安装虚拟网卡。
</p>

<p align="center">
  🔧 <a href="https://github.com/liliBestCoder/ghost-proxifier" target="_blank"><b>Ghost Proxifier 开源版</b></a> — 纯命令行工具，MIT 开源
</p>

<p align="center">
  <a href="https://www.bilibili.com/video/BV1TkTP61Eyb/" target="_blank">
    <img src="bilibili-cover.png" alt="观看 Ghost Proxifier 使用介绍视频" width="880">
  </a>
</p>

## 核心特性

- **拖拽即用**：拖入快捷方式或 `.exe` 文件，自动注入目标进程。
- **子进程自动追踪**：自动接管目标程序创建的子进程，无需手动配置 PID。
- **进程级代理**：只代理选中的应用，不影响系统其它流量。
- **Local DNS**：DNS 查询通过代理转发，减少 DNS 泄露和污染问题。
- **DoH / QUIC 阻断**：阻止浏览器绕过代理，强制回退到 TCP 连接。
- **实时监控**：查看进程状态、代理状态和流量统计，并支持自动重连。

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
    <td align="center"><sub>...</sub></td>
  </tr>
</table>

> 理论上支持所有使用 Winsock 的 Windows 应用，以上为已测试和验证过的应用。

## 适用场景

- AI 编程工具代理，例如 Codex、Claude Code、Antigravity 等。
- 多个 VPN/代理软件混用时，只代理指定应用，减少虚拟网卡和路由规则之间的冲突。
- 为不遵循系统代理的命令行工具、开发工具和游戏客户端配置独立代理。
- 为不同应用或账号分配不同代理节点，实现网络 IP 层面的隔离。

## 快速使用

1. 从 [Releases](https://github.com/liliBestCoder/ghost-proxifier-pro/releases) 下载并启动 Ghost Proxifier Pro。
2. 在界面中配置上游 HTTP 代理和 DNS 设置。
3. 将目标程序的快捷方式或 `.exe` 文件拖入窗口，启动代理进程。

### 使用注意

拖入目标程序前，请确保该程序及其子进程已经完全退出。若程序已在后台运行，注入可能不会生效。

## 运行截图

<img src="process.png" width="880" alt="进程管理" />

<img src="flow.png" width="880" alt="流量监控" />

<img src="safe_dns.png" width="880" alt="安全 DNS" />

<img src="upstream.png" width="880" alt="上游代理设置" />

## FAQ

**Ghost Proxifier Pro 收费吗？**

目前 Pro 版免费使用，包含拖拽注入、无限应用代理、进程树追踪等功能。

**Pro 版和开源版有什么区别？**

Pro 版提供图形界面、进程规则管理、流量监控、子进程自动追踪、Watchdog 自动重连和安装包。开源版是纯命令行工具。

**如何反馈问题？**

欢迎通过 [GitHub Issue](https://github.com/liliBestCoder/ghost-proxifier-pro/issues) 或官方社群反馈问题。

## 企业合作与社群

- [QQ 交流群 945138408](https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info)
- [Telegram 频道 @ghostproxifier](https://t.me/ghostproxifier)
- [Telegram 群组](https://t.me/+SCVIJJFocWAxN2Y9)

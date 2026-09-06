<!-- LOGO & CONTACT -->
<p align="right">
  <a href="https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info" target="_blank">QQ Group</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/ghostproxifier" target="_blank">TG Channel</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/+SCVIJJFocWAxN2Y9" target="_blank">TG Group</a>
</p>

<p align="center"><img src="app_icon.ico" alt="Logo" width="64"></p>

<h1 align="center">Ghost Proxifier Pro</h1>

<p align="center">
  <a href="README.md">🇨🇳 中文</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/liliBestCoder/ghost-proxifier-pro/releases" target="_blank">Download</a>
  &nbsp;·&nbsp;
  <a href="https://ghostproxifier.com" target="_blank">Website</a>
</p>

<p align="center">
  <a href="#core-features">Core Features</a>
  &nbsp;·&nbsp;
  <a href="#supported-apps">Supported Apps</a>
  &nbsp;·&nbsp;
  <a href="#quick-start">Quick Start</a>
  &nbsp;·&nbsp;
  <a href="#architecture-overview">Architecture</a>
  &nbsp;·&nbsp;
  <a href="#use-cases">Use Cases</a>
  &nbsp;·&nbsp;
  <a href="#comparison">Comparison</a>
  &nbsp;·&nbsp;
  <a href="#screenshots">Screenshots</a>
  &nbsp;·&nbsp;
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  A process-level transparent proxy for Windows. It injects a DLL and hooks Winsock APIs to route traffic from selected applications and their child processes through HTTP / SOCKS5 proxies — without changing routing tables or installing virtual network adapters.
</p>

<p align="center">
  🔧 <a href="https://github.com/liliBestCoder/ghost-proxifier" target="_blank"><b>Ghost Proxifier Open Source</b></a> — CLI-only, MIT licensed
</p>

<p align="center">
  <b>🎬 Video Tutorial: Ghost Proxifier Basic Usage</b>
</p>

<p align="center">
  <a href="https://www.bilibili.com/video/BV1TkTP61Eyb/" target="_blank">
    <img src="bilibili-cover.png" alt="Watch the Ghost Proxifier video tutorial" width="640">
  </a>
</p>

### ⚠️ Important
<blockquote>
<p><font color="#d93025"><b>About Windows security warnings:</b></font><br>The project does not yet have a Microsoft code-signing certificate. When downloading the installer through Microsoft Edge, some antivirus software may report a false positive and Windows SmartScreen may block the download or launch.</p>
<p>If Edge blocks the download, open <code>Settings → Privacy, search, and services → Security</code> and temporarily disable “Block potentially unwanted apps and downloads”. Re-enable this setting after downloading the installer.</p>
<p>If SmartScreen still blocks the installer, click <code>More info → Run anyway</code> in the blue warning dialog.</p>
<p>Only do this after confirming that the installer came from the official project Releases page and verifying its source.</p>
<p><font color="#d93025"><b>Make sure the target application and its child processes are fully closed before injection.</b></font><br>Injection may fail if an existing instance is already running in the background. Fully exit the application before dropping its shortcut or <code>.exe</code> file into the window.</p>
</blockquote>

## Use Cases

- AI coding tools, such as Codex, Claude Desktop, Claude Code, Antigravity, Cursor, etc.
- Use multiple VPN or proxy clients together while routing only selected applications to reduce virtual-adapter and routing conflicts.
- Proxy command-line tools, developer tools, and game clients that ignore system proxy settings.
- Assign different proxy nodes to different applications or accounts for network-level IP isolation.

## Core Features

- **Drag & Drop Simplicity**: Drop any shortcut or `.exe` into the window to enable proxying instantly.
- **Auto Child-Process Tracking**: Automatically takes over all child processes (like browser subprocesses) without manual PID setup.
- **HTTP & SOCKS5 Protocol Support**: Fully compatible with mainstream proxy clients, supporting username/password authentication for any proxy environment.
- **UDP Forwarding & QUIC Protection**: Supports UDP traffic forwarding and blocks browser QUIC protocol from bypassing your proxy, keeping 100% of traffic proxied.
- **Native WinStore App Support**: Seamlessly proxies WinStore apps like ChatGPT and Claude; automatically adapts when WinStore apps auto-update to new version directories.
- **Leak-Proof DNS Resolution**: DNS queries are encrypted and routed via proxy, with built-in DoH blocking to prevent browser bypass; includes DNS Strict Mode to block unencrypted fallbacks to ISP DNS.
- **One-Click Diagnostic Pack Export**: Easily export a troubleshooting diagnostic zip from Settings for fast problem feedback and debugging.
- **Personalized Settings & Multi-Language**: Customize window close behavior (e.g. minimize to system tray) with native one-click switching between **English and Simplified Chinese**.
- **Live Traffic Monitoring & Watchdog**: View real-time bandwidth and process stats with an underlying background watchdog for maximum stability.

## Supported Apps

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
    <td align="center"><img src="icons/cf.exe.png" width="40" alt="CF (CrossFire)"><br><sub>CF</sub></td>
    <td align="center"><img src="icons/hyperdown.png" width="40" alt="HyperDown"><br><sub>HyperDown</sub></td>
    <td align="center"><img src="icons/mstsc.exe.png" width="40" alt="MSTSC (Remote Desktop)"><br><sub>MSTSC</sub></td>
    <td align="center"><img src="icons/multilogin.exe.png" width="40" alt="Multilogin"><br><sub>Multilogin</sub></td>
  </tr>
</table>

> In theory, all Windows applications using Winsock are supported. The list above contains tested and verified applications.

## Quick Start

1. Download and launch Ghost Proxifier Pro from [Releases](https://github.com/liliBestCoder/ghost-proxifier-pro/releases).
2. Configure upstream HTTP / SOCKS5 proxy and DNS settings.
3. Drop the target shortcut or `.exe` file into the window and start the proxied process.

## Architecture Overview

```text
                        Ghost Proxifier Pro Architecture
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Target Process (e.g. Chrome / ChatGPT)               │
│                                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────────────────┐  │
│  │ DNS Query │   │ TCP Connect│  │ UDP Send  │   │ 8.8.8.8:53              │  │
│  │          │   │          │   │          │   │                         │  │
│  │ getaddrinfo│   │ connect()│   │ sendto() │   │ sendto(53)              │  │
│  │GetAddrInfoW│   │ConnectEx()│  │WSASendTo()│  │WSASendTo()              │  │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬────────────────────┘  │
│       │              │              │              │                       │
│       └──────┬───────┘              │              │                       │
│              │                      │              │                       │
│         ┌────┴─────────────┐   ┌────┴─────────────┐ ┌────┴─────────────┐   │
│         │ Shared Mem Cache │   │ Redirect to Proxy│ │ UDP ASSOCIATE    │   │
│         │ IOCP Worker Pool │   │ HTTP / SOCKS5    │ │ STUN Probe       │   │
│         │ Strict Mode      │   │ Auth Support     │ │ QUIC Fallback    │   │
│         └──────────────────┘   └──────────────────┘ └──────────────────┘   │
│                                                                             │
│                   ghost_core.dll (injected into target process)              │
└─────────────────────────────────────────────────────────────────────────────┘
                   │                       │
                   │   127.0.0.1:2080      │
                   │                       │
            ┌──────┴───────┐      ┌────────┴────────┐
            │ Upstream     │      │ Watchdog Host   │
            │ HTTP / SOCKS5│      │ Crash Dump/ACL  │
            │ Proxy        │      │ Event Log Mirror│
            └──────────────┘      └─────────────────┘
```

No TUN/TAP virtual adapter or WFP kernel driver is required. Ghost Proxifier uses user-mode API Hooking based on MinHook to intercept Winsock functions and take over only selected processes and their child processes.

## Comparison

| Feature | Ghost Proxifier Pro | Proxifier | ProxyBridge | Antigravity-Proxy |
| :--- | :---: | :---: | :---: | :---: |
| GUI and drag-and-drop | ✅ | ⚠️ Rules required | ⚠️ Rules required | ❌ |
| Automatic child-process tracking | ✅ | ⚠️ Rule matching | ⚠️ Rule matching | ❌ |
| Virtual adapter/driver required | ❌ | ⚠️ WFP driver | ⚠️ WinDivert driver | ❌ |
| Application scope | ✅ General multi-app | ✅ General multi-app | ✅ General multi-app | ⚠️ Mainly single-app |
| DNS / DoH / QUIC handling | ✅ Built in | ⚠️ Extra configuration | ⚠️ Extra configuration | ❌ |

## Screenshots

<img src="process.png" width="880" alt="Process Management" />

<img src="flow.png" width="880" alt="Traffic Monitoring" />

<img src="safe_dns.png" width="880" alt="Safe DNS" />

<img src="upstream.png" width="880" alt="Upstream Proxy Settings" />

## FAQ

**Is Ghost Proxifier Pro free?**

Ghost Proxifier Pro is now **completely free with all Pro features unlocked (FREE & UNLOCKED)**. $0.00 without registration or activation to enjoy unlimited drag-and-drop injection, infinite processes, SOCKS5 / UDP forwarding, and process tree tracking.

**What is the difference between Pro and the open-source version?**

The Pro version provides a GUI, process rules, traffic monitoring, automatic child-process tracking, SOCKS5 authentication, Watchdog reconnection, and an MSI installer. The open-source version is CLI-only.

**What if I cannot add or edit nodes on the Upstream Nodes page?**

This is usually caused by corrupted files in the software installation directory. Simply run the downloaded `.msi` installer again and select **Repair** to restore the installation.

**Getting `create process error 5` when launching ChatGPT / Claude WinStore apps?**

`create process error 5` is usually caused by Windows user permission constraints. Simply right-click the **Ghost Proxifier Pro shortcut** and select **"Run as Administrator"** to resolve it.

**How can I report an issue?**

You can click **[Export Diagnostic Pack]** in the Settings page to generate a redacted diagnostic zip file, then send it via [GitHub Issues](https://github.com/liliBestCoder/ghost-proxifier-pro/issues) or community channels.

## Community

If your enterprise requires centralized management features for overseas operations, cross-border e-commerce, game proxying, development, or compliance auditing—such as global configuration distribution, access auditing and monitoring, dynamic access blocking, or custom driver and protocol integration—feel free to contact us to discuss cooperation.

- [QQ Group 945138408](https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Ilc3Zm41TUQ1RkU1alFNOUVxMW5hckVNZmpqSFN6V25JcUtyK3duaFZWYisyblVsSEdFNzZ3RUQrTmt3enVIajgiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=u7S-lMspdK2PJy1DWRR7cda6y4mYYoKKmA_GaiXg1g_ArnccknlAlDz-zbdWg2H5s7nt_PrY47zqHFCZI8Ffaw&svctype=4&tempid=h5_group_info)
- [Telegram Channel @ghostproxifier](https://t.me/ghostproxifier)
- [Telegram Group](https://t.me/+SCVIJJFocWAxN2Y9)

## Support the Project

If Ghost Proxifier is useful to you, you can support the project via WeChat or PayPal. Your support helps fund ongoing development, maintenance, and operation of the software:

<table><tr>
  <td align="center"><img src="weixin-pay.jpg" alt="WeChat donation QR code" width="240" height="240" style="object-fit: contain;"></td>
  <td align="center"><img src="palpay-pay.jpg" alt="PayPal donation QR code" width="240" height="240" style="object-fit: contain;"></td>
</tr></table>

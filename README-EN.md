<!-- LOGO & CONTACT -->
<p align="right">
  <a href="https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info" target="_blank">QQ Group</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/ghostproxifier" target="_blank">TG Channel</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/+SCVIJJFocWAxN2Y9" target="_blank">TG Group</a>
</p>

<p align="center">
  <img src="app_icon.ico" alt="Logo" width="64">
</p>

<h1 align="center">Ghost Proxifier Pro</h1>

<p align="center">
  <a href="README.md">🇨🇳 中文</a>
  &nbsp;·
  <a href="https://github.com/liliBestCoder/ghost-proxifier-pro/releases" target="_blank">Download</a>
  &nbsp;·
  <a href="https://ghostproxifier.com" target="_blank">Website</a>
</p>

<p align="center">
  <a href="#supported-apps">Supported Apps</a>
  ·
  <a href="#primary-use-cases">Primary Use Cases</a>
  ·
  <a href="#what-problem-does-it-solve">What Problem Does It Solve</a>
  ·
  <a href="#architecture">Architecture</a>
  ·
  <a href="#how-it-works">How It Works</a>
  ·
  <a href="#features">Features</a>
  ·
  <a href="#comparison-with-similar-tools">Comparison</a>
  ·
  <a href="#usage">Usage</a>
  ·
  <a href="#screenshots">Screenshots</a>
  ·
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  Process-level transparent proxy engine — injects a DLL into target processes, hooks the Winsock API, and transparently forwards all network traffic through an HTTP proxy. No virtual adapter. No routing table changes. The proxy is completely invisible to applications.
</p>

<p align="center">
  🔧 <a href="https://github.com/liliBestCoder/ghost-proxifier" target="_blank"><b>Ghost Proxifier (Open Source)</b></a> — CLI-only tool, MIT licensed, ideal for DIY and custom development
</p>

## Supported Apps

<table width="100%" style="table-layout: fixed;">
  <tr>
    <td align="center" width="10%"><img src="icons/chrome.exe.png" width="40" alt="Chrome"><br><sub>Chrome</sub></td>
    <td align="center" width="10%"><img src="icons/msedge.exe.png" width="40" alt="MS Edge"><br><sub>MS Edge</sub></td>
    <td align="center" width="10%"><img src="icons/claude.exe.png" width="40" alt="Claude Code"><br><sub>Claude Code</sub></td>
    <td align="center" width="10%"><img src="icons/Codex.png" width="40" alt="Codex"><br><sub>Codex</sub></td>
    <td align="center" width="10%"><img src="icons/antigravity.exe.png" width="40" alt="Antigravity"><br><sub>Antigravity</sub></td>
    <td align="center" width="10%"><img src="icons/node.png" width="40" alt="Node.js"><br><sub>Node.js</sub></td>
    <td align="center" width="10%"><img src="icons/python.exe.png" width="40" alt="Python"><br><sub>Python</sub></td>
    <td align="center" width="10%"><img src="icons/ssh.png" width="40" alt="SSH"><br><sub>SSH</sub></td>
    <td align="center" width="10%"><img src="icons/finalshell.exe.png" width="40" alt="FinalShell"><br><sub>FinalShell</sub></td>
    <td align="center" width="10%"><img src="icons/xshell.exe.png" width="40" alt="Xshell"><br><sub>Xshell</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="icons/mysqlworkbench.exe.png" width="40" alt="MySQL Workbench"><br><sub>MySQL Workbench</sub></td>
    <td align="center"><img src="icons/cmd.exe.png" width="40" alt="CMD"><br><sub>CMD</sub></td>
    <td align="center"><img src="icons/powershell.exe.png" width="40" alt="PowerShell"><br><sub>PowerShell</sub></td>
    <td align="center"><sub>...</sub></td>
  </tr>
</table>

> Theoretically supports all Windows applications that use Winsock. The list above represents tested and verified applications — more are being validated continuously.

## Primary Use Cases

* AI Programming / Vibe Coding Acceleration: Proxies Codex, Claude Code, Antigravity, and Cursor to solve API timeouts and drops.
* Cross-Border Multi-Account Anti-Association: Assigns independent proxy IPs per process for physical isolation of e-commerce & social media accounts.
* Concurrent VPN & Proxy Coexistence: Eliminates routing conflicts with corporate VPNs by proxying only designated applications.
* Transparent Proxy for Dev & CLI Tools: Intercepts CMD, PowerShell, FinalShell, Xshell, and MySQL Workbench that ignore system proxies.
* Game Launchers & Dedicated App Proxying: Assigns dedicated proxy nodes to specific games or software, avoiding global proxy latency.

## What Problem Does It Solve?

### Apps That Ignore the System Proxy

Chrome mostly behaves, but Telegram, Antigravity, game launchers — they completely ignore Windows proxy settings. Ghost Proxifier enters the process itself, intercepting network requests at the Winsock layer and forcing them through your designated proxy. **No traffic leaks.**

### VPN and Proxy Can't Coexist

Your corporate VPN connects to the intranet while Clash tries to bypass the firewall — routing tables clash, and one of them always breaks. In TUN mode, the virtual adapter constantly switches with the VPN adapter, causing extra latency from kernel/user-mode transitions.

Ghost Proxifier **installs no virtual adapter, touches no routing table**. It only proxies the processes you select; all other traffic is left untouched. VPN, intranet, and proxy can all stay online simultaneously with zero interference.

### Child Processes Run Naked

You drop a launcher into the proxy, it spawns ten child windows — and those children's traffic goes straight to real IPs, rendering the proxy useless. The Pro edition automatically tracks the process tree. Drop it once, and the entire process family is covered.

## Architecture

```
                        Ghost Proxifier Pro Architecture
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Target Process (e.g. Chrome)                         │
│                                                                             │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────────────────┐  │
│  │ DNS Query │   │ TCP Connect│  │ Data Send │   │ 8.8.8.8:53             │  │
│  │          │   │          │   │          │   │                         │  │
│  │ getaddrinfo│   │ connect()│   │ send() / │   │ sendto(53)             │  │
│  │GetAddrInfoW│   │ConnectEx()│  │WSASend() │   │WSASendTo()             │  │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬──────────────────┘  │
│       │              │              │              │                       │
│       └──────┬───────┘              │              │                       │
│              │                      │              │                       │
│         ┌────┴─────┐           ┌────┴─────┐   ┌────┴─────┐                 │
│         │  HOOK    │           │  HOOK    │   │  HOOK    │                 │
│         └────┬─────┘           └────┬─────┘   └────┬─────┘                 │
│              │                      │              │                       │
│         ┌────┴─────┐           ┌────┴─────┐   ┌────┴─────┐                 │
│         │ Local DNS │           │ Redirect to  │   │ Lazy Handshake       │
│         │ Proxy     │           │ Proxy, Save  │   │ 1. Check PendingMap  │
│         │ UDP → TCP │           │ to PendingMap│   │ 2. HTTP CONNECT      │
│         │ Forward to│           │              │   │ 3. Send original data│
│         │ 8.8.8.8:53│           │              │   │                      │
│         └────────────┘           └──────────┘   └─────────────────────────┘
│                                                                             │
│                   ghost_core.dll (injected into target process)              │
└─────────────────────────────────────────────────────────────────────────────┘
                   │                       │
                   │   127.0.0.1:2080      │
                   │                       │
            ┌──────┴───────┐      ┌────────┴────────┐
            │  Upstream     │      │  DNS Results    │
            │  HTTP CONNECT │      │                 │
            │  Proxy        │      │  IP → Hostname  │
            │ (V2Ray/Clash/ │      │                 │
            │  NekoBox/...) │      │                 │
            └──────────────┘      └─────────────────┘
```

No TUN/TAP virtual adapter — that gets flagged by anti-detection systems. No WFP kernel driver — that requires an EV code-signing certificate. Our approach is **user-mode API Hooking**, deeply intercepting 25+ Winsock functions via MinHook. Written in C++17, minimal memory footprint, injection completes in milliseconds.

## How It Works

### 1. HTTP CONNECT Protocol

Ghost Proxifier uses the standard **HTTP CONNECT** method to establish a tunnel through the upstream proxy:

```text
# When domain is resolved
CONNECT www.google.com:443 HTTP/1.1\r\nHost: www.google.com:443\r\n\r\n

# When domain resolution fails (fallback)
CONNECT 142.251.45.10:443 HTTP/1.1\r\nHost: 142.251.45.10:443\r\n\r\n
```

After the proxy responds with `HTTP/1.1 200 Connection Established\r\n\r\n`, the tunnel is up and bidirectional forwarding begins.

`connect()` receives an **IP address**, not a hostname. Ghost Proxifier uses the **IP → Hostname** mapping built during DNS resolution to prefer hostname-based CONNECT requests, enabling upstream domain-based routing. When the hostname is unavailable, it falls back to the IP — the upstream can then leverage GeoIP rules. This is why **Local DNS anti-poisoning** is critical.

### 2. Lazy Handshake

Browsers like Chrome use non-blocking I/O with I/O completion ports. Synchronously waiting for the proxy handshake during `connect()` would trigger Chrome's hang detection.

Ghost Proxifier's solution:

| Phase | Operation | Blocking? |
|-------|-----------|-----------|
| `connect()` | Redirect to proxy address, save target to PendingMap | ❌ Non-blocking |
| Waiting | App event loop runs normally | ❌ |
| First `send()` | Retrieve target from PendingMap, complete HTTP CONNECT | ✅ Brief (< 5ms) |
| Subsequent `send()` | Direct forwarding | ❌ |

`connect()` returns success immediately — the application believes the connection is established. The actual proxy handshake is deferred until the first `send()`, completely transparent to the application.

### 3. Built-in Local DNS

System DNS has two fundamental problems:
- **DNS Leakage** — your ISP can see every DNS query
- **DNS Poisoning** — the GFW returns forged IPs, causing connections to be reset

Ghost Proxifier's DNS flow:

```
App DNS Query (UDP)
    ↓ Hook intercepts
Local DNS Proxy (127.0.0.1:random port)
    ↓ UDP → TCP conversion
CONNECT tunnel through proxy to 8.8.8.8:53
    ↓ TCP DNS query
Google DNS returns the real result
    ↓ Record IP → Hostname mapping (for use during connect phase)
```

DNS queries travel through the encrypted proxy tunnel, preventing ISP snooping and GFW poisoning. The resulting IP→Hostname mapping table, combined with upstream GeoIP/GeoSite routing rules, ensures traffic takes the optimal path.

### 4. DoH Blocking

Browsers like Chrome enable DNS-over-HTTPS (DoH) by default, connecting directly to `8.8.8.8:443`, `1.1.1.1:443`, and other DoH servers — bypassing the Local DNS Proxy entirely.

Ghost Proxifier recognizes known DoH server IPs and returns `WSAECONNREFUSED` at the `connect()` stage, forcing the browser to fall back to standard DNS:

```
Chrome → connect(8.8.8.8:443)  → DoH request
              ↓ Hook identifies DoH server
          Returns WSAECONNREFUSED
              ↓ Chrome falls back
Chrome → sendto(8.8.8.8:53)   → Standard DNS → handled by Local DNS Proxy ✅
```

### 5. QUIC Blocking

QUIC (HTTP/3) runs over UDP 443 and likewise bypasses the proxy. Ghost Proxifier blocks UDP 443 traffic on all paths — `sendto`/`WSASendTo` and `recvfrom`/`WSARecvFrom` — returning `WSAENETUNREACH` to trigger the browser's TCP fallback (HTTP/2 or HTTP/1.1), which then goes through the HTTP CONNECT tunnel.

## Features

### Automatic Process Tree Tracking

Drop in one main process and the engine automatically identifies and injects into all child processes it creates. Chrome's Network Service, GPU Process, Utility Process — all covered automatically. No manual PID configuration needed.

Built-in Watchdog continuously monitors hook status and automatically reconnects if the proxy disconnects due to network fluctuations.

### Traffic Visualization

Glassmorphism UI + dark mode. Real-time traffic charts, process-level network topology, status indicators (green / yellow / red). Refreshes every 2 seconds, smooth with no jitter.

### DNS Anti-Poisoning + DoH Blocking

Built-in Local DNS routes all DNS queries through the encrypted tunnel, eliminating ISP poisoning. Simultaneously blocks DoH direct connections from browsers like Chrome, forcing all DNS through the local proxy to ensure upstream GeoIP/GeoSite routing rules receive genuine IP addresses.

## Comparison with Similar Tools

| Technical Dimension | Ghost Proxifier Pro | Proxifier | ProxyBridge | Antigravity-Proxy |
| :--- | :---: | :---: | :---: | :---: |
| **Core Architecture** | Winsock API Hook (DLL Injection) | WFP Kernel Driver / Winsock | WinDivert Packet Filter Driver | DLL Injection / API Hook |
| **Kernel Driver Required** | ❌ No Driver Needed (User-mode) | ⚠️ Requires WFP Driver | ⚠️ Requires WinDivert Driver | ❌ No Driver Needed (User-mode) |
| **App Support Scope** | ✅ General Multi-App Manager (20+ Apps) | ✅ General App Rules | ✅ General App Rules | ⚠️ Specialized for Antigravity |
| **UI & Usability** | ✅ Modern Windows GUI (Drag & Drop) | Classic Desktop GUI | Desktop GUI / CLI | Basic CLI / Simple UI |
| **Process Tree Tracking** | ✅ Auto-injects all child processes | ✅ Rule-based process matching | ⚠️ Process-name filtering | ❌ Target process only |
| **DoH / QUIC Blocking** | ✅ Built-in active blocking (Force TCP) | ❌ Manual firewall rules needed | ❌ No built-in blocking | ❌ No built-in blocking |

## Usage

Operate through the Pro graphical interface: drag and drop or manually select a target process shortcut or exe to auto-inject. The engine automatically identifies and injects into the process and all its children. The main window provides a process list, proxy status, traffic statistics, and more in real time.

All configuration — upstream proxy nodes, DNS servers, injection rules — is done within the GUI. No manual config file editing required.

> ⚠️ <font color="#ff3333"><b>Important Usage Notice:</b></font><br>
> <font color="#ff3333">Before dragging a shortcut (<code>.lnk</code>) or executable (<code>.exe</code>) file into Ghost Proxifier Pro, please ensure there are <b>no existing running instances</b> of the target process in the background. If an instance is already running, proxy injection will not succeed (the status indicator light will not illuminate). Please completely exit the target process before dragging it in to launch.</font>

## Screenshots

<img src="process.png" width="880" alt="Process Management" />

<img src="flow.png" width="880" alt="Traffic Flow" />

<img src="safe_dns.png" width="880" alt="Safe DNS" />

<img src="upstream.png" width="880" alt="Upstream Settings" />

## FAQ

**Is Ghost Proxifier paid?**

No. Ghost Proxifier is now completely free and has unlocked all Pro features. All users can enjoy unlimited drag-and-drop injection, unlimited concurrent applications, and no per-session runtime limits. There are no longer any process or time restrictions.

**How is this different from the open-source edition?**

The Pro edition offers a modern graphical UI, process rule management, traffic visualization panel, automatic process tree tracking, Watchdog auto-reconnect, MSI installer, and other advanced features. The open-source edition is a command-line-only tool.

**How do I report an issue?**

If you encounter any issues during installation or usage, feel free to [Submit an Issue](https://github.com/liliBestCoder/ghost-proxifier-pro/issues) or reach out via our community channels.

## Enterprise Partnership & Community

If your enterprise requires centralized management features (e.g., global config distribution, access auditing, dynamic blocking, custom driver/protocol integration), feel free to contact us:

- **QQ Group**: [**945138408**](https://qun.qq.com/universal-share/share?ac=1&authKey=jLD98s%2BuMM87y8zEcP6tBhrYEyCh2H9gnwigYoYoNLIjY4XqRWTFT0cmx0QDF4hT&busi_data=eyJncm91cENvZGUiOiI5NDUxMzg0MDgiLCJ0b2tlbiI6Imh0cHlaWUViTURaNXoyNklyMGI1akVIcFI5Q3ZIVEFzYktZTEQyRkUwallRck1tQ0d4SFN1d3haNmVMR0lzL3kiLCJ1aW4iOiIxODcxODE0NzQ5In0%3D&data=iw28-MBoXAQ6Pc8ThvaD6YOIC2xcOqodEkkc4rW6JgVNZWNxS5Ka8rqbOiJFZov5cN1L6atFKQwdpoHkdb34fw&svctype=4&tempid=h5_group_info)
- **Telegram Channel**: [@ghostproxifier](https://t.me/ghostproxifier)
- **Telegram Group**: [Ghost Proxifier](https://t.me/+SCVIJJFocWAxN2Y9)
- **GitHub Issues**: [Report Bugs or Suggestions](https://github.com/liliBestCoder/ghost-proxifier-pro/issues)

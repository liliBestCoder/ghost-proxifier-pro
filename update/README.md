# update/

应用内自动更新从这个目录取更新信息。站点地址：

- `https://ghostproxifier.com/update/personal.json`
- `https://ghostproxifier.com/update/personal.json.sig`

同样的两个文件也会作为 Release 资产发布，客户端在站点不可达时改从 `https://github.com/liliBestCoder/ghost-proxifier-pro/releases/latest/download/personal.json`（及 `.sig`）获取。两处是**同一份签名字节**。

## 不要手工编辑

这两个文件由发版流水线在每次发版时生成、签名并提交到这里。**手工改动任何一个字节都会让签名失效**，客户端会拒收整份清单，结果是所有用户收不到这次更新。

同样，**不要对这两个文件做换行符转换**（例如编辑器自动补一个末尾换行）：被签名的是文件的原始字节。

## 格式

`personal.json`（企业版将来使用 `enterprise.json`）：

```json
{ "sku": "personal",
  "version": "1.3.0",
  "url": "https://github.com/liliBestCoder/ghost-proxifier-pro/releases/download/v1.3.0/GhostProxifier-1.3.0-win64.msi",
  "size": 4718592,
  "sha256": "<64 位小写十六进制>",
  "notesUrl": "https://github.com/liliBestCoder/ghost-proxifier-pro/releases/tag/v1.3.0" }
```

`personal.json.sig` 装着签名证书与两个签名（ECDSA P-256）：

```json
{ "cert": "<base64>", "certSig": "<base64>", "sig": "<base64>" }
```

客户端的校验顺序：用编译进程序的根公钥验证书 → 检查证书没被吊销、没过期 → 用证书里的签名公钥验 `personal.json` 的原始字节 → 逐字段检查（`sku` 与本机一致、`url` 在允许的地址前缀内、`size`/`sha256` 合法）。任何一步失败，这份清单就不被信任，客户端不会提示任何更新，更不会下载。下载完成后，安装包的大小和 SHA-256 必须与清单一致，否则删除、不安装。

信任只来自签名，不来自文件放在哪里：即使站点或 GitHub 被攻破，没有签名密钥也推不出一个能被安装的文件。

## 发版后怎么确认

流水线在提交后会自动轮询站点和兜底地址，逐字节比对并完整验签，最多等 15 分钟；不一致会让发版流水线失败。手工确认可以：

```bash
curl -sS https://ghostproxifier.com/update/personal.json
curl -sS -o /dev/null -w "%{http_code}\n" https://ghostproxifier.com/update/personal.json.sig
```

两个都应返回 200。如果 Pages 部署失败导致长时间拿不到新文件，可以重新触发一次 Pages 构建。

## 历史

早期版本曾在这里放过一个未签名的 `latest.json`。没有任何正式发布的客户端读过它，新格式上线时已删除，不需要兼容。

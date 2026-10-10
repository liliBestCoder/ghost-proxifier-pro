#!/usr/bin/env python3
"""Send the latest GitHub release to the Ghost Proxifier Telegram channel."""

from __future__ import annotations

import html
import json
import os
import re
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


REPOSITORY = "liliBestCoder/ghost-proxifier-pro"
RELEASES_URL = f"https://api.github.com/repos/{REPOSITORY}/releases/latest"
MARKDOWN_URL = "https://api.github.com/markdown"
TELEGRAM_CHAT = "@ghostproxifier"
TELEGRAM_TEXT_LIMIT = 4096


def request(url: str, *, data: bytes | None = None, accept: str = "application/vnd.github+json") -> bytes:
    headers = {
        "Accept": accept,
        "User-Agent": "ghost-proxifier-telegram-notifier",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = Request(url, data=data, headers=headers)
    with urlopen(req, timeout=30) as response:
        return response.read()


class TelegramHTMLRenderer(HTMLParser):
    """Translate GitHub-rendered HTML into Telegram's supported HTML subset."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.list_depth = 0
        self.pre_depth = 0
        self.suppressed_depth = 0
        self.alert_title_depth = 0
        self.anchor_stack: list[bool] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag in {"script", "style", "svg"}:
            self.suppressed_depth += 1
            return
        if self.suppressed_depth:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("<b>")
        elif tag in {"strong", "b"}:
            self.parts.append("<b>")
        elif tag in {"em", "i"}:
            self.parts.append("<i>")
        elif tag in {"del", "s", "strike"}:
            self.parts.append("<s>")
        elif tag == "pre":
            self.pre_depth += 1
            self.parts.append("<pre>")
        elif tag == "code" and self.pre_depth == 0:
            self.parts.append("<code>")
        elif tag == "a":
            href = attributes.get("href") or ""
            is_safe_link = urlparse(href).scheme.lower() in {"http", "https", "tg"}
            self.anchor_stack.append(is_safe_link)
            if is_safe_link:
                self.parts.append(f'<a href="{html.escape(href, quote=True)}">')
        elif tag in {"ul", "ol"}:
            self.list_depth += 1
            self.parts.append("\n")
        elif tag == "p" and "markdown-alert-title" in (attributes.get("class") or ""):
            self.alert_title_depth += 1
            self.parts.append("<b>")
        elif tag == "li":
            self.parts.append(f"{'  ' * max(self.list_depth - 1, 0)}• ")
        elif tag == "blockquote":
            self.parts.append("<blockquote>")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "hr":
            self.parts.append("\n────────\n")
        elif tag == "tr":
            self.parts.append("\n")
        elif tag in {"td", "th"}:
            if self.parts and not self.parts[-1].endswith(("\n", " | ")):
                self.parts.append(" | ")
            if tag == "th":
                self.parts.append("<b>")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"}:
            self.suppressed_depth = max(0, self.suppressed_depth - 1)
            return
        if self.suppressed_depth:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "strong", "b"}:
            self.parts.append("</b>\n\n")
        elif tag in {"em", "i"}:
            self.parts.append("</i>")
        elif tag in {"del", "s", "strike"}:
            self.parts.append("</s>")
        elif tag == "pre":
            self.pre_depth = max(0, self.pre_depth - 1)
            self.parts.append("</pre>\n\n")
        elif tag == "code" and self.pre_depth == 0:
            self.parts.append("</code>")
        elif tag == "a":
            if self.anchor_stack and self.anchor_stack.pop():
                self.parts.append("</a>")
        elif tag == "li":
            self.parts.append("\n")
        elif tag in {"ul", "ol"}:
            self.list_depth = max(0, self.list_depth - 1)
            self.parts.append("\n")
        elif tag == "blockquote":
            self.parts.append("</blockquote>\n\n")
        elif tag == "p":
            if self.alert_title_depth:
                self.alert_title_depth -= 1
                self.parts.append("</b>")
            self.parts.append("\n\n")
        elif tag in {"div", "section", "table", "tr"}:
            self.parts.append("\n\n")
        elif tag in {"td", "th"} and tag == "th":
            self.parts.append("</b>")

    def handle_data(self, data: str) -> None:
        if not self.suppressed_depth:
            self.parts.append(html.escape(data, quote=False))

    def render(self) -> str:
        rendered = "".join(self.parts)
        rendered = re.sub(r"[ \t]+\n", "\n", rendered)
        rendered = re.sub(r"\n{3,}", "\n\n", rendered)
        return rendered.strip()


class PlainTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def count_telegram_characters(message_html: str) -> int:
    parser = PlainTextParser()
    parser.feed(message_html)
    return len("".join(parser.parts).encode("utf-16-le")) // 2


def main() -> None:
    token = os.environ.get("TELEGRAM_TOKEN", "").strip()
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN is not configured")

    release_data = json.loads(request(RELEASES_URL).decode("utf-8"))
    tag = release_data.get("tag_name")
    url = release_data.get("html_url")
    body = release_data.get("body") or ""
    if not tag or not url:
        raise RuntimeError("GitHub returned incomplete release metadata")

    markdown_request = json.dumps(
        {"text": body, "mode": "gfm", "context": REPOSITORY},
        ensure_ascii=False,
    ).encode("utf-8")
    rendered_markdown = request(MARKDOWN_URL, data=markdown_request, accept="text/html").decode("utf-8")
    renderer = TelegramHTMLRenderer()
    renderer.feed(rendered_markdown)
    body_html = renderer.render()

    message = (
        f"🚀 <b>Ghost Proxifier {html.escape(tag)} 发布！</b>\n\n"
        f"📋 <b>更新说明：</b>\n{body_html}\n\n"
        f'📥 <b>官方下载：</b>\n<a href="{html.escape(url, quote=True)}">'
        "👉 查看 Release 页面与下载 MSI 安装包</a>"
    )
    if count_telegram_characters(message) > TELEGRAM_TEXT_LIMIT:
        raise RuntimeError(
            "The rendered notification exceeds Telegram's 4096-character limit; "
            "shorten the release notes."
        )

    payload = json.dumps(
        {
            "chat_id": TELEGRAM_CHAT,
            "parse_mode": "HTML",
            "text": message,
            "disable_web_page_preview": False,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        response = json.loads(
            request(telegram_url, data=payload, accept="application/json").decode("utf-8")
        )
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Telegram returned HTTP {error.code}: {details}") from None
    except URLError as error:
        raise RuntimeError(f"Could not reach Telegram: {error.reason}") from None

    if not response.get("ok"):
        raise RuntimeError(f"Telegram rejected the message: {response.get('description', 'unknown error')}")
    print(f"Successfully sent Telegram notification for {tag}.")


if __name__ == "__main__":
    main()

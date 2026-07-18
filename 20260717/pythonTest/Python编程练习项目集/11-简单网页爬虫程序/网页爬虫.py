# -*- coding: utf-8 -*-
"""
简单网页爬虫程序

功能：
- 抓取指定 URL 的网页 HTML 内容
- 提取页面标题
- 提取页面中的所有链接（自动转换为绝对 URL）
- 提取页面中的标题标签（h1-h6）

本程序仅使用 Python 标准库，无需安装第三方包。
"""

import argparse
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from typing import List, Optional, Tuple


class SimpleHTMLParser(HTMLParser):
    """简单的 HTML 解析器，用于提取标题、链接和标题标签。"""

    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.title: Optional[str] = None
        self.links: List[str] = []
        self.headings: List[Tuple[str, str]] = []

        self._in_title = False
        self._title_parts: List[str] = []
        self._current_heading: Optional[str] = None
        self._heading_parts: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attrs_dict = dict(attrs)

        if tag == "title":
            self._in_title = True
            self._title_parts = []

        if tag == "a":
            href = attrs_dict.get("href")
            if href:
                absolute_url = urllib.parse.urljoin(self.base_url, href)
                if absolute_url not in self.links:
                    self.links.append(absolute_url)

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._current_heading = tag
            self._heading_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)
        if self._current_heading:
            self._heading_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.title = "".join(self._title_parts).strip()

        if tag == self._current_heading:
            text = "".join(self._heading_parts).strip()
            self.headings.append((self._current_heading, text))
            self._current_heading = None


def parse_html(html: str, base_url: str = "") -> dict:
    """
    解析 HTML 字符串，提取标题、链接和标题标签。

    :param html: HTML 文本
    :param base_url: 基础 URL，用于将相对链接转为绝对链接
    :return: 包含 title、links、headings 的字典
    """
    parser = SimpleHTMLParser(base_url)
    parser.feed(html)
    return {
        "title": parser.title,
        "links": parser.links,
        "headings": parser.headings,
    }


def fetch_url(
    url: str, timeout: int = 10, user_agent: str = "PythonSimpleCrawler/1.0"
) -> str:
    """
    抓取指定 URL 的页面内容。

    :raises urllib.error.URLError: 网络请求失败时抛出
    """
    request = urllib.request.Request(
        url, headers={"User-Agent": user_agent}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="ignore")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="简单网页爬虫程序")
    parser.add_argument("url", help="目标网页 URL")
    parser.add_argument(
        "--timeout", type=int, default=10, help="请求超时时间（秒）"
    )
    args = parser.parse_args()

    try:
        html = fetch_url(args.url, timeout=args.timeout)
        result = parse_html(html, base_url=args.url)

        print(f"页面标题: {result['title']}")
        print(f"链接数量: {len(result['links'])}")
        print("\n前 20 个链接:")
        for link in result["links"][:20]:
            print(link)

        print("\n页面标题标签:")
        for level, text in result["headings"]:
            print(f"{level}: {text}")
    except urllib.error.URLError as exc:
        print(f"请求失败: {exc}")


if __name__ == "__main__":
    main()
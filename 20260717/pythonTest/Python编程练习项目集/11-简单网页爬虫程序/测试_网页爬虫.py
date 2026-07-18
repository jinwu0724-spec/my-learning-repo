# -*- coding: utf-8 -*-
"""
简单网页爬虫程序单元测试
"""

import unittest

from 网页爬虫 import parse_html


class TestWebCrawler(unittest.TestCase):
    """测试网页解析功能。"""

    def test_parse_title(self):
        html = "<html><head><title>测试页面</title></head><body></body></html>"
        result = parse_html(html)
        self.assertEqual(result["title"], "测试页面")

    def test_parse_headings(self):
        html = "<h1>标题一</h1><h2>标题二</h2>"
        result = parse_html(html)
        self.assertEqual(len(result["headings"]), 2)
        self.assertEqual(result["headings"][0], ("h1", "标题一"))

    def test_parse_links_absolute(self):
        html = '<a href="https://example.com/page">链接</a>'
        result = parse_html(html, base_url="https://example.com")
        self.assertIn("https://example.com/page", result["links"])

    def test_parse_links_relative(self):
        html = '<a href="/about">关于</a>'
        result = parse_html(html, base_url="https://example.com")
        self.assertIn("https://example.com/about", result["links"])


if __name__ == "__main__":
    unittest.main()
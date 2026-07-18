# -*- coding: utf-8 -*-
"""
简易日志分析工具单元测试
"""

import datetime
import unittest

from 日志分析工具 import (
    count_levels,
    filter_by_time,
    parse_line,
    parse_log,
    search_keyword,
)


class TestLogAnalyzer(unittest.TestCase):
    """测试日志分析相关函数。"""

    def setUp(self):
        self.sample_log = """\
[2024-05-20 08:30:00] [INFO] 系统启动成功
[2024-05-20 08:31:15] [WARNING] 磁盘使用率超过 80%
[2024-05-20 08:32:00] [ERROR] 数据库连接超时
[2024-05-20 08:35:42] [INFO] 用户 admin 登录
[2024-05-20 08:36:10] [ERROR] 请求处理失败
"""
        self.entries = parse_log(self.sample_log)

    def test_parse_line_valid(self):
        entry = parse_line("[2024-05-20 08:30:00] [INFO] 系统启动成功")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["level"], "INFO")
        self.assertEqual(entry["message"], "系统启动成功")

    def test_parse_line_invalid(self):
        self.assertIsNone(parse_line("这不是日志"))

    def test_parse_log(self):
        self.assertEqual(len(self.entries), 5)

    def test_count_levels(self):
        counts = count_levels(self.entries)
        self.assertEqual(counts["INFO"], 2)
        self.assertEqual(counts["WARNING"], 1)
        self.assertEqual(counts["ERROR"], 2)

    def test_search_keyword(self):
        results = search_keyword(self.entries, "超时")
        self.assertEqual(len(results), 1)
        self.assertIn("数据库", results[0]["message"])

    def test_filter_by_time(self):
        start = datetime.datetime(2024, 5, 20, 8, 31, 30)
        end = datetime.datetime(2024, 5, 20, 8, 33, 0)
        results = filter_by_time(self.entries, start, end)
        self.assertEqual(len(results), 1)
        self.assertIn("数据库", results[0]["message"])


if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
文件读写操作工具单元测试
"""

import os
import tempfile
import unittest

from 文件读写工具 import (
    append_text_file,
    copy_file,
    count_lines,
    list_directory,
    read_text_file,
    search_text,
    write_text_file,
)


class TestFileIOTool(unittest.TestCase):
    """测试文件读写相关函数。"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = os.path.join(self.temp_dir.name, "测试文件.txt")
        # 在临时目录中创建一个空文件，供 list_directory 测试使用
        write_text_file(self.test_file, "")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_write_and_read(self):
        write_text_file(self.test_file, "你好，世界！")
        content = read_text_file(self.test_file)
        self.assertEqual(content, "你好，世界！")

    def test_append(self):
        write_text_file(self.test_file, "第一行\n")
        append_text_file(self.test_file, "第二行\n")
        content = read_text_file(self.test_file)
        self.assertEqual(content, "第一行\n第二行\n")

    def test_count_lines(self):
        write_text_file(self.test_file, "第一行\n第二行\n第三行\n")
        self.assertEqual(count_lines(self.test_file), 3)

    def test_search_text(self):
        write_text_file(self.test_file, "苹果\n香蕉\n苹果汁\n")
        self.assertEqual(search_text(self.test_file, "苹果"), [1, 3])

    def test_copy_file(self):
        write_text_file(self.test_file, "复制测试")
        destination = os.path.join(self.temp_dir.name, "目标文件.txt")
        copy_file(self.test_file, destination)
        self.assertTrue(os.path.exists(destination))
        self.assertEqual(read_text_file(destination), "复制测试")

    def test_list_directory(self):
        items = list_directory(self.temp_dir.name)
        self.assertIn("测试文件.txt", items)


if __name__ == "__main__":
    unittest.main()
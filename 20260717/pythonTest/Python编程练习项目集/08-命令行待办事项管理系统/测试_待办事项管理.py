# -*- coding: utf-8 -*-
"""
命令行待办事项管理系统单元测试
"""

import os
import tempfile
import unittest

from 待办事项管理 import TodoManager


class TestTodoManager(unittest.TestCase):
    """测试 TodoManager 的核心功能。"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(self.temp_dir.name, "待办数据.json")
        self.manager = TodoManager(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add(self):
        task_id = self.manager.add("学习 Python")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.list()), 1)

    def test_complete(self):
        task_id = self.manager.add("完成作业")
        self.manager.complete(task_id)
        task = self.manager.list()[0]
        self.assertEqual(task.status, "已完成")

    def test_remove(self):
        task_id = self.manager.add("整理房间")
        self.manager.remove(task_id)
        self.assertEqual(len(self.manager.list()), 0)

    def test_list_filter(self):
        self.manager.add("任务 A")
        task_id = self.manager.add("任务 B")
        self.manager.complete(task_id)
        completed = self.manager.list(status="已完成")
        pending = self.manager.list(status="待完成")
        self.assertEqual(len(completed), 1)
        self.assertEqual(len(pending), 1)

    def test_clear(self):
        self.manager.add("任务 1")
        self.manager.add("任务 2")
        self.manager.clear()
        self.assertEqual(len(self.manager.list()), 0)

    def test_persistence(self):
        self.manager.add("持久化测试")
        new_manager = TodoManager(self.data_file)
        self.assertEqual(len(new_manager.list()), 1)


if __name__ == "__main__":
    unittest.main()
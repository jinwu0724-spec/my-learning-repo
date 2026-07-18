# -*- coding: utf-8 -*-
"""
简易通讯录管理系统单元测试
"""

import os
import tempfile
import unittest

from 通讯录管理 import ContactManager


class TestContactManager(unittest.TestCase):
    """测试 ContactManager 的增删改查功能。"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(self.temp_dir.name, "通讯录数据.json")
        self.manager = ContactManager(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_list(self):
        self.manager.add("张三", "13800138000", "zhangsan@example.com")
        contacts = self.manager.list_all()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].name, "张三")

    def test_add_duplicate(self):
        self.manager.add("李四", "13900139000", "lisi@example.com")
        with self.assertRaises(ValueError):
            self.manager.add("李四", "13900139000", "lisi@example.com")

    def test_delete(self):
        self.manager.add("王五", "13700137000", "wangwu@example.com")
        self.manager.delete("王五")
        self.assertEqual(len(self.manager.list_all()), 0)

    def test_update(self):
        self.manager.add("赵六", "13600136000", "zhaoliu@example.com")
        self.manager.update("赵六", phone="13500135000")
        contact = self.manager.list_all()[0]
        self.assertEqual(contact.phone, "13500135000")

    def test_search(self):
        self.manager.add("张三", "13800138000", "zhangsan@example.com")
        self.manager.add("李四", "13900139000", "lisi@example.com")
        results = self.manager.search("zhang")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "张三")

    def test_persistence(self):
        self.manager.add("孙七", "15000150000", "sunqi@example.com")
        # 重新实例化管理器，验证数据已从文件加载
        new_manager = ContactManager(self.data_file)
        self.assertEqual(len(new_manager.list_all()), 1)


if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
学生成绩管理系统单元测试
"""

import csv
import os
import tempfile
import unittest

from 学生成绩管理 import StudentGradeManager


class TestStudentGradeManager(unittest.TestCase):
    """测试 StudentGradeManager 的功能。"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(self.temp_dir.name, "成绩数据.json")
        self.manager = StudentGradeManager(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_list(self):
        self.manager.add_student("2024001", "张三")
        self.assertIn("2024001", self.manager.students)

    def test_add_score(self):
        self.manager.add_student("2024001", "张三")
        self.manager.add_score("2024001", "数学", 90)
        self.assertEqual(self.manager.students["2024001"].scores["数学"], 90)

    def test_invalid_score(self):
        self.manager.add_student("2024001", "张三")
        with self.assertRaises(ValueError):
            self.manager.add_score("2024001", "数学", 101)

    def test_average(self):
        self.manager.add_student("2024001", "张三")
        self.manager.add_score("2024001", "数学", 90)
        self.manager.add_score("2024001", "英语", 80)
        self.assertAlmostEqual(self.manager.get_average("2024001"), 85.0)

    def test_ranking(self):
        self.manager.add_student("2024001", "张三")
        self.manager.add_student("2024002", "李四")
        self.manager.add_score("2024001", "数学", 90)
        self.manager.add_score("2024002", "数学", 95)
        ranking = self.manager.get_ranking()
        self.assertEqual(ranking[0].student_id, "2024002")

    def test_export_csv(self):
        self.manager.add_student("2024001", "张三")
        self.manager.add_score("2024001", "数学", 90)
        csv_path = os.path.join(self.temp_dir.name, "成绩导出.csv")
        self.manager.export_csv(csv_path)
        self.assertTrue(os.path.exists(csv_path))
        with open(csv_path, "r", encoding="utf-8-sig") as file:
            rows = list(csv.reader(file))
        self.assertEqual(len(rows), 2)  # 表头 + 1 条记录


if __name__ == "__main__":
    unittest.main()
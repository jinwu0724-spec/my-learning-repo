# -*- coding: utf-8 -*-
"""
基础计算器单元测试
"""

import unittest

from 基础计算器 import Calculator


class TestCalculator(unittest.TestCase):
    """测试 Calculator 的核心功能。"""

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_evaluate_simple(self):
        self.assertEqual(self.calc.evaluate("1 + 2 * 3"), 7)

    def test_evaluate_with_parentheses(self):
        self.assertEqual(self.calc.evaluate("(1 + 2) * 3"), 9)

    def test_evaluate_power(self):
        self.assertEqual(self.calc.evaluate("2 ** 3"), 8)

    def test_evaluate_unary(self):
        self.assertEqual(self.calc.evaluate("-5 + 3"), -2)

    def test_evaluate_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("1 + * 2")

    def test_evaluate_forbidden_call(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("__import__('os').system('dir')")


if __name__ == "__main__":
    unittest.main()

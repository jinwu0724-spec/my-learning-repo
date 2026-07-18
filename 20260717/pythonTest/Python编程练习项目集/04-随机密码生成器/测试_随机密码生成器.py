# -*- coding: utf-8 -*-
"""
随机密码生成器单元测试
"""

import string
import unittest

from 随机密码生成器 import generate_password


class TestPasswordGenerator(unittest.TestCase):
    """测试 generate_password 函数。"""

    def test_default_length(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_contains_required_categories(self):
        password = generate_password(16)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(
            8, use_upper=False, use_digits=False, use_symbols=False
        )
        self.assertTrue(password.islower())
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0)

    def test_no_category_selected(self):
        with self.assertRaises(ValueError):
            generate_password(
                8,
                use_upper=False,
                use_lower=False,
                use_digits=False,
                use_symbols=False,
            )


if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
单位换算工具单元测试
"""

import unittest

from 单位换算工具 import UnitConverter


class TestUnitConverter(unittest.TestCase):
    """测试 UnitConverter 的换算功能。"""

    def setUp(self):
        self.converter = UnitConverter()

    def test_length_conversion(self):
        result = self.converter.convert("长度", 100, "厘米", "米")
        self.assertAlmostEqual(result, 1.0)

    def test_weight_conversion(self):
        result = self.converter.convert("重量", 1, "千克", "克")
        self.assertAlmostEqual(result, 1000.0)

    def test_temperature_celsius_to_fahrenheit(self):
        result = self.converter.convert("温度", 0, "摄氏度", "华氏度")
        self.assertAlmostEqual(result, 32.0)

    def test_temperature_fahrenheit_to_celsius(self):
        result = self.converter.convert("温度", 32, "华氏度", "摄氏度")
        self.assertAlmostEqual(result, 0.0)

    def test_temperature_celsius_to_kelvin(self):
        result = self.converter.convert("温度", 0, "摄氏度", "开尔文")
        self.assertAlmostEqual(result, 273.15)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            self.converter.convert("面积", 10, "米", "厘米")

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert("长度", 10, "光年", "米")


if __name__ == "__main__":
    unittest.main()
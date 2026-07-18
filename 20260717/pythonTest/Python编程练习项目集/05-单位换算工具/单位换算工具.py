# -*- coding: utf-8 -*-
"""
单位换算工具

功能：
- 长度单位换算（毫米、厘米、米、千米、英寸、英尺）
- 重量单位换算（毫克、克、千克、吨、磅、盎司）
- 温度单位换算（摄氏度、华氏度、开尔文）
"""

from typing import Dict


class UnitConverter:
    """单位换算器。"""

    # 长度：以米为基准的换算系数
    LENGTH_FACTORS: Dict[str, float] = {
        "毫米": 0.001,
        "厘米": 0.01,
        "米": 1.0,
        "千米": 1000.0,
        "英寸": 0.0254,
        "英尺": 0.3048,
    }

    # 重量：以克为基准的换算系数
    WEIGHT_FACTORS: Dict[str, float] = {
        "毫克": 0.001,
        "克": 1.0,
        "千克": 1000.0,
        "吨": 1_000_000.0,
        "磅": 453.59237,
        "盎司": 28.34952,
    }

    SUPPORTED_CATEGORIES = {
        "长度": "LENGTH_FACTORS",
        "重量": "WEIGHT_FACTORS",
        "温度": "temperature",
    }

    def convert(self, category: str, value: float, from_unit: str, to_unit: str) -> float:
        """
        进行单位换算。

        :param category: 换算类别，可选 "长度"、"重量"、"温度"
        :param value: 待换算数值
        :param from_unit: 原始单位
        :param to_unit: 目标单位
        :return: 换算后的数值
        """
        if category not in self.SUPPORTED_CATEGORIES:
            raise ValueError(f"不支持的换算类别: {category}")

        if category == "温度":
            return self._convert_temperature(value, from_unit, to_unit)

        factors = getattr(self, self.SUPPORTED_CATEGORIES[category])
        if from_unit not in factors or to_unit not in factors:
            raise ValueError(f"单位 {from_unit} 或 {to_unit} 不在支持的列表中。")

        base_value = value * factors[from_unit]
        return base_value / factors[to_unit]

    def _convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """温度换算，先统一转换为摄氏度，再转换为目标单位。"""
        if from_unit == to_unit:
            return value

        if from_unit not in {"摄氏度", "华氏度", "开尔文"}:
            raise ValueError(f"不支持的温度单位: {from_unit}")
        if to_unit not in {"摄氏度", "华氏度", "开尔文"}:
            raise ValueError(f"不支持的温度单位: {to_unit}")

        # 先转为摄氏度
        if from_unit == "摄氏度":
            celsius = value
        elif from_unit == "华氏度":
            celsius = (value - 32) * 5 / 9
        else:  # 开尔文
            celsius = value - 273.15

        # 再转为目标单位
        if to_unit == "摄氏度":
            return celsius
        if to_unit == "华氏度":
            return celsius * 9 / 5 + 32
        return celsius + 273.15

    def list_units(self, category: str) -> list:
        """返回指定类别支持的所有单位。"""
        if category == "温度":
            return ["摄氏度", "华氏度", "开尔文"]
        factors = getattr(self, self.SUPPORTED_CATEGORIES[category])
        return list(factors.keys())


def run_interactive() -> None:
    """命令行交互入口。"""
    converter = UnitConverter()
    print("=== 单位换算工具 ===")
    print("支持类别: 长度、重量、温度")
    print("输入示例: 长度 100 厘米 米\n")

    while True:
        try:
            line = input("请输入换算（类别 数值 原单位 目标单位，quit 退出）: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if line.lower() in {"quit", "exit", "q"}:
            print("再见！")
            break

        parts = line.split()
        if len(parts) != 4:
            print("格式错误，请按: 类别 数值 原单位 目标单位")
            continue

        category, value_str, from_unit, to_unit = parts
        try:
            value = float(value_str)
            result = converter.convert(category, value, from_unit, to_unit)
            print(f"结果: {result}")
        except ValueError as exc:
            print(f"错误: {exc}")


if __name__ == "__main__":
    run_interactive()
# -*- coding: utf-8 -*-
"""
基础计算器应用

功能：
- 支持加、减、乘、除四则运算
- 支持括号优先级
- 对输入表达式进行安全解析，避免使用 eval 带来的风险
- 提供命令行交互界面
"""

import ast
import operator
from typing import Union


Number = Union[int, float]


class Calculator:
    """安全的数学表达式计算器。"""

    # 允许参与运算的二元操作符
    _BIN_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
    }

    # 允许参与运算的一元操作符
    _UNARY_OPS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def evaluate(self, expression: str) -> Number:
        """
        解析并计算数学表达式。

        :param expression: 用户输入的数学表达式字符串，例如 "(1 + 2) * 3"
        :return: 计算结果
        :raises ValueError: 表达式非法或包含不允许的语法
        :raises ZeroDivisionError: 除数为零
        """
        if not isinstance(expression, str):
            raise ValueError("表达式必须是字符串类型。")

        try:
            tree = ast.parse(expression.strip(), mode="eval")
        except SyntaxError as exc:
            raise ValueError(f"表达式语法错误: {exc}") from exc

        return self._eval_node(tree.body)

    def _eval_node(self, node: ast.AST) -> Number:
        """递归求值 AST 节点。"""
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"不支持的常量类型: {type(node.value).__name__}")

        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self._BIN_OPS:
                raise ValueError(f"不支持的二元运算符: {op_type.__name__}")
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return self._BIN_OPS[op_type](left, right)

        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self._UNARY_OPS:
                raise ValueError(f"不支持的一元运算符: {op_type.__name__}")
            operand = self._eval_node(node.operand)
            return self._UNARY_OPS[op_type](operand)

        if isinstance(node, ast.Expression):
            return self._eval_node(node.body)

        raise ValueError(f"不支持的表达式节点: {type(node).__name__}")

    def add(self, a: Number, b: Number) -> Number:
        """返回两数之和。"""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """返回两数之差。"""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """返回两数之积。"""
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """返回两数之商，除数不能为零。"""
        if b == 0:
            raise ZeroDivisionError("除数不能为零。")
        return a / b


def run_interactive() -> None:
    """命令行交互入口。"""
    print("=== 基础计算器 ===")
    print("支持的运算: + - * / () 以及幂运算 **")
    print("输入 'quit' 或 'exit' 退出程序。\n")

    calculator = Calculator()
    while True:
        try:
            expression = input("请输入表达式: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if expression.lower() in {"quit", "exit", "q"}:
            print("再见！")
            break

        if not expression:
            continue

        try:
            result = calculator.evaluate(expression)
            print(f"结果: {result}")
        except ZeroDivisionError as exc:
            print(f"错误: {exc}")
        except ValueError as exc:
            print(f"错误: {exc}")


if __name__ == "__main__":
    run_interactive()

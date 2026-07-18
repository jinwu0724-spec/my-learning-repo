# -*- coding: utf-8 -*-
"""
猜数字游戏

游戏规则：
- 程序在指定范围内随机生成一个目标整数
- 玩家每次输入一个猜测，程序给出“偏大”、“偏小”或“猜中”的提示
- 限定最大猜测次数，超过次数则游戏失败
- 提供命令行交互界面
"""

import random
from typing import Optional


class GuessNumberGame:
    """猜数字游戏核心逻辑。"""

    def __init__(self, min_value: int = 1, max_value: int = 100, max_attempts: int = 7):
        """
        初始化游戏。

        :param min_value: 随机数最小值（含）
        :param max_value: 随机数最大值（含）
        :param max_attempts: 最大可猜测次数
        """
        if not isinstance(min_value, int) or not isinstance(max_value, int):
            raise ValueError("最小值和最大值必须是整数。")
        if min_value >= max_value:
            raise ValueError("最小值必须小于最大值。")
        if max_attempts < 1:
            raise ValueError("最大猜测次数必须至少为 1。")

        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.target: Optional[int] = None
        self.attempts: int = 0
        self.finished: bool = False
        self.won: bool = False

    def start(self, seed: Optional[int] = None) -> None:
        """开始新游戏，重置状态并生成目标数字。"""
        if seed is not None:
            random.seed(seed)
        self.target = random.randint(self.min_value, self.max_value)
        self.attempts = 0
        self.finished = False
        self.won = False

    def check_guess(self, guess: int) -> str:
        """
        判断一次猜测结果。

        :param guess: 玩家输入的整数
        :return: "偏大"、"偏小"、"猜中" 或 "游戏已结束"
        :raises ValueError: 猜测值不在有效范围内
        """
        if self.finished:
            return "游戏已结束"
        if self.target is None:
            raise RuntimeError("请先调用 start() 开始游戏。")
        if not isinstance(guess, int):
            raise ValueError("猜测值必须是整数。")
        if guess < self.min_value or guess > self.max_value:
            raise ValueError(
                f"请输入 {self.min_value} 到 {self.max_value} 之间的整数。"
            )

        self.attempts += 1

        if guess == self.target:
            self.finished = True
            self.won = True
            return "猜中"

        if self.attempts >= self.max_attempts:
            self.finished = True
            return "偏大" if guess > self.target else "偏小"

        return "偏大" if guess > self.target else "偏小"

    def remaining_attempts(self) -> int:
        """返回剩余可猜测次数。"""
        return max(0, self.max_attempts - self.attempts)


def run_interactive() -> None:
    """命令行交互入口。"""
    print("=== 猜数字游戏 ===")
    print("我已经想好了一个 1 到 100 之间的整数，你有 7 次机会猜中它。\n")

    game = GuessNumberGame()
    game.start()

    while not game.finished:
        try:
            guess = input(f"第 {game.attempts + 1}/{game.max_attempts} 次猜测: ").strip()
            guess_number = int(guess)
        except ValueError:
            print("请输入有效的整数。")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n游戏已中断。")
            return

        try:
            result = game.check_guess(guess_number)
        except ValueError as exc:
            print(f"输入错误: {exc}")
            continue

        if result == "猜中":
            print(f"恭喜你，猜中了！答案就是 {game.target}，你用了 {game.attempts} 次。")
        elif result == "游戏已结束":
            print(f"很遗憾，次数已用尽。正确答案是 {game.target}。")
        else:
            print(result)

    if game.finished and not game.won:
        print(f"很遗憾，次数已用尽。正确答案是 {game.target}。")


if __name__ == "__main__":
    run_interactive()

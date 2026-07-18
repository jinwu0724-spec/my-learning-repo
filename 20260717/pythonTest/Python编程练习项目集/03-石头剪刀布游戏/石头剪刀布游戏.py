# -*- coding: utf-8 -*-
"""
石头剪刀布游戏

游戏规则：
- 石头胜剪刀，剪刀胜布，布胜石头
- 玩家与电脑对战，电脑随机出拳
- 支持命令行交互
"""

import random
from typing import Optional, Tuple


class RockPaperScissors:
    """石头剪刀布游戏核心逻辑。"""

    CHOICES = ["石头", "剪刀", "布"]

    # 定义获胜组合（玩家选择 -> 电脑选择）
    WINNING_RULES = {
        ("石头", "剪刀"): True,
        ("剪刀", "布"): True,
        ("布", "石头"): True,
    }

    # 别名映射，方便用户输入
    ALIASES = {
        "石头": ["石头", "1", "rock", "stone"],
        "剪刀": ["剪刀", "2", "scissors"],
        "布": ["布", "3", "paper", "cloth"],
    }

    def normalize(self, user_input: str) -> str:
        """
        将用户输入转换为标准出拳名称。

        :raises ValueError: 输入无法识别时抛出
        """
        stripped = user_input.strip().lower()
        for canonical, aliases in self.ALIASES.items():
            if stripped in [a.lower() for a in aliases]:
                return canonical
        raise ValueError(f"无法识别输入: {user_input}")

    def get_computer_choice(self, seed: Optional[int] = None) -> str:
        """随机生成电脑的出拳。"""
        if seed is not None:
            random.seed(seed)
        return random.choice(self.CHOICES)

    def determine_winner(self, player: str, computer: str) -> str:
        """
        根据双方出拳判断胜负。

        :return: "玩家胜"、"电脑胜" 或 "平局"
        """
        if player == computer:
            return "平局"
        if (player, computer) in self.WINNING_RULES:
            return "玩家胜"
        return "电脑胜"

    def play_round(
        self, user_input: str, seed: Optional[int] = None
    ) -> Tuple[str, str, str]:
        """
        进行一局游戏。

        :return: (玩家出拳, 电脑出拳, 胜负结果)
        """
        player = self.normalize(user_input)
        computer = self.get_computer_choice(seed)
        result = self.determine_winner(player, computer)
        return player, computer, result


def run_interactive() -> None:
    """命令行交互入口。"""
    print("=== 石头剪刀布游戏 ===")
    print("请输入: 石头(1)、剪刀(2)、布(3)，或输入 quit 退出。\n")

    game = RockPaperScissors()
    while True:
        try:
            user_input = input("你的出拳: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n游戏结束。")
            break

        if user_input.lower() in {"quit", "exit", "q"}:
            print("游戏结束。")
            break

        try:
            player, computer, result = game.play_round(user_input)
            print(f"你出了: {player}，电脑出了: {computer}，结果: {result}")
        except ValueError as exc:
            print(f"输入错误: {exc}")


if __name__ == "__main__":
    run_interactive()

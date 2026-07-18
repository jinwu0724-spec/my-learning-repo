# -*- coding: utf-8 -*-
"""
石头剪刀布游戏单元测试
"""

import unittest

from 石头剪刀布游戏 import RockPaperScissors


class TestRockPaperScissors(unittest.TestCase):
    """测试 RockPaperScissors 的核心逻辑。"""

    def setUp(self):
        self.game = RockPaperScissors()

    def test_normalize_valid(self):
        self.assertEqual(self.game.normalize("石头"), "石头")
        self.assertEqual(self.game.normalize("1"), "石头")
        self.assertEqual(self.game.normalize("ROCK"), "石头")
        self.assertEqual(self.game.normalize("  布  "), "布")

    def test_normalize_invalid(self):
        with self.assertRaises(ValueError):
            self.game.normalize("手枪")

    def test_determine_winner(self):
        self.assertEqual(self.game.determine_winner("石头", "剪刀"), "玩家胜")
        self.assertEqual(self.game.determine_winner("剪刀", "石头"), "电脑胜")
        self.assertEqual(self.game.determine_winner("布", "布"), "平局")

    def test_play_round(self):
        player, computer, result = self.game.play_round("石头", seed=0)
        self.assertEqual(player, "石头")
        self.assertIn(computer, self.game.CHOICES)
        self.assertIn(result, {"玩家胜", "电脑胜", "平局"})


if __name__ == "__main__":
    unittest.main()
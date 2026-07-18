# -*- coding: utf-8 -*-
"""
猜数字游戏单元测试
"""

import unittest

from 猜数字游戏 import GuessNumberGame


class TestGuessNumberGame(unittest.TestCase):
    """测试 GuessNumberGame 的核心逻辑。"""

    def test_initial_state(self):
        game = GuessNumberGame(1, 10, 5)
        self.assertEqual(game.min_value, 1)
        self.assertEqual(game.max_value, 10)
        self.assertEqual(game.max_attempts, 5)
        self.assertIsNone(game.target)

    def test_start_generates_target(self):
        game = GuessNumberGame(1, 10, 5)
        game.start(seed=42)
        self.assertIsNotNone(game.target)
        self.assertGreaterEqual(game.target, 1)
        self.assertLessEqual(game.target, 10)

    def test_check_guess_correct(self):
        game = GuessNumberGame(1, 10, 5)
        game.start(seed=42)
        # 使用相同种子可复现目标数字
        target = game.target
        result = game.check_guess(target)
        self.assertEqual(result, "猜中")
        self.assertTrue(game.won)
        self.assertTrue(game.finished)

    def test_check_guess_too_high(self):
        game = GuessNumberGame(1, 10, 5)
        game.start(seed=42)
        target = game.target
        result = game.check_guess(target + 1 if target < 10 else target - 1)
        self.assertEqual(result, "偏大")

    def test_check_guess_too_low(self):
        game = GuessNumberGame(1, 10, 5)
        game.start(seed=42)
        target = game.target
        result = game.check_guess(target - 1 if target > 1 else target + 1)
        self.assertEqual(result, "偏小")

    def test_max_attempts(self):
        game = GuessNumberGame(1, 10, 2)
        game.start(seed=42)
        wrong_guess = 11 - game.target if game.target != 11 else 1
        game.check_guess(wrong_guess)
        game.check_guess(wrong_guess)
        self.assertTrue(game.finished)
        self.assertFalse(game.won)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            GuessNumberGame(10, 10)

    def test_out_of_range_guess(self):
        game = GuessNumberGame(1, 10, 5)
        game.start(seed=42)
        with self.assertRaises(ValueError):
            game.check_guess(100)


if __name__ == "__main__":
    unittest.main()

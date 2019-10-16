import unittest
from game import Game
from unittest.mock import patch

class TestMultiplyItems(unittest.TestCase):
    def test_game_first_win(self):
        g = Game()
        user_input = [
            "1", "4", "2", "8", "3"
        ]
        
        with patch('builtins.input', side_effect=user_input):
            res = g.game()
        self.assertEqual(res, "First win")
    def test_game_second_win(self):
        g = Game()
        user_input = [
            "1", "5", "2", "3", "8", "7"
        ]
        
        with patch('builtins.input', side_effect=user_input):
            res = g.game()
        self.assertEqual(res, "Second win")
    def test_game_draw(self):
        g = Game()
        user_input = [
            "1", "5", "2", "3", "7", "4", "6", "9", "8"
        ]
        
        with patch('builtins.input', side_effect=user_input):
            res = g.game()
        self.assertEqual(res, "Draw")
if __name__ == '__main__':
    unittest.main()
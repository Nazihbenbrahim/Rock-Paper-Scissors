import unittest
from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugby


class RockPaperScissorsTest(unittest.TestCase):
    
    def test_player_vs_quincy(self):
        """Player should win at least 60% against Quincy"""
        wins, losses = play(player, quincy, 1000)
        win_rate = wins / 1000
        self.assertGreaterEqual(win_rate, 0.6, 
                               f"Win rate {win_rate} is below 60%")
    
    def test_player_vs_abbey(self):
        """Player should win at least 60% against Abbey"""
        wins, losses = play(player, abbey, 1000)
        win_rate = wins / 1000
        self.assertGreaterEqual(win_rate, 0.6,
                               f"Win rate {win_rate} is below 60%")
    
    def test_player_vs_kris(self):
        """Player should win at least 60% against Kris"""
        wins, losses = play(player, kris, 1000)
        win_rate = wins / 1000
        self.assertGreaterEqual(win_rate, 0.6,
                               f"Win rate {win_rate} is below 60%")
    
    def test_player_vs_mrugby(self):
        """Player should win at least 60% against MrRugby"""
        wins, losses = play(player, mrugby, 1000)
        win_rate = wins / 1000
        self.assertGreaterEqual(win_rate, 0.6,
                               f"Win rate {win_rate} is below 60%")


if __name__ == "__main__":
    unittest.main()

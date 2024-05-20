# test_module.py

import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class TestRPSPlayer(unittest.TestCase):
    def test_against_quincy(self):
        result = play(player, quincy, 1000)
        win_rate = result['player'] / 1000
        self.assertGreaterEqual(win_rate, 0.6, "Player should win at least 60% of the games against Quincy")

    def test_against_abbey(self):
        result = play(player, abbey, 1000)
        win_rate = result['player'] / 1000
        self.assertGreaterEqual(win_rate, 0.6, "Player should win at least 60% of the games against Abbey")

    def test_against_kris(self):
        result = play(player, kris, 1000)
        win_rate = result['player'] / 1000
        self.assertGreaterEqual(win_rate, 0.6, "Player should win at least 60% of the games against Kris")

    def test_against_mrugesh(self):
        result = play(player, mrugesh, 1000)
        win_rate = result['player'] / 1000
        self.assertGreaterEqual(win_rate, 0.6, "Player should win at least 60% of the games against Mrugesh")

if __name__ == "__main__":
    unittest.main()

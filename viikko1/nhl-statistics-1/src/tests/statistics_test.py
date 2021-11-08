import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Parkov", "FLA", 6, 10),
            Player("Aho", "CAR", 44, 53),
            Player("Pietrangelo", "CAR", 22, 30)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_top_scorer_is_correct(self):
        top_scorers = self.statistics.top_scorers(3)
        top_scorer = top_scorers[0]

        self.assertEqual(top_scorer.goals, 44)

    def test_amount_of_top_scorers_is_correct(self):
        top_scorers = self.statistics.top_scorers(2)
        amount = len(top_scorers)

        self.assertEqual(amount, 2)

    def test_search_returns_correct_player(self):
        player = self.statistics.search("Aho")

        self.assertEqual(player, Player("Aho", "CAR", 44, 53))

    def test_search_nonexistent_player_returns_none(self):
        player = self.statistics.search("Test")

        self.assertEqual(player, None)
    
    def test_team_returns_correct_players(self):
        team = self.statistics.team("CAR")
        expected = [
            Player("Aho", "CAR", 44, 53),
            Player("Pietrangelo", "CAR", 22, 30)
        ]

        self.assertEqual(team, expected)

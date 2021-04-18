import unittest
from index import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("James")

    def test_constructor_sets_name_right(self):
#        self.player = Player("James")
        answer = str(self.player)
        self.assertEqual(answer, "Player name is James")

    def test_points_are_added_right(self):
#        self.player = Player("James")
        self.player._add_points(10)
        answer = self.player._show_points()
        self.assertEqual(answer, 10)
import unittest
from tkinter import Frame, Tk
from entities.player import Player
from services.playgame import PlayGame


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


class TestPlayGame(unittest.TestCase):
    def setUp(self):
        root = Tk()
        center_frame = Frame(
            root
        )
        self.game = PlayGame(center_frame)

    def test_generate_game_list(self):
        cards = self.game._generate_game_list(
            self.game._pairs_to_find, self.game._sudden_deaths)
        length_of_cards = len(cards)
        self.assertEqual(length_of_cards, 12)

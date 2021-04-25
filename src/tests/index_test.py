import unittest
from tkinter import Frame, Tk
import random
import string
import os
from repositories.dbutilities import DbUtilities
from entities.player import Player
from services.gameoptions import GameOptions
from services.playgame import PlayGame

class TestDbUtilitlies(unittest.TestCase):
    def setUp(self):
        self.database = DbUtilities()
        self.database.create_player_database()

    def test_file_name_exists(self):
        wanted_answer = os.path.join(".", "data", "playerdatabase.db")
        answer = self.database._file_name
        self.assertEqual(answer, wanted_answer)

class TestPlayer(unittest.TestCase):
    #
    #    def setUp(self):
    #        self.player = Player("James")
    #
    #    def test_constructor_sets_name_right(self):
    #        #        self.player = Player("James")
    #        answer = str(self.player)
    #        self.assertEqual(answer, "Player name is James")
    #
    #    def test_points_are_added_right(self):
    #        #        self.player = Player("James")
    #        self.player._add_points(10)
    #        answer = self.player._show_points()
    #        self.assertEqual(answer, 10)

    def setUp(self):
        self.database = Player()

    def test_check_player_exists_is_false(self):
        #        self.database = Player()
        letters = string.ascii_lowercase
        self.test_name_1 = "".join(random.choice(letters) for i in range(8))

        answer = self.database.check_player_exists(self.test_name_1)
        self.assertEqual(answer, False)

    def test_create_new_player(self):
        #        self.database = Player()
        letters = string.ascii_lowercase
        self.test_name_2 = "".join(random.choice(letters) for i in range(8))
        self.database.create_new_player(self.test_name_2)

        answer = self.database.check_player_exists(self.test_name_2)
        self.assertEqual(answer, True)

#    def test_get_one_player_stats(self):
#        self.database = Player()
#        answer = self.database.get_one_player_stats(self.test_name_2)
#        self.assertEqual(answer, [self.test_name_2, 0, 5, 0])

    def test_update_player_stats(self):
        #        self.database = Player()
        letters = string.ascii_lowercase
        self.test_name_3 = "".join(random.choice(letters) for i in range(8))
        self.database.create_new_player(self.test_name_3)

        new_stats = [self.test_name_3, 1000, 10, 5]
        self.database.update_player_stats(new_stats)

        answer = self.database.get_one_player_stats(self.test_name_3)
        self.assertEqual(answer, new_stats)

class TestGameOptions(unittest.TestCase):
    def setUp(self):
        root = Tk()
        center_frame = Frame(
            root
        )
        self.options = GameOptions(center_frame)

    def test__check_if_name_ok_too_long(self):
        answer = self.options._check_if_name_ok(proposed_name = "billybobtoomuch")
        self.assertEqual(answer, False)

    def test__check_if_name_ok_wrong_characters(self):
        answer = self.options._check_if_name_ok(proposed_name = "!#bill")
        self.assertEqual(answer, False)

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

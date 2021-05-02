import unittest
from tkinter import Frame, Tk
import random
import string
import os

from repositories.playerdbutilities import PlayerDatabaseUtilities
from repositories.katakanadbutilities import KatakanaDatabaseUtilities
from repositories.katakanadatabaseinteraction import KatakanaDatabaseInteraction
from repositories.playerdatabaseinteraction import PlayerDatabaseInteraction
from services.playgame import PlayGame


class TestPlayerDatabaseUtilities(unittest.TestCase):
    def setUp(self):
        self.database = PlayerDatabaseUtilities()
        self.database.initialize_player_db()

    def test_file_name_exists(self):
        wanted_answer = os.path.join(".", "data", "playerdatabase.db")
        answer = self.database._file_name
        self.assertEqual(answer, wanted_answer)


class TestPlayerDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        self.interaction = PlayerDatabaseInteraction()

    def test__get_all_player_names(self):
        player_name_list = self.interaction._get_all_players_names()
        if len(player_name_list) > 0:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_check_player_exists_is_false(self):
        letters = string.ascii_lowercase
        self.test_name_1 = "".join(random.choice(letters) for i in range(8))

        answer = self.interaction._check_player_exists(self.test_name_1)
        self.assertEqual(answer, False)

    def test_create_new_player(self):
        letters = string.ascii_lowercase
        self.test_name_2 = "".join(random.choice(letters) for i in range(8))
        self.interaction._create_new_player(self.test_name_2)
        answer = self.interaction._check_player_exists(self.test_name_2)
        self.assertEqual(answer, True)

    def test_get_one_player_stats(self):
        letters = string.ascii_lowercase
        self.test_name_3 = "".join(random.choice(letters) for i in range(8))
        self.interaction._create_new_player(self.test_name_3)

        answer = self.interaction._get_one_player_stats(self.test_name_3)
        wanted_answer = [self.test_name_3, 0, 5, 0]
        self.assertEqual(answer, wanted_answer)

    def test_get_player_max_level(self):
        letters = string.ascii_lowercase
        self.test_name_4 = "".join(random.choice(letters) for i in range(8))
        self.interaction._create_new_player(self.test_name_4)

        answer = self.interaction._get_player_max_level(self.test_name_4)
        wanted_answer = 0
        self.assertEqual(answer, wanted_answer)

    def test_get_current_game_specs(self):
        sent_specs = self.interaction._get_current_game_specs()
        if len(sent_specs) > 0:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_update_player_stats(self):
        letters = string.ascii_lowercase
        self.test_name_5 = "".join(random.choice(letters) for i in range(8))
        self.interaction._create_new_player(self.test_name_5)

        new_stats = [self.test_name_5, 1000, 10, 5]
        self.interaction._update_player_stats(new_stats)

        answer = self.interaction._get_one_player_stats(self.test_name_5)
        self.assertEqual(answer, new_stats)


class TestKatakanaDatabaseUtilities(unittest.TestCase):
    # Cannot test other capabilities separately.
    def setUp(self):
        self.database = KatakanaDatabaseUtilities()
        self.database.initialize_katakana_db()

        self.interaction = KatakanaDatabaseInteraction()

    def test_file_name_exists(self):
        wanted_answer = os.path.join(".", "data", "katakanadatabase.db")
        answer = self.database._file_name
        self.assertEqual(answer, wanted_answer)

    def test_katakana_database_exists(self):
        self.database._create_katakana_database_table()
        created_katakanas = self.interaction._get_all_katakanas()
        number_of_created_katakanas = len(created_katakanas)
        wanted_answer = 104
        self.assertEqual(number_of_created_katakanas, wanted_answer)


class TestKatakanaDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        self.interaction = KatakanaDatabaseInteraction()

    def test_get_game_specs(self):
        game_specs = self.interaction._get_game_specs(2)
        if len(game_specs) > 0:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_get_all_game_levels(self):
        game_levels = self.interaction._get_all_game_levels()
        answer = max(game_levels)
        wanted_answer = 12
        self.assertEqual(answer, wanted_answer)

    def test_katakana_list(self):
        katakanas_level_1 = self.interaction._get_katakana_list(1)
        answer = len(katakanas_level_1)
        wanted_answer = 8
        self.assertEqual(answer, wanted_answer)

    def test_get_cards_for_game_board(self):
        game_board_level_1 = self.interaction._get_cards_for_game_board(1)
        answer = len(game_board_level_1)
        wanted_answer = 16
        self.assertEqual(answer, wanted_answer)


class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.game = PlayGame()

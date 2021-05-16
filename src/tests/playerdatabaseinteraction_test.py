import unittest
import random
import string
import os
from repositories.playerdbutilities import PlayerDatabaseUtilities
from repositories.playerdatabaseinteraction import PlayerDatabaseInteraction


class TestPlayerDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        self.interaction = PlayerDatabaseInteraction()

    def test_get_all_player_names(self):
        player_name_list = self.interaction.get_all_players_names()
        if len(player_name_list) > 0:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_check_player_exists_is_false(self):
        letters = string.ascii_lowercase
        self.test_name_1 = "".join(random.choice(letters) for i in range(8))

        answer = self.interaction.check_player_exists(self.test_name_1)
        self.assertEqual(answer, False)

    def test_create_new_player(self):
        letters = string.ascii_lowercase
        self.test_name_2 = "".join(random.choice(letters) for i in range(8))
        self.interaction.create_new_player(self.test_name_2)
        answer = self.interaction.check_player_exists(self.test_name_2)
        self.interaction.delete_player(self.test_name_2)
        self.assertEqual(answer, True)

    def test_get_one_player_stats(self):
        letters = string.ascii_lowercase
        self.test_name_3 = "".join(random.choice(letters) for i in range(8))
        self.interaction.create_new_player(self.test_name_3)

        answer = self.interaction.get_one_player_stats(self.test_name_3)
        wanted_answer = [self.test_name_3, 0, 5, 3]
        self.interaction.delete_player(self.test_name_3)
        self.assertEqual(answer, wanted_answer)

    def test__get_player_max_level(self):
        letters = string.ascii_lowercase
        self.test_name_4 = "".join(random.choice(letters) for i in range(8))
        self.interaction.create_new_player(self.test_name_4)

        answer = self.interaction._get_player_max_level(self.test_name_4)
        wanted_answer = 3
        self.interaction.delete_player(self.test_name_4)
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
        self.interaction.create_new_player(self.test_name_5)

        new_stats = [self.test_name_5, 1000, 10, 5]
        self.interaction.update_player_stats(new_stats)

        answer = self.interaction.get_one_player_stats(self.test_name_5)
        self.interaction.delete_player(self.test_name_5)
        self.assertEqual(answer, new_stats)


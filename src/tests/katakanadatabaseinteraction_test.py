import unittest
from repositories.katakanadatabaseinteraction import KatakanaDatabaseInteraction

class TestKatakanaDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        self.interaction = KatakanaDatabaseInteraction()

    def test__get_game_specs(self):
        game_specs = self.interaction._get_game_specs(2)
        if len(game_specs) > 0:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test__get_game_specs_right_cards(self):
        game_specs = self.interaction._get_game_specs(1)
        answer = game_specs[1]
        wanted_answer = 16
        self.assertEqual(answer, wanted_answer)

    def test_get_all_game_levels(self):
        game_levels = self.interaction.get_all_game_levels()
        answer = max(game_levels)
        wanted_answer = 12
        self.assertEqual(answer, wanted_answer)

    def test_katakana_list(self):
        katakanas_level_1 = self.interaction._get_katakana_list(1)
        answer = len(katakanas_level_1)
        wanted_answer = 8
        self.assertEqual(answer, wanted_answer)

    def test_get_cards_for_game_board(self):
        game_board_level_1 = self.interaction.get_cards_for_game_board(1)
        answer = len(game_board_level_1)
        wanted_answer = 16
        self.assertEqual(answer, wanted_answer)

    def test__check_enough_unique_cards(self):
        example_list = []
        pituus1 = len(example_list)
        tested_level = self.interaction._get_game_specs(12)
        returned_list = self.interaction._check_enough_unique_cards(example_list, tested_level)
        pituus2 = len(returned_list)
        answer = ""
        if pituus1 == pituus2:
            answer = False
        elif pituus1 != pituus2:
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

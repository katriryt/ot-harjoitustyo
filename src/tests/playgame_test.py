import unittest
from services.playgame import PlayGame


class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.game = PlayGame()

    def test_pair_found_add_points(self):
        points_at_start = self.game.points
        self.game.pair_found_add_points()
        points_now = self.game.points
        answer = points_now - points_at_start
        wanted_answer = 20
        self.game.points -=20
        final = self.game.points
        self.assertEqual(answer, wanted_answer)

    def test_all_pairs_found_add_points(self):
        points_at_start = self.game.points
        self.game.all_pairs_found_add_points()
        points_now = self.game.points
        difference = points_now - points_at_start
        answer = True
        if difference > 0: 
            answer = False
        wanted_answer = False
        self.game.points = points_at_start
        self.assertEqual(answer, wanted_answer)

    def test_pair_found_add_pairs(self):
        pairs_at_start = self.game.pairs_found
        self.game.pair_found_add_pairs()
        pairs_now = self.game.pairs_found
        answer = ""
        if pairs_at_start != pairs_now:
            answer = False
        else: 
            answer = True
        wanted_answer = False
        self.game.pairs_found -=1
        self.assertEqual(answer, wanted_answer)
    
    def test_death_card_reduce_lives(self):
        lives_at_start = self.game.lives
        self.game.death_card_reduce_lives()
        lives_now = self.game.lives
        difference = lives_now - lives_at_start
        answer = False
        if lives_at_start > lives_now:
            answer = True
        wanted_answer = True
        self.game.lives = lives_at_start
        self.assertEqual(answer, wanted_answer)

    def test_get_card_list(self):
        cards = self.game.get_card_list()
        list_length = len(cards)
        answer = False
        if list_length > 0: 
            answer = True
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_win_update_points(self):
        points_at_start = self.game.points
        original_points_at_start = self.game.original_points
        self.game.pair_found_add_points()
        points_now = self.game.points
        self.game.win_update_points()
        original_points_now = self.game.original_points
        answer = False
        if original_points_now > original_points_at_start:
            answer = True
        wanted_answer = True

        self.game.points = points_at_start
        self.game.original_points = original_points_at_start

        self.assertEqual(answer, wanted_answer)

    def test_win_update_lives_level_high_level(self):
        game_level_at_start = self.game.current_game_level
        lives_at_start = self.game.lives

        self.game.current_game_level = 8
        self.game.win_update_lives()
        lives_now = self.game.lives
        
        lives_gained = lives_now - lives_at_start
        wanted_answer = 4
        
        self.game.current_game_level = game_level_at_start
        self.game.lives = lives_at_start

        self.assertEqual(lives_gained, wanted_answer)

    def test_win_update_highest_level_at_7(self):
        game_level_at_start = self.game.current_game_level
        highest_level_at_start = self.game.player_highest_level

        self.game.current_game_level = 7
        self.game.player_highest_level = 5
        self.game.win_update_highest_level()

        highest_level_now = self.game.player_highest_level
        wanted_answer = 12

        self.game.current_game_level = game_level_at_start
        self.game.player_highest_level = highest_level_at_start

        self.assertEqual(highest_level_now, wanted_answer)

    def test_win_update_highest_level_at_5(self):
        game_level_at_start = self.game.current_game_level
        highest_level_at_start = self.game.player_highest_level

        self.game.current_game_level = 5
        self.game.player_highest_level = 5
        self.game.win_update_highest_level()

        highest_level_now = self.game.player_highest_level
        wanted_answer = 7

        self.game.current_game_level = game_level_at_start
        self.game.player_highest_level = highest_level_at_start

        self.assertEqual(highest_level_now, wanted_answer)

    def test_win_update_highest_level_at_3(self):
        game_level_at_start = self.game.current_game_level
        highest_level_at_start = self.game.player_highest_level

        self.game.current_game_level = 3
        self.game.player_highest_level = 3
        self.game.win_update_highest_level()

        highest_level_now = self.game.player_highest_level
        wanted_answer = 5

        self.game.current_game_level = game_level_at_start
        self.game.player_highest_level = highest_level_at_start

        self.assertEqual(highest_level_now, wanted_answer)

    def test_loss_update_all_points(self):
        points_at_start = self.game.points
        self.game.loss_update_points()
        points_now = self.game.points
        self.game.points = points_at_start

        self.assertEqual(points_now, 0)

    def test_loss_update_lives(self):
        lives_at_start = self.game.lives
        self.game.loss_update_lives()
        lives_now = self.game.lives
        self.game.lives = lives_at_start

        self.assertEqual(lives_now, 1)

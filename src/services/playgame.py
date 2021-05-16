from repositories.playerdatabaseinteraction import PlayerDatabaseInteraction
from repositories.katakanadatabaseinteraction import KatakanaDatabaseInteraction


class PlayGame:
    """This class includes the activities that result from the player
    interacting with the game, e.g. increasing points,
    reducing lives, losing/winning the game, and saving final results
    to the player database.
    """

    def __init__(self):
        """Constructor for the class: sets up connection with the databases,
        and stores the specifications for the game at hand.
        Note: Eleven instance attributes considered relevant for this case.
        """
        self.player_database = PlayerDatabaseInteraction()
        self.katakana_database = KatakanaDatabaseInteraction()

        current_game_specs = self.player_database._get_current_game_specs()
        self.current_game_level = current_game_specs[1]
        self.player_name = current_game_specs[0]

        current_game_details = self.katakana_database._get_game_specs(
            self.current_game_level)
        self.pairs_to_find = current_game_details[3]

        self.pairs_found = 0
        self.sudden_deaths = current_game_details[2]

        current_player_stats = self.player_database.get_one_player_stats(
            self.player_name)
        self.lives = current_player_stats[2]
        self.original_points = current_player_stats[1]
        self.points = 0
        self.player_highest_level = current_player_stats[3]

    def pair_found_add_points(self):
        """Method adds points when a pair is found for the point counter in the level.
        """
        self.points += 20

    def pair_found_add_pairs(self):
        """When a pair is found, method adds one to the counter of the found pairs.
        """
        self.pairs_found += 1

    def all_pairs_found_add_points(self):
        """When all pairs are found, method adds additional points to the point
        counter in the level.
        """
        self.points += self.pairs_to_find*2*20

    def death_card_reduce_lives(self):
        """When a death card is opened, method reduces a life from the lives
        counter.
        """
        self.lives -= 1

    def get_card_list(self):
        """Method calls for the katakana database to generate a card list for the game
        in this level.

        Returns:
            list: Method returns a list ready to be used in the game.
        """

        new_cards = self.katakana_database.get_cards_for_game_board(
            self.current_game_level)

        return new_cards

    def win_update_all_stats(self):
        """When the player wins the game, method calls other methods to update all
        counters in the game, as well as it calls to update the players' statistics
        in the database.
        """
        self.win_update_points()
        self.win_update_lives()
        self.win_update_highest_level()
        self.update_stats_in_database()

    def win_update_points(self):
        """ When the player wins the game, points collected in this game are added
        to the players' original points at the beginning of the level.
        """
        self.original_points += self.points

    def win_update_lives(self):
        """ When the player wins the game, the player gains new lives depending on
        the difficulty level of the game. Method adds the gained lives to the
        players' lives counter.
        """
        if self.current_game_level >= 0 and self.current_game_level <= 5:
            self.lives += 1
        elif self.current_game_level >= 6 and self.current_game_level <= 7:
            self.lives += 2
        elif self.current_game_level >= 8 and self.current_game_level <= 12:
            self.lives += 4

    def win_update_highest_level(self):
        """ When the player wins the game, the player gains access to new levels
        depending on the difficulty level of the game solved. Method updates players'
        highest level counter.
        """
        if self.current_game_level == 7:
            if self.player_highest_level < 12:
                self.player_highest_level = 12
        elif self.current_game_level == 5:
            if self.player_highest_level < 7:
                self.player_highest_level = 7
        elif self.current_game_level == 3:
            if self.player_highest_level < 5:
                self.player_highest_level = 5

    def loss_update_all_stats(self):
        """ When the player loses a game, this method calls other methods to update all
        relevant counters in the game, as well as it calls to update the players' statistics
        in the database.
        """
        self.loss_update_points()
        self.loss_update_lives()
        self.update_stats_in_database()

    def loss_update_points(self):
        """ When the player loses a game, the player loses all the points gained in this level.
        No new points are added to the player's statistics in the database. Method updates the
        counter for the points in the level.
        """
        self.points = 0

    def loss_update_lives(self):
        """ When the player loses a game (i.e. all lives are spent), to be able to continue
        in other levels, one additional life is given for the player. Method updates
        the lives counter.
        """
        self.lives = 1

    def update_stats_in_database(self):
        """ When the player wins / loses a game, all the updated statistics are updated
        to the player's files in the database.
        """
        new_stats = [self.player_name,
                     self.original_points,
                     self.lives,
                     self.player_highest_level]
        self.player_database.update_player_stats(new_stats)

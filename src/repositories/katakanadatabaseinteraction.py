import random
from repositories.katakanadbutilities import KatakanaDatabaseUtilities


class KatakanaDatabaseInteraction():
    """Purpose of this class is to handle all the interactions with the Katakana database.
    Methods in this class include e.g. getting list of katakanas for the game as well as
    specifications for the game difficulty level selected.
    Class acts as a link between the database and the UI, services, and entities.
    """

    def __init__(self):
        """Constructor for the class.
        """
        self._katakana_database = KatakanaDatabaseUtilities()

    def _get_game_specs(self, level):
        """Method returns specs for a particular game level as a tuple: (Game level,
        number of cards, number of death cards, and number of unique cards series).
        """

        self._katakana_database._create_katakana_database_connection()

        given_level = int(level)

        raw_game_specs = self._katakana_database._katakana_db.execute(
            """SELECT * FROM Games WHERE game_level = ?""", [given_level]).fetchone()

        return raw_game_specs

    def _get_all_game_levels(self):
        """Methods returns a list of games for all the game levels.
        """

        self._katakana_database._create_katakana_database_connection()

        raw_game_levels = self._katakana_database._katakana_db.execute(
            """SELECT game_level FROM Games""").fetchall()

        all_game_levels = []
        for i in raw_game_levels:
            all_game_levels.append(i[0])
        return all_game_levels

    def _get_katakana_list(self, level):
        """ Method gets from the database and returns to the customer
        a list of the katakanas for the given level.
        """
        self._katakana_database._create_katakana_database_connection()

        given_level = int(level)

        katakanas_in_level = self._katakana_database._katakana_db.execute(
            """SELECT
                        roomaji,
                        katakana,
                        difficulty_level
                    FROM Katakanas
                    WHERE difficulty_level = ?""", [given_level]).fetchall()

        return katakanas_in_level

    def _get_cards_for_game_board(self, level: int):
        """Method generates a shuffled deck of katakana-cards to be printed
        to the game board.

        Args:
            level (int): Cards are selected based on the game level given.

        Returns:
            list: Method returns a list of the right katakana cards and,
            if releant for the level, also the right number of sudden death cards.
        """
        self._katakana_database._create_katakana_database_connection()

        given_level = int(level)
        game_specs = self._get_game_specs(given_level)
        katakanas_for_game = self._get_katakana_list(given_level)

        raw_game_board = []
        for i in katakanas_for_game:
            raw_game_board.append((i[0], i[1]))

        checked_raw_game_board = self._check_enough_unique_cards(
            raw_game_board, game_specs)

        game_board = checked_raw_game_board*2
        sudden_deaths_in_game = game_specs[2]

        for i in range(sudden_deaths_in_game):
            game_board.append(("", "Sudden Death"))

        random.shuffle(game_board)

        return game_board

    def _check_enough_unique_cards(self, raw_game_board: list, game_specs: list):
        """Method checks whether there are enough cards selected for the game.
        If there is, nothing is done. If there is not, cards are either added or
        removed.
        Args:
            raw_game_board (list): List of katakanas generated based on database difficulty levels.
            game_specs (list): List of specifications for the game based on specs in database.

        Returns:
            List: Given raw_game_board is appended with additional katakanas (if needed)
            or reduced (if there were too many katakanas in the start).
        """
        self._katakana_database._create_katakana_database_connection()

        if len(raw_game_board) == game_specs[3]:
            pass

        elif len(raw_game_board) < game_specs[3]:
            additional_cards = self._get_all_katakanas()
            needed_unique_cards = game_specs[3]-len(raw_game_board)

            for i in range(needed_unique_cards):
                random.shuffle(additional_cards)
                raw_game_board.append(
                    (additional_cards[i][0], additional_cards[i][1]))

        elif len(raw_game_board) < game_specs[3]:
            cards_to_be_removed = len(raw_game_board) - game_specs[3]
            random.shuffle(raw_game_board)
            for i in range(cards_to_be_removed):
                raw_game_board.pop()

        return raw_game_board

    def _get_all_katakanas(self):
        """ Method generates and returns a list of all of the katakana characters as a list.
        List consists of tuples with the roomaji and katakana characters and their
        difficulty levels.
        """
        self._katakana_database._create_katakana_database_connection()

        all_katakanas = self._katakana_database._katakana_db.execute(
            """SELECT
                    roomaji,
                    katakana,
                    difficulty_level
                FROM Katakanas""").fetchall()

        return all_katakanas

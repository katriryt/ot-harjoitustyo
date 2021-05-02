from repositories.playerdbutilities import PlayerDatabaseUtilities


class PlayerDatabaseInteraction():
    """Purpose of this class is the handle all the interactions with the Player Database.

    Returns:
        String: Depending on the method, class returns e.g. lists of player names, or
        Boolean values (True/False) on whether a particular player exists.
    """

    def __init__(self):
        """Constructor for the class.
        """
        self._player_database = PlayerDatabaseUtilities()

    def _get_all_players_names(self):
        """Method retrieves all the player names from the Player database.

        Returns:
            List: Method returns a list of names in the database.
        """
        self._player_database._create_player_database_connection()

        all_players_names = self._player_database._player_db.execute(
            """SELECT name FROM Players""").fetchall()

        answer_list = []
        for i in all_players_names:
            answer_list.append(i[0])

        return answer_list

    def _check_player_exists(self, given_name):
        """Method checks whether the player of the given name exists

        Args:
            given_name (string): Method requires a name in string format
            to be searched from the database.

        Returns:
            Boolean: Method returns True, if a player with the given name
            is already in the database, and False, if not.
        """
        self._player_database._create_player_database_connection()

        current_names = self._get_all_players_names()

        if given_name not in current_names:
            return False

        else:
            return True

    def _create_new_player(self, given_name):
        """Method creates a new player to the database of the given name.
        Also basic data (e.g. number of lives available) is added to the database.
        """
        self._player_database._create_player_database_connection()

        self._player_database._player_db.execute("""INSERT INTO
            Players (name, points, lives, maxlevel)
            VALUES(?, 0, 5, 0)""", [given_name])

    def _get_one_player_stats(self, given_name):
        """Method retrieves from the database statistics (e.g. number of lives)
        for the player with the given name. Data is returned as a list.
        If the player does not exist, response None is returned.
        """
        self._player_database._create_player_database_connection()

        player_stats = []

        if self._check_player_exists(given_name) is True:
            answer = self._player_database._player_db.execute("""SELECT *
                                    FROM Players
                                    WHERE name = ?""", [given_name]).fetchone()

            for i in range(1, len(answer)):
                player_stats.append(answer[i])

            return player_stats

        else:
            return None

    def _get_player_max_level(self, given_name):
        """Method retrieves and returns from the database maximum level
        that the player has reached so far.

        Args:
            given_name (string): Method requires a name in string format
            to be searched from the database

        Returns:
            integer: Method returns a number for the current level
        """
        self._player_database._create_player_database_connection()
        player_all_stats = self._get_one_player_stats(given_name)

        return player_all_stats[3]

    def _get_current_game_specs(self):
        """Method retrieves and returns from the database specifications
        for the current game.

        Returns:
            tuple: Method returns a tuple with the name of the player
            and the chosen level to be played in the game.
        """

        self._player_database._create_player_database_connection()
        raw_answer = self._player_database._player_db.execute("""SELECT *
                                    FROM Current_game""").fetchone()

        answer = (raw_answer[1], raw_answer[2])

        return answer

    def _update_current_game_specs(self, new_specs):
        """Method updates specs of the currect game to the database.
        New specifications to be updated are given as a tuple.
        """
        self._player_database._create_player_database_connection()

        self._player_database._player_db.execute("""UPDATE Current_game
                        SET player = ?,
                            current_active_level = ?""",
                                                 [new_specs[0], new_specs[1]])

    def _update_player_stats(self, new_stats):
        """Method updates all player stats at once, if the player exists.
        """
        self._player_database._create_player_database_connection()

        given_name = new_stats[0]

        if self._check_player_exists(given_name) is True:
            new_points = new_stats[1]

            current_stats = self._get_one_player_stats(given_name)

            if new_stats[2] < 0:
                new_lives = 0
            else:
                new_lives = new_stats[2]

            new_max_level = max(new_stats[3], current_stats[3])

        self._player_database._player_db.execute("""UPDATE Players
                        SET points = ?,
                            lives = ?,
                            maxlevel = ?
                        WHERE name = ?
                        """, [new_points, new_lives, new_max_level, given_name])

    def _set_default_player_data(self):
        """ Method sets default player's data on its original level.
        """
        self._player_database._create_player_database_connection()

        default_player_name = "NoName"
        if self._check_player_exists(default_player_name) is True:
            self._player_database._player_db.execute("""UPDATE Players
                        SET points = 0,
                            lives = 5,
                            maxlevel = 1
                        WHERE name = ?""", [default_player_name])

        else:
            self._player_database._player_db.execute(
                """INSERT INTO Players (name, points, lives, maxlevel)
                VALUES("NoName", 0, 5, 1)""")

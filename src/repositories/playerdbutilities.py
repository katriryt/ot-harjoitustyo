import os
import sqlite3


class PlayerDatabaseUtilities():
    """Purpose of this class is to set up connection with the player
    database, create the necessary tables, and set data to start the game.
    Idea is to use operations in this class once when the game is first established,
    with the exception of creating database connection.
    """

    def __init__(self):
        """ Constructor for the class.
        """

        text = os.path.join(".", "data", "playerdatabase.db")
        self._file_name = text
        self.player_db = ""

    def initialize_player_db(self):
        """Method calls other methods in class to create the necessary
        databases, tables and data at the beginning of the game for the Player database.
        """

        self.create_player_database_connection()
        self._create_player_database_table()
        self._create_current_game_database_table()

    def create_player_database_connection(self):
        """Method sets up connection with the Player database.
        """

        self.player_db = sqlite3.connect(self._file_name)
        self.player_db.isolation_level = None

    def _create_player_database_table(self):
        """Method creates table Player for the database,
        if it has not yet been created.
        """

        raw_existing_databases = self.player_db.execute("""SELECT *
                                            FROM sqlite_master
                                            WHERE type = "table" """).fetchall()

        existing_databases = []
        for i in raw_existing_databases:
            existing_databases.append(i[1])

        if (len(existing_databases)) == 0 or ("Players" not in existing_databases):
            self.player_db.execute("""CREATE TABLE Players(
                id INTEGER PRIMARY KEY,
                name TEXT,
                points INTEGER,
                lives INTEGER,
                maxlevel INTEGER)""")

            self._set_first_player_data()

    def _set_first_player_data(self):
        """Method adds a default player to the database.
        """
        self.player_db.execute(
            """INSERT INTO Players
                            (name,
                            points,
                            lives,
                            maxlevel)
                VALUES("NoName", 0, 5, 3)""")

    def _create_current_game_database_table(self):
        """Method creates a database table that stores key data
        for the current game being played.
        """

        raw_existing_databases = self.player_db.execute("""SELECT *
                                            FROM sqlite_master
                                            WHERE type = "table" """).fetchall()

        existing_databases = []
        for i in raw_existing_databases:
            existing_databases.append(i[1])

        if (len(existing_databases)) == 0 or ("Current_game" not in existing_databases):
            self.player_db.execute("""CREATE TABLE Current_game(
                id INTEGER PRIMARY KEY,
                player TEXT,
                current_active_level INTEGER)""")

            self._set_default_game_data()

    def _set_default_game_data(self):
        """Method sets up a default game to start the game.
        """
        self.player_db.execute(
            """INSERT INTO Current_game
                (player,
                current_active_level)
                VALUES("NoName", 1)""")

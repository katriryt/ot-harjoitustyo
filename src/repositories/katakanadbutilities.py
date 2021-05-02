import sqlite3
import os


class KatakanaDatabaseUtilities():
    """Purpose of this class is to set-up connection with the katakana
    database and fill it with the katakanas and options for the different game levels.
    Idea is to use operations in this class once when the game is first established.
    """

    def __init__(self):
        """Constructor for the class.
        """
        text = os.path.join(".", "data", "katakanadatabase.db")
        self._file_name = text

    def initialize_katakana_db(self):
        """Method calls other methods in class to create the necessary
        databases, tables and data at the beginning of the game
        for the Katakana database.
        """
        self._create_katakana_database_connection()
        self._create_katakana_database_table()
        self._create_games_database_table()

    def _create_katakana_database_connection(self):
        """Method sets up connection with the Katakana database.
        """
        self._katakana_db = sqlite3.connect(self._file_name)
        self._katakana_db.isolation_level = None

    def _create_katakana_database_table(self):
        """Method creates a empty table Katakanas for katakanas in the Katakana
        database, if the table does not yet exist.
        """
        self._create_katakana_database_connection()

        raw_existing_databases = self._katakana_db.execute("""SELECT name
                                            FROM sqlite_master
                                            WHERE type = "table" """).fetchall()

        existing_databases = []

        for i in raw_existing_databases:
            existing_databases.append(i[0])

        if (len(existing_databases) == 0) or ("Katakanas" not in existing_databases):
            self._katakana_db.execute("""CREATE TABLE Katakanas(
                id INTEGER PRIMARY KEY,
                roomaji TEXT,
                katakana TEXT,
                series TEXT,
                difficulty_level INTEGER)"""
                                      )

            self._create_katakana_baseline_data()

    def _create_katakana_baseline_data(self):
        """Method fills in the Katakana table in the Katakana Database
        when the table is created for the first time.
        Note. This function is only called in the first time, when the database
        is created and it is filled with original raw katakana data.
        """
        text = os.path.join(".", "data", "katakanas.csv")
        with open(text) as katakana_baseline_file:
            raw_katakana_data = katakana_baseline_file.readlines()

        for i in range(1, len(raw_katakana_data)):
            line = raw_katakana_data[i]
            line = line.strip()
            line = line.split(',')

            self._katakana_db.execute("""INSERT INTO Katakanas
                                            (roomaji,
                                            katakana,
                                            series,
                                            difficulty_level)
                                            VALUES(?, ?, ?, ?)
                                            """, [line[0], line[1], line[2], line[3]])

    def _create_games_database_table(self):
        """At the beginning of the game, a table Games is created, if it does not exist.
        This operation is done only once at the beginning of the game.
        """
        self._create_katakana_database_connection()

        raw_existing_databases = self._katakana_db.execute("""SELECT *
                                            FROM sqlite_master
                                            WHERE type = "table" """).fetchall()

        existing_databases = []
        for i in raw_existing_databases:
            existing_databases.append(i[1])

        if (len(existing_databases) == 0) or ("Games" not in existing_databases):
            self._katakana_db.execute("""CREATE TABLE Games(
                game_level INTEGER PRIMARY KEY,
                number_of_cards INTEGER,
                number_of_deaths INTEGER,
                number_of_unique_cards INTEGER)"""
                                      )

            self._create_games_baseline_data()

    def _create_games_baseline_data(self):
        """Method fills in the Games table in the Katakana database at the beginning of the game.
        Source for the data is a separate csv file.
        """
        text = os.path.join(".", "data", "games.csv")
        with open(text) as games_baseline_file:
            raw_games_data = games_baseline_file.readlines()

        self._create_katakana_database_connection()

        for i in range(1, len(raw_games_data)):
            line = raw_games_data[i]
            line = line.strip()
            line = line.split(',')

            self._katakana_db.execute("""INSERT
                                            INTO Games
                                            (game_level,
                                            number_of_cards,
                                            number_of_deaths,
                                            number_of_unique_cards)
                                            VALUES(?, ?, ?, ?)
                                            """, [line[0], line[1], line[2], line[3]])

import os
import sqlite3


class DbUtilities:
    def __init__(self):
        text = os.path.join(".", "data", "playerdatabase.db")
        self._file_name = text

#    def create_player_database(self, file_name):
    def create_player_database(self):
        # refactor: make separate filename and table check functions

        #    file_name = "playerdatabase.db"
        #    file_name = database_name

        #        if os.path.exists(self._file_name):
        #            os.remove(self._file_name)
        #        else:
        #            print("The file does not exist")

        db = sqlite3.connect(self._file_name)
    #    db = sqlite3.connect(database_name)
        db.isolation_level = None

        existing_databases = db.execute("""SELECT *
                                            FROM sqlite_master
                                            WHERE type = "table" """).fetchall()

#        print(existing_databases)
#        print(existing_databases[0][1])

        if (len(existing_databases) == 0) or (existing_databases[0][1] != "Players"):
            db.execute("""CREATE TABLE Players(
                id INTEGER PRIMARY KEY,
                name TEXT,
                points INTEGER,
                lives INTEGER,
                maxlevel INTEGER)""")

            db.execute(
                """INSERT INTO Players (name, points, lives, maxlevel) VALUES("NoName", 600, 5, 2)""")
        else:
            #            print("database already exists")
            pass

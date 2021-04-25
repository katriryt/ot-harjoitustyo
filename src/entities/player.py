# Luodaan tietokanta, johon voidaan lisätä tyyppejä ja hakea tietoa

import sqlite3
import os

class Player:
    def __init__(self):
        text = os.path.join(".", "data", "playerdatabase.db")
        # note! this path, when run from command line with poetry run invoke start in the project root directory
        self._file_name = text

    def get_all_players_names(self):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None  # unclear if needed

        all_players_names = db.execute(
            """SELECT name FROM Players""").fetchall()

        answer_list = []

        for i in all_players_names:
            answer_list.append(i[0])

        return answer_list

    def check_player_exists(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

        current_names = (self.get_all_players_names())
#        current_names = (self.get_all_players_names("playerdatabase.db"))
    #    print(current_names)

        if given_name not in current_names:
            #        print("name not in list")
            return False

        else:
            #        pass
            return True

    def create_new_player(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

    #    exists = check_player_exists("playerdatabase.db", "NoName")

    #    if exists == True:

#        print("create new player, no checks done")
        db.execute("""INSERT INTO
            Players (name, points, lives, maxlevel)
            VALUES(?, 0, 5, 0)""", [given_name])

#        if self.check_player_exists(given_name) == False:
#            print("create new player")
#            db.execute("""INSERT INTO
#                Players (name, points, lives, maxlevel)
#                VALUES(?, 600, 5, 0)""", [given_name]) # some checks here?
#
#    #    if check_player_exists(file_name, given_name) == True:
#        else:
#            print("player exists, does not create new player")
#    #        pass

    def get_one_player_stats(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

        player_stats = []

        if self.check_player_exists(given_name) == True:
            #        print("can get stats")
            answer = db.execute("""SELECT *
                                    FROM Players
                                    WHERE name = ?""", [given_name]).fetchone()

        #    print(answer)
        #    print(len(answer))

            for i in range(1, len(answer)):
                player_stats.append(answer[i])

    #        print(player_stats)
            return player_stats

        else:
            #        print("no stats to get")
            return None

    def get_one_player_points(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

        if self.check_player_exists(given_name) == True:
            #        print("can get points")

            answer = db.execute("""SELECT points
                                    FROM Players
                                    WHERE name = ?""", [given_name]).fetchone()

        return answer[0]

    def get_one_player_lives(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

        if self.check_player_exists(given_name) == True:
            #        print("can get lives")

            answer = db.execute("""SELECT lives
                                    FROM Players
                                    WHERE name = ?""", [given_name]).fetchone()

        return answer[0]

    def get_one_player_maxlevel(self, given_name):
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

        if self.check_player_exists(given_name) == True:
            #        print("can get maxlevel")

            answer = db.execute("""SELECT maxlevel
                                    FROM Players
                                    WHERE name = ?""", [given_name]).fetchone()

        return answer[0]

    def update_player_stats(self, new_stats):
        # updates all player stats at once. Probably need to cahnge this, adding checks etc.
        db = sqlite3.connect(self._file_name)
        db.isolation_level = None

    #    print(new_stats)
        given_name = new_stats[0]
    #    stats_to_database = []

        if self.check_player_exists(given_name) == True:
            #        print("can update stats")
            new_points = new_stats[1]

    #        stats_to_database.append(given_name)
    #        stats_to_database.append(new_stats[1])

            current_stats = self.get_one_player_stats(given_name)
    #        print(current_stats)
            if new_stats[2] < 0:
                # check that lives are ok. see later, if need this as a separate function!
                # stats_to_database.append(0)
                new_lives = 0
            else:
                #           stats_to_database.append(new_stats[2])
                new_lives = new_stats[2]
            new_max_level = new_stats[3]
            print(given_name, new_points, new_lives, new_max_level)

        db.execute("""UPDATE Players
                        SET points = ?,
                            lives = ?,
                            maxlevel = ?
                        WHERE name = ?""",
                   [new_points, new_lives, new_max_level, given_name])

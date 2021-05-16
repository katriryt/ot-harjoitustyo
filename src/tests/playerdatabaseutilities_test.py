import unittest
import os
from repositories.playerdbutilities import PlayerDatabaseUtilities


class TestPlayerDatabaseUtilities(unittest.TestCase):
    def setUp(self):
        self.database = PlayerDatabaseUtilities()
        self.database.initialize_player_db()

    def test_file_name_exists(self):
        wanted_answer = os.path.join(".", "data", "playerdatabase.db")
        answer = self.database._file_name
        self.assertEqual(answer, wanted_answer)
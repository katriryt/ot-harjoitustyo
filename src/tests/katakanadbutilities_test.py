import unittest
import os
from repositories.katakanadbutilities import KatakanaDatabaseUtilities


class TestKatakanaDatabaseUtilities(unittest.TestCase):
    def setUp(self):
        self.database = KatakanaDatabaseUtilities()
        self.database.initialize_katakana_db()

    def test_file_name_exists(self):
        wanted_answer = os.path.join(".", "data", "katakanadatabase.db")
        answer = self.database._file_name
        self.assertEqual(answer, wanted_answer)

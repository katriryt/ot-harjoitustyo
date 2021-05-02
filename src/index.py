from tkinter import Tk
from ui.ui import UI
from repositories.playerdbutilities import PlayerDatabaseUtilities
from repositories.katakanadbutilities import KatakanaDatabaseUtilities


class Main:
    """Purpose of the class is to initialize key databases and start the game.
    It also initializes the basic settings for the game window (change is not allowed).
    """
    new_player_database = PlayerDatabaseUtilities()
    new_player_database.initialize_player_db()

    katakana_database = KatakanaDatabaseUtilities()
    katakana_database.initialize_katakana_db()

    window = Tk()

    window.title("Katakana no geemu - Sudden death")
    window_height = 600
    window_width = 1000

    window.geometry("{}x{}".format(window_width, window_height))
    window.resizable(False, False)

    ui = UI(window, window_width, window_height)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    game = Main()

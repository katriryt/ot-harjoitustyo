from tkinter import Tk
from ui.ui import UI


# Basic setting for the window: title, size and ability to change (not allowed)
class Main:
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

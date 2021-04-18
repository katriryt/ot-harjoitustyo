#from tkinter import *
#from PIL import Image, ImageTk
#from functools import partial
#import random

from services.playgame import PlayGame


class GameView():
    def __init__(self, root):
        self._root = root

        self._initialize()

    def destroy(self):
        self._root.destroy()

    def _initialize(self):

        #        self._root.grid_rowconfigure([0, 1, 2, 3, 4], minsize = 100) # how many rows
        #        self._root.grid_columnconfigure([0, 1, 2, 3, 4], minsize = 50) # how many columns

        #        self._set_up_game_board()
        PlayGame(self._root)

#from tkinter import *
#from tkinter import Label
from services.gameoptions import GameOptions


class OptionsView():
    def __init__(self, root):
        self._root = root
        self._initialize()

    def destroy(self):
        self._root.destroy()

    def _initialize(self):
        #        print("alustaa options-sivua")
        #        self._root.configure(bg="blue")
        GameOptions(self._root)

#
#        self._root.grid_rowconfigure([0, 1, 2, 3], minsize=100)
#        self._root.grid_columnconfigure([0, 1, 2, 3], minsize=100)
#
#        label1 = Label(
#            self._root,
#            text="Welcome to options: Choose your player name, team, and game level"
#        )
#
#        label1.grid(
#            row=0,
#            column=0
#        )
#

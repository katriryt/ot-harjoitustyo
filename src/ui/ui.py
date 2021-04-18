#from tkinter import *
#from PIL import Image, ImageTk
#from functools import partial
#import random
from tkinter import Frame, Button
from ui.openingview import OpeningView
from ui.introview import IntroView
from ui.optionsview import OptionsView
from ui.gameview import GameView

class UI:
    def __init__(self, root, input_width, input_height):
        # Sets window as the main object and current view as None.
        self._root = root
        self._root_width = input_width
        self._root_height = input_height
        self._bottom_height = 50

        self._current_view = None

    def start(self):
        self._root.grid_rowconfigure(0, weight=1)
        # remember to configure the same from the start
        self._root.grid_columnconfigure(0, weight=1)

        center_frame = Frame(
            self._root,
            bg = "cyan",
            width = self._root_width,
            heigh = self._root_height - self._bottom_height,
        )

        bottom_frame = Frame(
            self._root,
            bg = "black",
            width = self._root_width,
            height = self._bottom_height,
        )

        self._root.grid_rowconfigure(2)
        self._root.grid_columnconfigure(1)

        center_frame.grid(
            row = 0,
            column = 0,
            sticky = "nsew"
        )

        bottom_frame.grid(
            row = 1,
            column = 0,
            sticky = "nsew"
        )

        # bottom frame configure
        bottom_frame.grid_rowconfigure(1)
        bottom_frame.grid_columnconfigure([0, 1, 2, 3, 4, 5, 6, 7] , minsize = (self._root_width/8))

        bottom_frame_headlines = ["Intro", "Options", "Start", "Exit"]
        commands = [lambda: self._show_intro_view(center_frame),
                    lambda: self._show_options_view(center_frame),
                    lambda: self._show_game_view(center_frame),
                    self._quit]

        for j in range(0, len(bottom_frame_headlines)):
            button = Button(
                bottom_frame,
                text = bottom_frame_headlines[j],
                compound = "center",#CENTER
                width = 12,
                height = 1,
                background = "orange",
                activebackground = "red",
#                command = self._quit
#                command = lambda: self._show_game_view(center_frame),
                command = commands[j]
            )

            button.grid(
                row = 0,
                column = j,
                padx = 12,
                pady = 12
            )

        self._show_opening_view(center_frame)

    def _show_opening_view(self, screen):
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = OpeningView(
            screen
        )

    def _show_intro_view(self, screen):
        for widget in screen.winfo_children():
        # removes widgets from e.g. frame without actually destroying the frame
            widget.destroy()
        self._current_view = IntroView(
            screen
        )

    def _show_options_view(self, screen):
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = OptionsView(
            screen
        )

    def _show_game_view(self, screen):
        #self._hide_current_view()
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = GameView(
            screen
        )

    def _hide_current_view(self):
    # removes current view
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _quit(self):
        self._root.destroy()

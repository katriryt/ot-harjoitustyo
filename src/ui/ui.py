from tkinter import Frame, Button
from ui.openingview import OpeningView
from ui.introview import IntroView
from ui.optionsview import OptionsView
from ui.gameview import GameView


class UI:
    """Purpose of the class is to set the common UI specifications
    and elements across all of the views.
    """

    def __init__(self, root, input_width, input_height):
        """Constructor for the class. Sets window given by the
        index.py as the baseline view for the game.
        """
        self._root = root
        self._root_width = input_width
        self._root_height = input_height
        self._bottom_height = 50

        self._current_view = None

    def start(self):
        """Methods sets the common frames across all of the views, as well as
        a common list of action buttons (e.g. start, exit) at the bottom of all the views.
        """
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

        center_frame = Frame(
            self._root,
            bg="cyan",
            width=self._root_width,
            heigh=self._root_height - self._bottom_height,
        )

        bottom_frame = Frame(
            self._root,
            bg="black",
            width=self._root_width,
            height=self._bottom_height,
        )

        center_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        bottom_frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        bottom_frame.grid_rowconfigure(1)
        bottom_frame.grid_columnconfigure(
            [0, 1, 2, 3, 4, 5, 6, 7], minsize=(self._root_width/8))

        bottom_frame_headlines = ["Intro", "Options", "Start", "Exit"]
        commands = [lambda: self._show_intro_view(center_frame),
                    lambda: self._show_options_view(center_frame),
                    lambda: self._show_game_view(center_frame),
                    self._quit]

        for j in range(0, len(bottom_frame_headlines)):
            button = Button(
                bottom_frame,
                text=bottom_frame_headlines[j],
                compound="center",
                width=12,
                height=1,
                background="orange",
                activebackground="red",
                command=commands[j]
            )

            button.grid(
                row=0,
                column=j,
                padx=12,
                pady=12
            )

        self._show_opening_view(center_frame)

    def _show_opening_view(self, screen):
        """Method draws the opening view of the common frame.

        Args:
            screen (frame): Method is given a frame defined in the common UI.
        """
        new_center_frame = Frame(
            screen,
            bg="cyan",
            width=self._root_width,
            heigh=self._root_height - self._bottom_height,
        )

        new_center_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self._current_view = OpeningView(
            new_center_frame
        )

    def _show_intro_view(self, screen):
        """Method draws the introduction view of the common frame.

        Args:
            screen (frame): Method is given a frame defined in the common UI.
        """

        new_center_frame = Frame(
            screen,
            bg="cyan",
            width=self._root_width,
            heigh=self._root_height - self._bottom_height,
        )

        new_center_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self._current_view = IntroView(
            new_center_frame
        )

    def _show_options_view(self, screen):
        """Method draws the options view of the common frame.

        Args:
            screen (frame): Method is given a frame defined in the common UI.
        """

        new_center_frame = Frame(
            screen,
            bg="cyan",
            width=self._root_width,
            heigh=self._root_height - self._bottom_height,
        )

        new_center_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self._current_view = OptionsView(
            new_center_frame
        )

    def _show_game_view(self, screen):
        """Method draws the games view of the common frame.

        Args:
            screen (frame): Method is given a frame defined in the common UI.
        """

        new_center_frame = Frame(
            screen,
            bg="cyan",
            width=self._root_width,
            heigh=self._root_height - self._bottom_height,
        )

        new_center_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self._current_view = GameView(
            new_center_frame
        )

    def _hide_current_view(self):
        """Method hides the currently active view.
        """
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _quit(self):
        """Method exits the game.
        """
        self._root.destroy()

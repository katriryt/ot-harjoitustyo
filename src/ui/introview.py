from tkinter import Label
import os
from PIL import Image, ImageTk
from ui.fonts import Fonts


class IntroView():
    """Purpose of this view is to give information about the game
    for the player.
    """

    def __init__(self, root):
        """Constructor for the class.

        Args:
            root (frame): Sets the frame where everything in the view
            is presented.
        """
        self._root = root
        self.fonts = Fonts()
        self._initialize()

    def destroy(self):
        """Method destroys the root of the view.
        """
        self._root.destroy()

    def _initialize(self):
        """Method initializes all the visual elements in the view.
        """

        self._create_intro_headline_label("Welcome to Katakana no geemu!")
        self._create_instructions()
        self._create_picture()

    def _create_intro_headline_label(self, given_text):
        """Method creates and draws the headline for the introduction screen.
        """
        headline_label = Label(
            self._root,
            text=given_text,
            font=self.fonts.small_headline_font)

        headline_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=12,
            pady=12
        )

    def _create_instructions(self):
        """Method creates and draws instructions for the game on the introduction screen.
        """
        all_text = ["",
                    "Purpose of the game is to...",
                    "... identify pairs of katakana characters",
                    "... collect points, and",
                    "... keep your team alive",
                    "",
                    "Instructions: ",
                    " * Two cards can be open at the same time",
                    " * Same card can be opened multiple times",
                    " * Not all cards are katakanas - some may hurt your team",
                    " * Level is cleared when all pairs are found",
                    " * There is no time limit",
                    "",
                    "Next: Choose your name and difficulty level from Options",
                    "... or start the game immediately from Start"]

        row_list = []
        for i in range(0, len(all_text)+1):
            row_list.append(i)

        self._root.grid_rowconfigure(row_list, minsize=10)
        self._root.grid_columnconfigure([0, 1], minsize=50)

        for j in range(0, len(all_text)):
            label = Label(
                self._root,
                text=all_text[j],
                font=self.fonts.medium_text_font
            )

            label.grid(
                row=j+1,
                column=1,
                padx=0,
                pady=0,
                sticky="w"
            )

    def _create_picture(self):
        """Method creates and draws picture in katakanas on the side of the introduction screen.
        """
        text = os.path.join(".", "data", "katakana2.png")
        image1 = Image.open(text)

        image1 = image1.resize((150, 500), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(
            self._root,
            image=test,
        )

        label1.image = test

        label1.place(x=800, y=25)

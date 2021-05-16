from tkinter import Label
import os
from PIL import Image, ImageTk
from ui.fonts import Fonts


class OpeningView():
    """Purpose of the class is to draw the opening view for the game.
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
        """Method calls other methods to create and draw
        all the visual elements in the view.
        """
        self.create_big_katakana_headline()
        self.create_small_headline_label()
        self.create_picture()

    def create_big_katakana_headline(self):
        """Method creates and draws the game headline in katakanas.
        """
        name_of_game = "\u30AB\u30BF\u30AB\u30CA\u306E\u30B2\u30FC\u30E0"
        headline_label = Label(
            self._root,
            text=name_of_game,
            font=self.fonts.big_katakana_headline_font)

        headline_label.place(x=100, y=250)

    def create_small_headline_label(self):
        """Method creates and draws the headline of the game in roomaji.
        """
        headline_label = Label(
            self._root,
            text="katakana no geemu",
            font=self.fonts.big_text_font)

        headline_label.place(x=360, y=320)

    def create_picture(self):
        """Method creates and draws a picture of the game.
        """
        text = os.path.join(".", "data", "suddendeath.png")
        image1 = Image.open(text)

        image1 = image1.resize((400, 200), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(
            self._root,
            image=test,
        )

        label1.image = test

        label1.place(x=550, y=70)

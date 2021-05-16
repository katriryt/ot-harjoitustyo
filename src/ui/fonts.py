import tkinter.font as tkFont


class Fonts():
    """Class defines the common fonts and their sizes used in the game.
    """

    def __init__(self):
        """ Constructor for the class. It contains the common fonts and their sizes.
        """
        self.big_katakana_headline_font = tkFont.Font(size=50)
        self.medium_headline_font = tkFont.Font(size=40)
        self.small_headline_font = tkFont.Font(size=30)
        self.big_text_font = tkFont.Font(size=20)
        self.medium_text_font = tkFont.Font(size=15)
        self.small_text_font = tkFont.Font(size=10)
        self.medium_katakana_text_font = tkFont.Font(size=20)
        self.small_katakana_text_font = tkFont.Font(size=12)

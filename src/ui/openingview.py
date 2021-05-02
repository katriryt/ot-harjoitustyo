from tkinter import Label
import os
from PIL import Image, ImageTk


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
        self._initialize()

    def destroy(self):
        """Method destroys the root of the view.
        """
        self._root.destroy()

    def _initialize(self):
        """Method initializes all the visual elements in the view.
        """
        self._root.grid_rowconfigure([0, 1, 2, 3], minsize=100)
        self._root.grid_columnconfigure([0, 1, 2, 3], minsize=200)

        headline_label = Label(
            self._root,
            text="Katakana no geemu - welcome",
        )

        text = os.path.join(".", "data", "explosion2.png")
        image1 = Image.open(text)

        image1 = image1.resize((400, 200), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(
            self._root,
            image=test,
            bg="cyan"
        )

        label1.image = test

        headline_label.grid(
            row=2,
            column=2,
            columnspan=1
        )

        label1.place(x=400, y=0)

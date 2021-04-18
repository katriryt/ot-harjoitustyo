#from tkinter import *
from tkinter import Label
from PIL import Image, ImageTk

class OpeningView():
    def __init__(self, root):
        self._root = root                               # given root value: center_frame
        self._initialize()

    def destroy(self):                                  # removes the view
        self._root.destroy()

    def _initialize(self):

        self._root.grid_rowconfigure([0, 1, 2, 3], minsize = 100)
        self._root.grid_columnconfigure([0, 1, 2, 3], minsize = 200)  # note: need to define for each frame how want to divide to grid

        headline_label = Label(
            self._root,
            text = "Katakana no geemu - welcome",
            )

        image1 = Image.open("C:\MyFolder\School\TKT20002 Ohjelmistotekniikka\Vko3\peli_kuvia\explosion2.png")
        image1 = image1.resize((400, 200), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(
            self._root,
            image = test,
            bg = "cyan"
        )

        label1.image = test

        headline_label.grid(
            row = 2,
            column = 2,
            columnspan = 1
        )

        label1.place(x = 400, y = 0)

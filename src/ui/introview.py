from tkinter import Label


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
        self._initialize()

    def destroy(self):
        """Method destroys the root of the view.
        """
        self._root.destroy()

    def _initialize(self):
        """Method initializes all the visual elements in the view.
        """
        self._root.configure(bg="cyan")

        all_text = ["Welcome to the Katakana no geemu!",
                    "",
                    "Purpose of the game is to...",
                    "... identify pairs of katakana characters",
                    "... collect points, and",
                    "... to keep your team alive",
                    "",
                    "Instructions: ",
                    " * You have a limited amount of time available to identify the pairs",
                    " * Two cards can be open at the same time",
                    " * Same card can be opened multiple times",
                    " * Not all cards are katakanas - some may hurt your team",
                    " * Level is cleared when only non-katakanas are left on the table",
                    "",
                    " Next: Choose the difficulty level and your team from Options!",
                    "NOTE: THIS IS WORKING DRAFT, ALL FUNCTIONALITIES ARE NOT YET IN PLACE"]

        row_list = []
        for i in range(0, len(all_text)+1):
            row_list.append(i)

        self._root.grid_rowconfigure(row_list, minsize=10)
        self._root.grid_columnconfigure([0, 1], minsize=100)

        for j in range(0, len(all_text)):
            label = Label(
                self._root,
                text=all_text[j],
                background="cyan"
            )

            label.grid(
                row=j,
                column=0,
                padx=0,
                pady=0,
                sticky="w"
            )

from ui.playgameinteractions import PlayGameInteractions


class GameView():
    """Class draws the outline for the game view.
    Class will be combined with the PlayGameInteractions class
    """

    def __init__(self, root):
        self._root = root
        self._initialize()

    def destroy(self):
        self._root.destroy()

    def _initialize(self):

        PlayGameInteractions(self._root)

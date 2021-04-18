class Player():
    def __init__(self, given_name):
        self._name = given_name
        self._points = 0

    def _add_points(self, new_points):
        self._points += new_points

    def _show_points(self):
        return self._points

    def __str__(self):
        return f"Player name is {self._name}"
#        return f"{self._name}"

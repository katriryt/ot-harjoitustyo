from tkinter import Label
from tkinter import ttk
from tkinter import Button
from repositories.playerdatabaseinteraction import PlayerDatabaseInteraction
from repositories.katakanadatabaseinteraction import KatakanaDatabaseInteraction


class OptionsView():
    """Purpose of the class is to present the levels available for playing for the player,
    and to let the player select their name and the level for their game.
    """

    def __init__(self, root):
        """Constructor for the class.

        Args:
            root (Frame): Sets the frame where everything in the view
            is presented.
        """
        self._root = root
        self._current_view = None
        self.database = PlayerDatabaseInteraction()
        self._game_database = KatakanaDatabaseInteraction()
        self._current_max_game_level = 12

        self._selected_name_for_game = "NoName"
        self._selected_level_for_game = 1

        self.stats_label = ""
        self.names_used = ""
        self.name_box = ""
        self._game_level_buttons = []
        self._selected_button = ""

        self.start()

    def destroy(self):
        """Method destroys the root of the view.
        """
        self._root.destroy()

    def start(self):
        """Method initializes the frame for the view, and
        calls all the methods to be drawn on the view.
        """
        self._root.grid_rowconfigure(10, minsize=1, weight=1)
        self._root.grid_columnconfigure(10, minsize=1, weight=1)

        self._create_headline()
        self._create_name_drop_box()
        self._choose_name_for_game()
        self._draw_stats()
        self._create_level_headline()
        self._generate_level_buttons()
        self._update_current_game_optios()

    def _create_headline(self):
        """Method sets up and draws the headline for the screen.
        """
        headline_label = Label(
            self._root,
            text='Options: Insert your name and select the level for your game')

        headline_label.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w"
        )

    def _create_name_drop_box(self):
        """Method sets up and draws headline for the drop box of names.
        """
        name_label = Label(
            self._root,
            text="Player name"
        )

        name_label.grid(
            row=1,
            column=0,
            sticky="w"
        )

    def _draw_stats(self):
        """Method sets up and draws the current statistics for
        the chosen player on the screen.
        """
        self.stats_label = Label(
            self._root,
            text="placeholder"
        )

        self.stats_label.grid(
            row=2,
            column=1,
            columnspan=4,
            sticky="w"
        )

    def _choose_name_for_game(self):
        """Method creates a drop box from which the player can select a name,
        or in which the player can type their name.
        """

        self.names_used = self.database._get_all_players_names()

        self.name_box = ttk.Combobox(
            self._root,
            value=self.names_used
        )

        self.name_box.bind("<<ComboboxSelected>>", self._comboclick)
        self.name_box.bind("<Return>", self._comboclick)
        self.name_box.grid(
            row=1,
            column=1,
            sticky="w"
        )

    def _comboclick(self, event):
        """Method checks if the name player typed in is acceptable.
        If it is and it does not yet exist, it calls other classes to
        create a new player for the game.
        """
        input_name = self.name_box.get()

        if self._check_if_name_ok(input_name) is True:
            if self.database._check_player_exists(input_name) is False:
                self.database._create_new_player(input_name)
                self.names_used = self.database._get_all_players_names()
                self.name_box["values"] = self.names_used

            player_stats = self.database._get_one_player_stats(input_name)

            new_text = (
                f"{self.name_box.get()}, points are {player_stats[1]}, lives are {player_stats[2]}, level is {player_stats[3]}")

            self.stats_label["text"] = new_text

            self._selected_name_for_game = self.name_box.get()
            self._update_current_game_optios()

    def _check_if_name_ok(self, proposed_name):
        """Method checks if the name typed by player is acceptable.
        """
        if len(proposed_name) > 10:
            new_text = "Player name max 10 characters"
            self.stats_label["text"] = new_text
            return False

        if any(not character.isalnum() for character in proposed_name):
            new_text = "Please use only numbers and/or letters"
            self.stats_label["text"] = new_text
            return False

        return True

    def _create_level_headline(self):
        """Method sets up and draws label instructing player to choose their
        level for the game at hand.
        """
        level_headline_label = Label(
            self._root,
            text='Select your game - you can only choose levels available')

        level_headline_label.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="w"
        )

    def _generate_level_buttons(self):
        """Method generates buttons from which the player can choose level for
        the next game.
        """
        game_levels = self._game_database._get_all_game_levels()

        number_of_rows = 3
        number_of_columns = 4
        game_level_button = 0
        self._game_level_buttons = []
        self._selected_button = None

        self._allowed_max_level = self._current_max_game_level

        for i in range(0, number_of_rows):
            for j in range(0, number_of_columns):
                if game_level_button < len(game_levels):
                    self._game_level_buttons.append(Button(
                        self._root,
                        text=game_levels[game_level_button],
                        width=6,
                        height=1,
                        background="white",
                        command=lambda x=game_level_button: self._select_game_level(
                            x)
                    ))
                    self._game_level_buttons[game_level_button].grid(
                        row=5+i,
                        column=1+j,
                        padx=0.5,
                        pady=0.5,
                    )
                    game_level_button += 1
                else:
                    break

        for i in range(0, len(self._game_level_buttons)):
            if i+1 > self._allowed_max_level:
                self._game_level_buttons[i].configure(state="disabled")

    def _select_game_level(self, selected_game_level_button):
        """ Method updates the visual outlook of the game level button
        when it is selected.
        """
        if self._selected_button is None:
            self._game_level_buttons[selected_game_level_button].configure(
                relief="sunken")
        else:
            self._game_level_buttons[self._selected_button].configure(
                relief="raised")
            self._game_level_buttons[selected_game_level_button].configure(
                relief="sunken")

        self._selected_button = selected_game_level_button
        self._selected_level_for_game = selected_game_level_button + 1
        self._update_current_game_optios()

    def _update_current_game_optios(self):
        """Method calls other classes to update information on
        the game to be played.
        """
        self.database._update_current_game_specs(
            (self._selected_name_for_game, self._selected_level_for_game))

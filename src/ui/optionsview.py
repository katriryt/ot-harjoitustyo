from tkinter import Label
from tkinter import ttk
from tkinter import Button
from ui.fonts import Fonts
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
        self.fonts = Fonts()
        self.database = PlayerDatabaseInteraction()
        self._game_database = KatakanaDatabaseInteraction()

        self._selected_name_for_game = "NoName"
        self._selected_level_for_game = 1

        self.names_used = ""
        self.name_box = ""

        self._game_level_buttons = []
        self._selected_button = ""

        starting_player_stats = self.database.get_one_player_stats(
            self._selected_name_for_game)

        self._allowed_max_level = ""

        self._current_max_game_level = starting_player_stats[3]

        self._current_total_points = starting_player_stats[1]
        self._current_lives = starting_player_stats[2]

        self.current_max_level_label = ""
        self.current_total_points_label = ""
        self.current_lives_label = ""
        self.message_to_player_label = ""

        self.start()

    def destroy(self):
        """Method destroys the root of the view.
        """
        self._root.destroy()

    def start(self):
        """Method initializes the frame for the view, and
        calls the methods to be drawn on the view.
        """
        self._root.grid_rowconfigure(10, minsize=50, weight=1)
        self._root.grid_columnconfigure(7, minsize=50, weight=1)

        self._create_headline()
        self._draw_message_to_player()
        self._create_name_drop_box_headline()
        self._choose_name_for_game()
        self._create_level_headline()
        self._generate_level_buttons()

        self._draw_stats_headline()
        self._draw_stats_max_level()
        self._draw_stats_points()
        self._draw_stats_lives()
        self._draw_instructions_label()
        self._update_current_game_optios()

    def _create_headline(self):
        """Method sets up and draws the headline for the screen.
        """
        headline_label = Label(
            self._root,
            text='Game options',
            font=self.fonts.small_headline_font)

        headline_label.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="w",
            padx=12,
            pady=12
        )

    def _draw_message_to_player(self):
        """Method creates and draws a label showing changing instructions
        for the player in the screen.
        """
        starting_text = "These are the options for the default player"
        self.message_to_player_label = Label(
            self._root,
            text=starting_text,
            anchor='w',
            justify='left',
            font=self.fonts.small_text_font
        )

        self.message_to_player_label.place(x=12, y=400)

    def _create_name_drop_box_headline(self):
        """Method sets up and draws headline for the drop box of names.
        """
        name_label = Label(
            self._root,
            text="Player name",
            font=self.fonts.medium_text_font
        )

        name_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=12,
            pady=12
        )

    def _choose_name_for_game(self):
        """Method creates a drop box from which the player can select a name,
        or in which the player can type his/her name for the game.
        """

        self.names_used = self.database.get_all_players_names()

        self.name_box = ttk.Combobox(
            self._root,
            value=self.names_used,
            font=self.fonts.medium_text_font
        )

        self.name_box.bind("<<ComboboxSelected>>", self._comboclick)
        self.name_box.bind("<Return>", self._comboclick)
        self.name_box.grid(
            row=1,
            column=1,
            sticky="w",
            columnspan=3
        )

    def _comboclick(self, event):
        """Method checks if the name player typed in is acceptable.
        If it is, and it does not yet exist, it calls other methods to
        create a new player for the game.
        """
        input_name = self.name_box.get()

        if self._check_if_name_ok(input_name) is True:
            if self.database.check_player_exists(input_name) is False:
                self.database.create_new_player(input_name)
                self.names_used = self.database.get_all_players_names()
                self.name_box["values"] = self.names_used

            player_stats = self.database.get_one_player_stats(input_name)
            self._update_stats(player_stats)
            self._generate_level_buttons()

            new_text = (
                f" You selected a player with name {self.name_box.get()}.")
            self.message_to_player_label["text"] = new_text

            self._selected_name_for_game = self.name_box.get()
            self._update_current_game_optios()

    def _check_if_name_ok(self, proposed_name):
        """Method checks if the name typed by the player is acceptable.
        If not, it gives a message to player how to correct the input.
        """
        if len(proposed_name) > 10:
            new_text = "Player name max 10 characters"
            self.message_to_player_label["text"] = new_text
            return False

        if any(not character.isalnum() for character in proposed_name):
            new_text = "Please use only numbers and/or letters in player name"
            self.message_to_player_label["text"] = new_text
            return False

        return True

    def _update_stats(self, given_player_stats):
        """Method updates key statistics for the chosen or the default player,
        e.g. maximum level the player can play.

        Args:
            given_player_stats (tuple): Tuple consists of player name, player's total points,
            player's current lives and maximum level the player can play.
        """
        player_stats = given_player_stats
        self._current_max_game_level = player_stats[3]
        self._current_total_points = player_stats[1]
        self._current_lives = player_stats[2]

        self.current_max_level_label.configure(
            text=(f"Highest level: {self._current_max_game_level}"))
        self.current_total_points_label.configure(
            text=(f"Total points: {self._current_total_points}"))
        self.current_lives_label.configure(
            text=(f"Team size: {self._current_lives}"))

    def _create_level_headline(self):
        """Method sets up and draws label instructing player to choose their
        level for the game at hand.
        """
        level_headline_label = Label(
            self._root,
            text='Game level',
            font=self.fonts.medium_text_font
        )

        level_headline_label.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="w",
            padx=12,
            pady=12
        )

    def _generate_level_buttons(self):
        """Method generates and updates buttons from which the player
        can choose level for the next game - depending on the highest level
        attainable for the player.
        """
        game_levels = self._game_database.get_all_game_levels()

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
                        height=2,
                        background="white",
                        font=self.fonts.medium_text_font,
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
        """Method calls other methods to update information on
        the game to be played.
        """
        self.database.update_current_game_specs(
            (self._selected_name_for_game, self._selected_level_for_game))

    def _draw_stats_headline(self):
        """Method creates and draws headline for statistics.
        """
        label = Label(
            self._root,
            text="Player statistics:",
            font=self.fonts.medium_text_font
        )

        label.grid(
            row=4,
            column=6,
            columnspan=2,
            sticky="w",
            padx=50,
            pady=0.5
        )

    def _draw_stats_max_level(self):
        """Method creates and draws maximum level for the chosen or the default player.
        """
        self.current_max_level_label = Label(
            self._root,
            text=(f"Highest level: {self._current_max_game_level}"),
            font=self.fonts.medium_text_font
        )

        self.current_max_level_label.grid(
            row=5,
            column=6,
            columnspan=2,
            sticky="w",
            padx=50,
            pady=0.5
        )

    def _draw_stats_points(self):
        """Method creates and draws total points for the chosen or the default player.
        """
        self.current_total_points_label = Label(
            self._root,
            text=(f"Total points: {self._current_total_points}"),
            font=self.fonts.medium_text_font
        )

        self.current_total_points_label.grid(
            row=6,
            column=6,
            columnspan=2,
            sticky="w",
            padx=50,
            pady=0.5
        )

    def _draw_stats_lives(self):
        """Method creates and draws lives for the chosen or the default player.
        """
        self.current_lives_label = Label(
            self._root,
            text=(f"Team size: {self._current_lives}"),
            font=self.fonts.medium_text_font
        )

        self.current_lives_label.grid(
            row=7,
            column=6,
            columnspan=2,
            sticky="w",
            padx=50,
            pady=0.5
        )

    def _draw_instructions_label(self):
        """Method creates and draws a label showing constant instructions for the screen.
        """
        new_text = "Choose name from drop box or type in a new one\nOnly levels available for you can be selected"
        label = Label(
            self._root,
            text=new_text,
            anchor='w',
            justify='left',
            font=self.fonts.small_text_font
        )

        label.place(x=12, y=500)

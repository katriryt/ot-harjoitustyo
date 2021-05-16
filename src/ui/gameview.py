from tkinter import Button, Label
import math
import os
from PIL import Image, ImageTk
from ui.fonts import Fonts
from services.playgame import PlayGame


class GameView():
    """Purpose of the class is to draw and update the game view and all of its elements,
    as the game progresses.
    """

    def __init__(self, root):
        """Constructor for the class.

        Args:
            relevant_root (frame): Frame where the game view and board are drawm.
        """

        self._root = root
        self.fonts = Fonts()
        self.play_game = PlayGame()

        self.background_picture = ""
        self.cards = self._generate_game_list()
        self._card_background = ["" for _ in range(len(self.cards))]

        self._open_cards = []

        self.headline_label = ""
        self.info_label = ""
        self.game_stats_label = ""
        self.game_level_label = ""
        self.pairs_label = ""
        self.sudden_death_label = ""
        self.player_stats_label = ""
        self.player_name_label = ""
        self.points_label = ""
        self.lives_label = ""
        self.buttons = []

        self._draw_game_view()

    def destroy(self):
        self._root.destroy()

    def _draw_game_view(self):
        """Method sets up the basic visual configuration for the game,
        and calls all methods to e.g. drawn and update the game board.
        """
        self._root.grid_rowconfigure(
            [0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=100)
        self._root.grid_columnconfigure(
            [0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=50)

        self.create_background_picture()
        self._draw_games_headline()
        self._draw_info_label()
        self.draw_game_stats()
        self.draw_player_stats()
        self._set_up_game_board()

    def create_background_picture(self):
        """Method opens and creates a picture for the cards' background.
        """
        text = os.path.join(".", "data", "ji.png")
        image1 = Image.open(text)

        image1 = image1.resize((80, 80), Image.ANTIALIAS)
        self.background_picture = ImageTk.PhotoImage(image1)

    def _draw_games_headline(self):
        """Method sets up and draws the headline for the game view.
        """
        self.headline_label = Label(
            self._root,
            text="Play the game!",
            font=self.fonts.small_headline_font
        )

        self.headline_label.grid(
            row=0,
            column=0,
            columnspan=6,
            padx=12,
            pady=12,
            sticky="w"
        )

    def _draw_info_label(self):
        """Method sets up and draws the information and instruction label for the game.
        """
        self.info_label = Label(
            self._root,
            text="Press any card to start the game",
            font=self.fonts.small_text_font
        )

        self.info_label.place(x=12, y=520)

    def draw_game_stats(self):
        """Method draws the headline and contents for the current game's
        statistics, e.g. game level and pairs to be found.
        """
        game_stats_text = "Current game"
        self.game_stats_label = Label(
            self._root,
            text=game_stats_text,
            font=self.fonts.medium_text_font
        )

        game_level_text = (
            f" * Level: {self.play_game.current_game_level}")
        self.game_level_label = Label(
            self._root,
            text=game_level_text,
            font=self.fonts.medium_text_font
        )

        pairs_text = (
            f" * Pairs found: {self.play_game.pairs_found} / {self.play_game.pairs_to_find}")
        self.pairs_label = Label(
            self._root,
            text=pairs_text,
            font=self.fonts.medium_text_font
        )

        sudden_death_text = (
            f" * Sudden deaths: {self.play_game.sudden_deaths}")
        self.sudden_death_label = Label(
            self._root,
            text=sudden_death_text,
            font=self.fonts.medium_text_font
        )

        self.game_stats_label.place(x=600, y=100)
        self.game_level_label.place(x=600, y=150)
        self.pairs_label.place(x=600, y=200)
        self.sudden_death_label.place(x=600, y=250)

    def draw_player_stats(self):
        """Method draws the headline and contents for the player's statistics
        in the current game, e.g. player's name and points collected on the level.
        """
        self.player_stats_label = Label(
            self._root,
            text="Player statistics",
            font=self.fonts.medium_text_font
        )

        player_name_text = (
            f" * Player: {self.play_game.player_name}")
        self.player_name_label = Label(
            self._root,
            text=player_name_text,
            font=self.fonts.medium_text_font
        )

        points_label_text = (
            f" * Level points: {self.play_game.points}")
        self.points_label = Label(
            self._root,
            text=points_label_text,
            font=self.fonts.medium_text_font
        )

        lives_label_text = (
            f" * Team size: {self.play_game.lives}")
        self.lives_label = Label(
            self._root,
            text=lives_label_text,
            font=self.fonts.medium_text_font
        )

        self.player_stats_label.place(x=600, y=300)
        self.player_name_label.place(x=600, y=350)
        self.points_label.place(x=600, y=400)
        self.lives_label.place(x=600, y=450)

    def _set_up_game_board(self):
        """ Method draws the buttons forming the game board.
        """
        button_number = 0
        self.buttons = []

        number_of_rows = 4
        number_of_columns = math.ceil(len(self.cards)/number_of_rows)

        for i in range(0, number_of_rows):
            for j in range(0, number_of_columns):
                if button_number < len(self.cards):
                    self.buttons.append(Button(
                        self._root,
                        text="",
                        image=self.background_picture,
                        font=self.fonts.small_katakana_text_font,
                        background="white",
                        activebackground="white",
                        compound="c",
                        command=lambda x=button_number: self._card_pressed(x)
                    ))
                    self.buttons[button_number].grid(
                        row=1+i,
                        column=1+j,
                        sticky="nsew"
                    )
                    button_number += 1

    def _decode_katakana(self, input_button_number):
        """Method decodes the katakana characters unicode numbers from database
        to be properly interpreted and drawn as katakana characters.
        """
        raw_character = self.cards[input_button_number][1]
        raw_character = raw_character.encode('utf-8')
        return raw_character.decode('unicode-escape')

    def _card_pressed(self, input_button_number):
        """Method shows results from player selecting different cards.
        """
        if len(self._open_cards) == 2:
            self.player_has_two_cards_open(input_button_number)

        elif len(self._open_cards) < 2:
            self.update_info_label("")

            if input_button_number not in self._open_cards:
                self.player_turns_new_card(input_button_number)

                if self.cards[input_button_number][1] == "Death":
                    self.player_turns_death_card()

                else:
                    if len(self._open_cards) == 2:
                        if self.cards[self._open_cards[0]] == self.cards[self._open_cards[1]]:
                            self.player_finds_a_pair()

                            if self.play_game.pairs_found == self.play_game.pairs_to_find:
                                self.player_has_found_all_pairs()

            else:
                self.player_tries_a_card_no_special_action(input_button_number)

    def player_has_two_cards_open(self, input_button_number):
        """ Method defines reactions to player's actions, when there are two
        cards open. If the currently open card is pressed, it is turned around.
        If player tries to open a third card, it gives an instruction message.
        """
        if input_button_number in self._open_cards:
            self.update_info_label("")
            self.turn_card_background_up(input_button_number)
            self._open_cards.remove(input_button_number)
        else:
            self.update_info_label(
                "Two cards are open - close at least one to continue")

    def player_turns_new_card(self, input_button_number):
        """ When player presses a card that is not open, method "turns" the card
        showing the katakana character on the card.
        """
        self.buttons[input_button_number].configure(
            image="",
            text=(f"""{self._decode_katakana(input_button_number)} {self.cards[input_button_number][0]}"""))

        self._open_cards.append(input_button_number)

    def player_turns_death_card(self):
        """If player turns a death card, method calls to reduce player's lives
        and depending on the remaining lives either continues the game or
        ends the game.
        """
        self.play_game.death_card_reduce_lives()

        if self.play_game.lives > 0:
            self.update_lives_label()
            self.update_info_label(
                "Sudden Death: Oh no - you lost a team member!")

        if self.play_game.lives == 0:
            self.update_lives_label()
            self.update_info_label("You have no more team left - GAME OVER")
            self._game_over("loss")

    def player_finds_a_pair(self):
        """ When player finds a pair, method calls for other methods to
        e.g. disable the cards for the found pair, and to increase player's points.
        """
        self.pair_found_disable_card(0)
        self.pair_found_disable_card(1)

        self.play_game.pair_found_add_points()
        self.update_points_label()

        self.play_game.pair_found_add_pairs()
        self.update_pairs_found_label()

        self._open_cards = []

        self.update_info_label(
            "Congratulations! You found a pair!")

    def player_has_found_all_pairs(self):
        """ When the player has found all pairs, method calls for other methods
        to e.g. add points and end the game as a win
        """
        self.play_game.all_pairs_found_add_points()
        self.update_points_label()
        self.update_info_label(
            "Congratulations! Level cleared!")
        self._game_over("win")

    def player_tries_a_card_no_special_action(self, input_button_number):
        """When less than two cards are open, and player presses the same card again,
        it is closed.

        Args:
            input_button_number (integer): indicates the card clicked by the player.
        """
        self.update_info_label("")
        self.turn_card_background_up(input_button_number)
        self._open_cards.remove(input_button_number)

    def _game_over(self, reason_for_end):
        """Method calls other methods, depending on the reason
        for the game's end.

        Args:
            reason_for_end (string): Value is "win" or "loss".
        """

        if reason_for_end == "win":
            self.play_game.win_update_all_stats()
            self.final_update_screen("win")

        elif reason_for_end == "loss":
            self.play_game.loss_update_all_stats()
            self.final_update_screen("loss")

    def final_update_screen(self, result):
        """Method updates the final screen, calling other methods to e.g.
        update labels on screen, and giving final instructions.

        Args:
            result (string): Value is "win" or "loss".
        """
        self.update_points_label()
        self.update_lives_label()
        self.disable_all_cards()

        if result == "win":
            final_text = f"Congratulations!\nLevel cleared!\nYou found new team members!\nYour max level is now {self.play_game.player_highest_level}.\nPress start to play again?"

        elif result == "loss":
            final_text = "Unfortunately you lost.\nTo continue, we found\na new team member.\nPress start to play again."

        final_text_label = Label(
            self._root,
            text=final_text,
            font=self.fonts.medium_text_font,
            bg="red",
            width=35,
            height=15
        )

        final_text_label.place(x=80, y=125)

    def _generate_game_list(self):
        """Method calls for game specifications and cards to be presented in the game
        from other classes.
        """
        new_cards = self.play_game.get_card_list()

        return new_cards

    def update_info_label(self, given_text):
        """Method updates information label to the given text.

        Args:
            given_text (string): Message to be drawn to the screen.
        """
        self.info_label.configure(text=given_text)

    def update_lives_label(self):
        """Method updates lives label to the current situation of the game.
        """
        lives_label_text = (f" * Team size: {self.play_game.lives}")
        self.lives_label.configure(
            text=lives_label_text)

    def update_points_label(self):
        """Method updates points label to the current situation of the game.
        """
        points_label_text = (
            f" * Level points: {self.play_game.points}")
        self.points_label.configure(
            text=points_label_text)

    def turn_card_background_up(self, input_button_number):
        """Method updates text / picture drawn on the button to be the
        background of the card.

        Args:
            input_button_number (integer): Number for the card to be
            updated.
        """
        self.buttons[input_button_number].configure(image=self.background_picture,
                                                    text=self._card_background[input_button_number])

    def update_pairs_found_label(self):
        """ Method updates the number of pairs found and the number of pairs
        to find on the screen.
        """
        pairs_text = (
            f" * Pairs found: {self.play_game.pairs_found} / {self.play_game.pairs_to_find}")
        self.pairs_label.configure(
            text=pairs_text)

    def pair_found_disable_card(self, card_number):
        """Method disables a card.

        Args:
            card_number (integer): Number for the card to be updated.
        """
        self.buttons[self._open_cards[card_number]
                     ].configure(state="disabled")

    def disable_all_cards(self):
        """ Method diables all cards on the table.
        """
        for i in range(0, len(self.cards)):
            self.buttons[i].configure(state="disabled")

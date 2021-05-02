from tkinter import Button, Label
import math
from repositories.playerdatabaseinteraction import PlayerDatabaseInteraction
from repositories.katakanadatabaseinteraction import KatakanaDatabaseInteraction


class PlayGameInteractions():
    """Purpose of this class is to draw e.g. draw game board and
    print instructions for the player on the Game View.
    Note. This class will be refactored and combined with the GameView class.
    """

    def __init__(self, relevant_root):
        """Constructor for the class.

        Args:
            relevant_root (frame): Frame where the game board is to be drawm.
        """
        self._root = relevant_root
        self._database = PlayerDatabaseInteraction()
        self._katakana_database = KatakanaDatabaseInteraction()

        self._lives = 5
        self._points = 0
        self._pairs_to_find = 5
        self._sudden_deaths = 2

        self.cards = self._generate_game_list()

        self._card_background = ["CARD_BACK" for _ in range(len(self.cards))]
        self._pairs_found = 0
        self._open_cards = []

        self.headline_label = ""
        self.info_label = ""
        self.points_label = ""
        self.lives_label = ""
        self.buttons = []

        self._draw_game_view()

    def _draw_game_view(self):
        """Method sets up the basic visual configuration for the game,
        and calls all methods to e.g. drawn the game board.
        """
        self._root.grid_rowconfigure(
            [0, 1, 2, 3, 4, 5, 6], minsize=100)
        self._root.grid_columnconfigure(
            [0, 1, 2, 3, 4, 5, 6], minsize=50)

        self._draw_games_headline()
        self._draw_info_label()
        self._draw_points_label()
        self._draw_lives_label()
        self._set_up_game_board()

    def _draw_games_headline(self):
        """Method sets up and draws the headline for the game.
        """
        self.headline_label = Label(
            self._root,
            text="Game view"
        )

        self.headline_label.grid(row=0, column=0)

    def _draw_info_label(self):
        """Method sets up and draws the information label for the game.
        """
        self.info_label = Label(
            self._root,
            text="messages from the game"
        )

        self.info_label.place(x=600, y=100)

    def _draw_points_label(self):
        """ Method sets up and draws the label showing points for the game.
        """
        self.points_label = Label(
            self._root,
            text=(f"{self._points} points")
        )

        self.points_label.place(x=600, y=200)

    def _draw_lives_label(self):
        """Method sets up and draws the label showing remaining lives in the game.
        """
        self.lives_label = Label(
            self._root,
            text=(f"{self._lives} lives left")
        )

        self.lives_label.place(x=600, y=300)

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
                        text=self._card_background[button_number],
                        width=12,
                        height=6,
                        background="orange",
                        activebackground="red",
                        command=lambda x=button_number: self._card_pressed(x)
                    ))
                    self.buttons[button_number].grid(
                        row=1+i,
                        column=j,
                        padx=0.5,
                        pady=0.5,
                        sticky="w"
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
            if input_button_number in self._open_cards:
                self.update_info_label("you closed a card")

                self.turn_card_background_up(input_button_number)

                self._open_cards.remove(input_button_number)

            else:
                self.update_info_label(
                    "2 cards are open - close at least 1 to continue")

        elif len(self._open_cards) < 2:
            if input_button_number not in self._open_cards:

                self.buttons[input_button_number].configure(
                    text=(f"""{self._decode_katakana(input_button_number)}   {self.cards[input_button_number][0]}"""))

                self._open_cards.append(input_button_number)
                if self.cards[input_button_number][1] == "Sudden Death":
                    self._lives -= 1
                    if self._lives > 0:
                        self.update_lives_label(self._lives)
                        self.update_info_label(
                            "sudden death: now you lost a life")

                    if self._lives == 0:
                        self.update_lives_label(self._lives)
                        self._game_over("ALL LIVES ARE OUT - GAME OVER")

                else:
                    if len(self._open_cards) == 2:
                        if self.cards[self._open_cards[0]] == self.cards[self._open_cards[1]]:
                            self.pair_found_disable_card(0)
                            self.pair_found_disable_card(1)

                            self._points += 20
                            self.update_points_label(self._points)

                            self._pairs_found += 1
                            self._open_cards = []

                            if self._pairs_found == self._pairs_to_find:
                                self._points += self._pairs_to_find*20*2
                                self.update_points_label(self._points)
                                self._game_over(
                                    "CONGRATULATIONS! LEVEL CLEARED")
                            else:
                                self.update_info_label(
                                    "congratulations! you found a pair!")

            else:
                self.turn_card_background_up(input_button_number)
                self._open_cards.remove(input_button_number)

    def _game_over(self, message):
        """Method launches actions are game over is reached.
        (At the moment only messages)
        """
        self.update_info_label(message)

    def _generate_game_list(self):
        """Method calls for game specifications and cards to be presented in the game
        from other classes.
        """
        game_specs = self._database._get_current_game_specs()

        new_cards = self._katakana_database._get_cards_for_game_board(
            game_specs[1])

        return new_cards

    def update_info_label(self, given_text):
        """Method updates information label depending the situation of the game.

        Args:
            given_text (string): Message to be drawn to the screen is needed.
        """
        self.info_label.configure(text=given_text)

    def update_lives_label(self, new_lives):
        """Method updates lives label depending the situation of the game.

        Args:
            new_lives (integer): Updated number from the counter of the number of lives
            is needed.
        """
        self.lives_label.configure(
            text=(f"{new_lives} lives left"))

    def update_points_label(self, new_points):
        """Method updates points label depending the situation of the game.

        Args:
            new_points (integer): Updated number from the counter of the points
            is needed.
        """
        self.points_label.configure(
            text=f"{new_points} points")

    def turn_card_background_up(self, input_button_number):
        """Method updates text / picture drawn on the button to be the
        background of the card.

        Args:
            input_button_number (integer): Number for the card to be
            updated is needed.
        """
        self.buttons[input_button_number].configure(
            text=self._card_background[input_button_number])

    def pair_found_disable_card(self, card_number):
        """Method disables card, when its pair is found.

        Args:
            card_number (integer): Number for the card to be
            updated is needed.
        """
        self.buttons[self._open_cards[card_number]
                     ].configure(state="disabled")

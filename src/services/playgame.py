#from tkinter import *
from tkinter import Button, Label

#from PIL import Image, ImageTk
from functools import partial
import random


class PlayGame():
    def __init__(self, relevant_root):
        self._root = relevant_root
        self._lives = 5  # to be sent to game
        self._points = 0  # to be sent to game
        self._pairs_to_find = 5  # to be sent to game
        self._sudden_deaths = 2  # to be sent to game
        self.cards = self._generate_game_list(
            self._pairs_to_find, self._sudden_deaths)
        self._card_background = ["CARD_BACK" for _ in range(len(self.cards))]
        self._pairs_found = 0
        self._open_cards = []

        self._set_up_game_board()

    def _set_up_game_board(self):

        self._root.grid_rowconfigure(
            [0, 1, 2, 3, 4], minsize=100)  # how many rows
        self._root.grid_columnconfigure(
            [0, 1, 2, 3, 4], minsize=50)  # how many columns

        button_number = 0
        self.buttons = []

        number_of_rows = 4

        for i in range(0, number_of_rows):
            for j in range(0, int(len(self.cards)/number_of_rows)):
                #                button = Button(
                self.buttons.append(Button(
                    #                    game_frame,
                    self._root,
                    #                    text = cards[i][j],
                    text=self._card_background[button_number],
                    width=12,
                    height=6,
                    background="orange",
                    activebackground="red",
                    #                    command = lambda x = cards[i][j]: self._card_pressed(x),
                    #                    command = lambda x = cards[button_number]: self._card_pressed(x),
                    command=lambda x=button_number: self._card_pressed(x)
                ))
#                button.grid(
                self.buttons[button_number].grid(
                    row=1+i,
                    column=1+j,
                    padx=0.5,
                    pady=0.5,
                    sticky="w"
                )
                button_number += 1

        self.headline_label = Label(
            self._root,
            text="Game view"
        )

        self.info_label = Label(
            self._root,
            text="messages from the game"
        )

        self.points_label = Label(
            self._root,
            text=(f"{self._points} points")
        )
        self.lives_label = Label(
            self._root,
            text=(f"{self._lives} lives left")
        )

        self.headline_label.grid(row=0, column=0)
        self.info_label.place(x=600, y=100)
        self.points_label.place(x=600, y=200)
        self.lives_label.place(x=600, y=300)

    def _card_pressed(self, input_button_number):
        #        print("card was pressed")
        #        print(self._open_cards)
        #        print(input_button_number)
        #        print(self.cards[input_button_number])
        #        print(self._open_cards)

        if len(self._open_cards) == 2:  # if there are two cards open
            if input_button_number in self._open_cards:
                # ... and you press the same card, the card turns over
                #                print("is in list")
                self.info_label.configure(text="you closed a card")
#                self.buttons[input_button_number].configure(text = self.cards[input_button_number])
                self.buttons[input_button_number].configure(
                    text=self._card_background[input_button_number])
                # poistetaan se sieltä
                self._open_cards.remove(input_button_number)
#                print(f" päivitetty avoimet kortit lista: {self._open_cards}")
            # if you press a third card, nothing happens (except error message)
            else:
                self.info_label.configure(
                    text="2 cards are open - close at least 1 to continue")

        elif len(self._open_cards) < 2:  # if less than two cards are open
            #            self._open_cards.append(self.cards[input_button_number])
            #            print(input_button_number)
            #            print(self._open_cards)
            if input_button_number not in self._open_cards:
                # and the current pressed one is not open
                #                print("not in list")
                #                self.buttons[input_button_number].configure(text = self.cards[input_button_number])
                #                self.buttons[input_button_number].configure(
                # text = self.cards[input_button_number][1])
                self.buttons[input_button_number].configure(
                    text=(f"""{self.cards[input_button_number][1]}   {self.cards[input_button_number][0]}"""))
                self._open_cards.append(input_button_number)
#                if self.cards[input_button_number] == "sudden": # works
                if self.cards[input_button_number][1] == "sudden":
                    # if card is sudden death and this one has not yet been opened
                    self._lives -= 1
                    if self._lives > 0:  # if lives are still left
                        self.lives_label.configure(
                            text=(f"{self._lives} lives left"))
                        self.info_label.configure(
                            text="sudden death: now you lost a life")
                    if self._lives == 0:
                        self.lives_label.configure(
                            text=(f"{self._lives} lives left"))
                        self._game_over("ALL LIVES ARE OUT - GAME OVER")
                else:  # if the card is not sudden death
                    #                    self.buttons[input_button_number].configure(text = "kukkuu")
                    #                    self.buttons[input_button_number].configure(
                    # text = self.cards[input_button_number])
                    if len(self._open_cards) == 2:  # and now there are two cards open
                        if self.cards[self._open_cards[0]] == self.cards[self._open_cards[1]]:
                            # and the cards are the same DISABLED
                            self.buttons[self._open_cards[0]
                                         ].configure(state="disabled")
                            self.buttons[self._open_cards[1]
                                         ].configure(state="disabled")
                            self._points += 20
                            self.points_label.configure(
                                text=f"{self._points} points")
                            self._pairs_found += 1
                            self._open_cards = []
                            if self._pairs_found == self._pairs_to_find:  # you find all the pairs
                                self._points += self._pairs_to_find*20*2  # get extra points
                                self.points_label.configure(
                                    text=f"{self._points} points")
                                self._game_over(
                                    "CONGRATULATIONS! LEVEL CLEARED")
                                # you will be taken away from the game screen
                            else:
                                self.info_label.configure(
                                    text="congratulations! you found a pair!")
            else:  # if the card is already open, it is turned over
                #                print("is in list")
                #                self.buttons[input_button_number].configure(text = self.cards[input_button_number])
                self.buttons[input_button_number].configure(
                    text=self._card_background[input_button_number])
                self._open_cards.remove(input_button_number)

#        print(self._open_cards)
#        print(self._pairs_to_find)
#        print(f"card background: {self._card_background}")

    def _game_over(self, message):
        self.publish = message
        self.info_label.configure(text=self.publish)

    def _generate_game_list(self, wanted_pairs, wanted_sudden_deaths):
        katakana_list_a = [("a", "\u30A2"), ("i", "\u30A4"),
                           ("u", "\u30A6"), ("e", "\u30A8"), ("o", "\u30AA")]
        katakana_list_ka = [("ka", "\u30AB"), ("ki", "\u30AD"),
                            ("ku", "\u30AF"), ("ke", "\u30B1"), ("ko", "\u30B3")]

        all_katakana = []
        for i in katakana_list_a:
            all_katakana.append(i)
        for i in katakana_list_ka:
            all_katakana.append(i)

        number_of_pairs = wanted_pairs
        number_of_sudden_deaths = wanted_sudden_deaths

        game_list = random.sample(all_katakana, number_of_pairs)*2
        for i in range(number_of_sudden_deaths):
            game_list.append(("", "sudden"))

        random.shuffle(game_list)
#        print(game_list)
        return game_list

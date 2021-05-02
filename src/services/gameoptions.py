# Tehdään tänne testialue nimen ja boksin luomiselle
# Avataan tätä varten erillinen ikkuna tkInteriin, johon koodataan tarvittavia pätkiä

from tkinter import Label  # Tk, Label
from tkinter import ttk  # tarpeen Comboboxissa
from entities.player import Player


class GameOptions:
    #    def __init__(self, root, input_width, input_height):
    def __init__(self, relevant_root):
        #        print("game options aloitettu")
        #        print(root)
        # Sets window as the main object and current view as None.
        self._root = relevant_root
        self._current_view = None
        self.database = Player()
#        self.database.create_player_database()
#        print(self.database.get_all_players_names())

        self.start()

    def start(self):
        #        print("startissa")
        self._root.grid_rowconfigure(10, minsize=1, weight=1)
        self._root.grid_columnconfigure(10, minsize=1, weight=1)
#        print("ckonfiguroinnissa")

#        self.database.create_player_database()

        headline_label = Label(
            self._root,
            text='Options: Insert your name and select the level for your game')

        name_label = Label(
            self._root,
            text="Player name"
        )

        # Piirretään gridille
#        headline_label.grid(
#            row=0,
#            column = 0,
#            columnspan=3)

#        headline_label.pack()

        headline_label.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w"
        )

#        names_from_database = self.database.get_all_players_names()

#        self.names_used = [
#            "NoName",
#            "Amaterasu",
#            "Okonomiyaki"
#        ]

        name_label.grid(
            row=1,
            column=0,
            sticky="w"
            #            columnspan=1
        )

        self._choose_name_for_game()

    def _choose_name_for_game(self):

        self.names_used = self.database.get_all_players_names()

        self.name_box = ttk.Combobox(
            self._root,
            value=self.names_used
        )

#        self.name_box.current(0) # ottaa ekan listalta
        self.name_box.bind("<<ComboboxSelected>>", self._comboclick)
        self.name_box.bind("<Return>", self._comboclick)
#        self.name_box.pack()
        self.name_box.grid(
            row=1,
            column=1,
            sticky="w"
        )

        self.stats_label = Label(
            self._root,
            #            text = self.name_box.get(),
            text="placeholder"
        )

#        new_label.pack()
        self.stats_label.grid(
            row=2,
            column=1,
            columnspan=4,
            sticky="w"
        )

    def _comboclick(self, event):
        input_name = self.name_box.get()

        if self._check_if_name_ok(input_name) == True:
            if self.database.check_player_exists(input_name) == False:
                #        if self.name_box.get() not in self.names_used:
                # Jos nimi ei ole listalla, lisätään se tietokantaan
                #                print(f"{self.name_box.get()} ei ole listalla")
                #            self.names_used.append(self.name_box.get()) # huom! ei päivitä dynaamisesti drop down -menua
                #            print(self.names_used)
                self.database.create_new_player(input_name)
                self.names_used = self.database.get_all_players_names()
                self.name_box["values"] = self.names_used

            else:
                #            print(f"{self.name_box.get()} on listalla")
                #                print(f"{input_name} on listalla")
                pass

            points = self.database.get_one_player_points(input_name)
            lives = self.database.get_one_player_lives(input_name)
            level = self.database.get_one_player_maxlevel(input_name)

            new_text = (
                f"{self.name_box.get()}, points are {points}, lives are {lives}, level is {level}")

            self.stats_label["text"] = new_text

    #        new_label = Label(
    #            self._root,
    ##            text = self.name_box.get(),
    #            text = new_text
    #        )
    #
    #        new_label.pack()
    #        new_label.grid(
    #            row = 2,
    #            column = 1,
    #            sticky = "w"
    #        )

    def _check_if_name_ok(self, proposed_name):
        #        print(proposed_name)

        if len(proposed_name) > 10:
            new_text = "Player name max 10 characters"
            self.stats_label["text"] = new_text
            return False

        if any(not character.isalnum() for character in proposed_name):
            new_text = "Please use only numbers and/or letters"
            self.stats_label["text"] = new_text
            return False

        return True

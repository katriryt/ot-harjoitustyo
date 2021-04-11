# Katakana no geemu: week 3: User can move between different pages

from tkinter import *
#from tkinter import Tk, ttk, constants
from PIL import Image, ImageTk
#import tkinter
from functools import partial

class UI: 
    def __init__(self, root):                           # Sets window as the main object and current view as None. 
        self._root = root
        self._root_width = 1000
        self._root_height = 600
        self._side_width = 120
        self._bottom_height = 50

        self._current_view = None

    def start(self): 
        #################################################################################################################
        # draws frame and basic buttons
        # create all the main containers, targeted for all views
        center_frame = Frame(
            self._root, 
            bg = "cyan", 
            width = self._root_width-self._side_width, 
            heigh = self._root_height - self._bottom_height, 
        )

        side_frame = Frame(
            self._root, 
            bg = "red", 
            width = self._side_width, 
            height = self._root_height-self._bottom_height
        )

        bottom_frame = Frame(
            self._root, 
            bg = "black", 
            width = self._root_width-self._side_width, 
            height = self._bottom_height
        )

        bottom_rhs_corner_frame = Frame(
            self._root, 
            bg = "pink", 
            width = self._side_width, 
            height = self._bottom_height
        )

        # layout for all the main containers: two rows and two columns
        self._root.grid_rowconfigure(2)
        self._root.grid_columnconfigure(2)

        # draw all frames to the common grid
        center_frame.grid(
            row = 0, 
            column = 0, 
            sticky = "nsew"
        )

        side_frame.grid(
            row = 0, 
            column = 1, 
            sticky = "nsew"
        )

        bottom_frame.grid(
            row = 1,
            column = 0, 
            sticky = "nsew"
        )

        bottom_rhs_corner_frame.grid(
            row = 1, 
            column = 1, 
            sticky = "nsew"
        )

        # BOTTOM RHS FRAME CONTENTS

        # create the bottom RHS corner widgets

#        bottom_rhs_corner

        bottom_rhs_corner_frame.grid_rowconfigure(1)
        bottom_rhs_corner_frame.grid_columnconfigure(1)

        exit_button = Button(
            bottom_rhs_corner_frame, 
            text = "Exit",
            compound = CENTER,
            width = 12, 
            height = 1,
            background = "orange", 
            activebackground = "red", 
            command = self._quit
        )

        exit_button.grid(
            row = 0, 
            column = 0, 
            padx = 12, 
            pady = 12
        )

#        bottom_frame 

        bottom_frame.grid_rowconfigure(1)
        bottom_frame.grid_columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize = (1000-120)/7)

        bottom_frame_headlines = ["Intro", "Options", "Start"]
        commands = [lambda: self._show_intro_view(center_frame), 
                    lambda: self._show_options_view(center_frame), 
                    lambda: self._show_game_view(center_frame)]

        for j in range(0, len(bottom_frame_headlines)): 
            button = Button(
                bottom_frame, 
                text = bottom_frame_headlines[j], 
                compound = CENTER, 
                width = 12,
                height = 1, 
                background = "orange", 
                activebackground = "red", 
                command = commands[j]
#                command = partial(
#                    self._show_intro_view,
#                    center_frame
#                    )  # toimii, mutta kun painaa, tulee virhe
#                command = self._show_intro_view
            )
            button.grid(
                row = 0, 
                column = j, 
                padx = 12,
                pady = 12
            )
        #################################################################################################################

        self._show_opening_view(center_frame)                       
#        self._show_intro_view(self._root, center_frame)            
#        self._show_options_view(center_frame)                       

    def _show_opening_view(self, screen):                       # calls opening view
        #self._hide_current_view()
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = Opening_View(
            screen
        )

    def _show_intro_view(self, screen):                       # calls intro
        #self._hide_current_view() # destroys the actual frame and everything in it. can not be accessed again
        # for info https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
        for widget in screen.winfo_children(): # removes widgets from e.g. frame without actually destroying the frame
            widget.destroy()
        self._current_view = Intro_View(
            screen
        )

    def _show_options_view(self, screen):
        #self._hide_current_view()
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = Options_View(
            screen
        )

    def _show_game_view(self, screen):
        #self._hide_current_view()
        for widget in screen.winfo_children():
            widget.destroy()
        self._current_view = Game_View(
            screen
        )

    def _hide_current_view(self):                       # removes current view
        if self._current_view: 
            self._current_view.destroy()
        self._current_view = None

    def _quit(self):                                    # ends the game and closes python
        #exit() 
        self._root.destroy()

class Opening_View(): 
    # first page when you start the application
    def __init__(self, root): 
        self._root = root                               # given root value: center_frame
        self._initialize()

    def destroy(self):                                  # removes the view
        self._root.destroy()

    def _initialize(self): 

        headline_label = Label(
            self._root, 
            text = "Katakana no geemu - welcome", 
            )

        image1 = Image.open("./data/explosion2.png")
        image1 = image1.resize((400, 200), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(
            self._root, 
            image = test,
            bg = "cyan"         
        )
        
        label1.image = test

        # layout for widgets in center frame
        self._root.grid_rowconfigure([0, 1, 2, 3], minsize = 100)
        self._root.grid_columnconfigure([0, 1, 2, 3], minsize = 200)  # note: need to define for each frame how want to divide to grid

        headline_label.grid(
            row = 2, 
            column = 2, 
            columnspan = 1
        ) 

        label1.place(x = 400, y = 0)

class Intro_View(): 
    def __init__(self, root): 
        self._root = root
        self._initialize()

    def destroy(self):                                  
        self._root.destroy()

    def _initialize(self): 

        self._root.configure(bg = "lightblue")

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
        "NOTE: THIS IS FIRST DRAFT, FUNCTIONALITIES ARE NOT YET IN PLACE"]

        row_list = []
        for i in range(0, len(all_text)+1): 
            row_list.append(i)

#        self._root.grid_rowconfigure(row_list, minsize = int((1000-100)/(16))))
        self._root.grid_rowconfigure(row_list, minsize = 10)
        self._root.grid_columnconfigure([0, 1], minsize = 100)

        for j in range(0, len(all_text)): 
            label = Label(
                self._root, 
                text = all_text[j], 
                background = "cyan"
            )

            label.grid(
                row = j, 
                column = 0, 
                padx = 0,
                pady = 0, 
                sticky = "w"
            )

class Options_View(): 
    def __init__(self, root): 
        self._root = root
        self._initialize()

    def destroy(self):                                  
        self._root.destroy()

    def _initialize(self): 

        self._root.configure(bg = "lightblue")

        self._root.grid_rowconfigure([0, 1, 2, 3], minsize = 100)
        self._root.grid_columnconfigure([0, 1, 2, 3], minsize = 100)

        label1 = Label(
            self._root, 
            text = "Welcome to options: Choose your player name, team, and game level"
        )

        label1.grid(
            row = 0, 
            column = 0
        )

class Game_View(): 
    def __init__(self, root): 
        self._root = root
        self._initialize()

    def destroy(self):                                  
        self._root.destroy()

    def _initialize(self): 

        self._root.configure(bg = "lightblue")

        self._root.grid_rowconfigure(1, minsize = 100)
        self._root.grid_columnconfigure(1, minsize = 100)

        label1 = Label(
            self._root, 
            text = "Here comes the actual game with functinalities and stats" 
        )

        label1.grid(
            row = 0, 
            column = 0
        )

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

##########################################################################################################
# One file for the main operations
# import all other files and classes 
# remember to include all other relevant imports

class Main: 

    window = Tk()

    # Basic setting for the window: title, size and ability to change (not allowed)
    window.title("Katakana no geemu_move_test")
    window.geometry("{}x{}".format(1000,600))
    window.resizable(False, False)

    ui = UI(window)
    ui.start()

    window.mainloop()

##########################################################################################################
# Calling from another file
#if __name__ == "__main__":
#    game = Main()
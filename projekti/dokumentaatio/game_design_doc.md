# Requirements Specification Document 

## Application Purpose

Purpose of the **Katakana no Geemu - Sudden Death** is to learn to read Japanese katakana symbols quickly in a fun and interactive way. 

Katakana is one of the three Japanese syllabary, along with hiragana and kanji (and in some cases the Latin script (known as roomaji)). 

The game is a modified version of a basic memory game (find the pairs game). The player needs to pick two cards with the same symbol from a set of turned over cards. There are a few "Sudden death" cards included in the set of cards, which cause the player to lose lives. There is also a timer, so the puzzle needs to be solved within a time limit. As levels become more difficult, time is reduced, number of cards and "Sudden death" cards is increased.

## User Groups

There is only one type of role in the application, normal user, i.e. a player. 

## User Interface Draft

To begin with, the game has six different screens. 

![Game design document picture](game_design_doc_pic.jpg)

To allow moving between screen, the same menu is shown at the bottom of every screen.

## Basic Version Functionalities

### High level functionalities by screen
* Screen 1 shows the name of the game and allows to go to introduction/options screen, start the game with default functionalities or exit.
* Screen 2 outlines the purpose of the game and the instructions for playing.
* In screen 3, the player can input their name, select their team and choose the level of the game (to begin with, only Level 0 (training mode) or Level 1 (easiest level)).
* In screen 4, a game board is set. The living members of the team are shows as well as the statistics for the game. 
* If the level is cleared (all identical pairs of katakana cards are identified within time limit, "Sudden death" cards may be left of the table unopened), game moves to screen 5, allowing e.g. advancement to new levels or replaying of the same level.
* If level is not cleared (cards are not identified within the time limit or the entire team is eliminated in the attempt), game moves to screen 6, allowing starting from level 0 and 1.

* The main screen will have a few different implementations depending on the level of the game. Variation could be done on e.g. number of cards, number of "Sudden death" cards, and time available for clearing the level.

### Functionalities as a list
User can...
* Read the instructions for the game
* Choose their team members
* Choose the difficulty level of the game (0 or 1 to begin with)
* Set a name for themselves
* Turn around two cards at the same time by selecting the card with a press of a mouse

The game will...
* Assign a default name for the player (if not inserted by the player)
* Select a default team and difficulty level (if not chosen by be player)
* Allow moving between screen with dedicated buttons (same menu structure on every page (buttons for Intro, Options, Start and Exit))
* Show the level that is being played
* Count down available time to clear the level 
* Show the team members still alive
* Remove cards from the table when a correct pair is identified
* Count and show points collected (player get points from identifying the correct pairs of cards)
* Show the number of cards that will eliminate participants per level
* Eliminate a team member if a card with "Sudden Death" item is opened

## Future Development Improvement Ideas
* Improve visuals/graphics of the game (background pictures, special effects in cases of success and "Sudden death")
* Allow characteristics for the team members (e.g. no elimination even in the case of "Sudden death" cards)
* Player chooses who is the one "guessing" the card and in case of "Sudden death" who from the team is eliminated
* Number of levels to be cleared (2 upwards), variation in the levels (number of cards to be turned, hints given in cards (e.g. katakana in one card and roomaji in another without showing both in the same card), increasing number of "Sudden death" cards, introducing "New Team member" cards)

## Limitations to be Considered

* Application needs to run on Linux, Windows and OSX desktop computers
* Data is stored on the user's computer
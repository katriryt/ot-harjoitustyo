# Description of the Application Architecture

## Structure

Application has three layers: presentation tier (UI), logic tier (services), and data tier (storage of data). Code is packaged as follows:

![Package structure](./pictures/architecture_package.png)

_ui_, _services_, and _repositories_ packages include the code for the user interface, game logic, and long-term storage and handling of data, respectively. 

Note: Implementation is work in progress. Significant development and restructuring of especially the UI and data tier has been done. Services layer requires finalization.

## User Interface (UI)

User interface has six different views (of which four have been implemented): 

- Opening view
- Introduction view
- Options view
- Game view
- Success view, and
- Failure view

Each of the views is implemented as their own class. Only one of the views is visible at any given point of time. 

Note: GameView is currently divided in two classes (GameView and PlayGameInteractions, which are to be combined).

[UI](../src/ui/ui.py) class is responsible for showing each of the view. UI class also includes the common functionalities for all the views (e.g. common buttons for moving between different views). Each of the views is drawn on a dedicated frame within the overall UI. 

User interface is intended to be separate from the game logic. UI related classes call on methods from the [PlayerDatabaseInteraction](../src/repositories/playerdatabaseinteraction.py), [KatakanaDatabaseInteraction](../src/repositories/katakanadatabaseinteraction.py), and [PlayGame](../src/services/playgame.py) classes (especially last one work in progress).

The most important UI classes are the following ones. 

In the [OptionsView](../src/ui/optionsview.py), the player sets the basic variables for the game to be played. Class offers, e.g., the following core functionalities:
- '_choose_name_for_game(self)'
- '_check_if_name_ok(self, proposed_name)'
- '_generate_level_buttons(self)'
- '_select_game_level(self, selected_game_level_button)'
- '_update_current_game_optios(self)'

In the [PlayGameInteractions](../src/ui/playgameinteractionsview.py), the player interacts with the game, flipping cards and collecting points. Class offers, e.g., the following core functionalities: 
- '_draw_game_view(self)'
- '_set_up_game_board(self)'
- '_card_pressed(self, input_button_number)'

## Game Logic

Game logic is work in progress. Class [PlayGame](../src/services/playgame.py) is to include the activities that will result from player interacting with the game, e.g. increasing points, reducing lives, losing/winning the game, and saving final results to the player database.

The full game logic is descibed below (based on current level of implementation): 

![ArchitecturePackageClasses](./pictures/architecture_package_classes.png)

## Long Term Storage of Data

First purpose of the classes in repositories is to create and store the data used by the application in the long term. Second task is to provide access to the data in the databases.

### Creating databases and storing data

There are two classes for the storage of data. [KatakanaDatabaseUtilities](../src/repositories/katakanadatabaseutilities.py) creates access to the Katakana database (SQLite database) and populates the database with katakanas used in the game. Database also stores specifications for the different levels of the game (e.g. number of cards and types of katakanas to be learnt). 

[PlayerDatabaseUtilities](../src/repositories/playerdatabaseutilities.py) sets up and creates access to the Player database (SQLite database). Player database includes all the players in the game and their data (e.g. points collected, game levels reached). Player database also stores specifications for the game that is currently played (e.g. name of the player, level being played). 

Both of these databases are initialized at the start of the game. 
Configuration file has not yet been developed.

### Getting data from the databases

There are two classes that provide access to the databases for the _ui_ and _services_. _ui_ and _services_ classes do not directly interact with the database. 

[KatakanaDatabaseInteraction](../src/repositories/katakanadatabaseinteraction.py), provides, e.g., the following services: 
- '_get_game_specs(self, level)'
- '_get_cards_for_game_board(self, level)'

[PlayerDatabaseInteraction](../src/repositories/playerdatabaseinteraction.py), provides, e.g., the following services: 
- '_create_new_player(self, given_name)'
- '_check_player_exists(self, given_name)'
- '_get_current_game_specs(self)'

## Main Functionalities

Here are selected sequence diagrams of the application's key functionalities

### Creation of a new player

One of the key functionalities in the game is the creation of a new player.

When the user has opened the game and entered the Options view by pressing _Options_ button in the UI, the user is presented with a drop-down menu of previously used player names from which to select. The user can also type in a new name and press _Enter_ after which a new player is created and the statistics for this new user are printed on the screen.

The following sequence diagrams shows how the information flows during this process (hand drawn version as the second, updated draft). For the sake of simplicity, only the case, where the name is acceptable and a new player can be created, is presented.

![SequenceDiagramNewPlayer](./pictures/sequence_diag_new_player_3.png)

### Other Functionalities

To be defined.

## Development Areas in the Application Structure

### User Interface

Visuals to be improved in all views.

### Game Logic

Game logic to be finalized.

### Repositories

Data layers to be expanded and finalized.
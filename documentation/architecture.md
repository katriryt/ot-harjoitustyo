# Description of the Application Architecture

## Structure

Application has three layers: presentation tier (UI), logic tier (services, entities), and data tier (storage of data). Code is packaged as follows: 

![Package structure](./pictures/architecture_package.png)

_ui_, _services_, _entities_, and _repositories_ packages include the code for the user interface, game logic, classes using data structures (e.g. player functionalities), and long-term storage of data, respectively.

Note: Implementation of the data tier, i.e. repositories package, is yet to be done, as well as creation of links in code between services and entities and repositories and entities packages.

## User Interface (UI)

User interface has six different views (of which four have been implemented): 

- Opening view
- Introduction view
- Options view
- Game view
- Success view, and
- Failure view

Each of the views is implemented as their own class. Only one of the views is visible at any given point of time. 

[UI](../src/ui/ui.py) class is responsible for showing each of the view. UI class also includes  the common functionalities for all the views (e.g. common buttons for moving between different views). Each of the views is drawn on a dedicated frame within the overall UI. 

User interface is intended to be separate from the game logic. UI related classes call on methods from the [PlayGame](../src/services/playgame.py) class, which will class the other classes (work in progress).

## Game Logic

Game logic is work in progress. 

At the moment, the core game logic had been developed in [PlayGame](../src/services/playgame.py) class. Class offers core functoinalities to play the memory game, such as
- '_set_up_game_board(self)'
- '_generate_game_list(self, wanted_pairs, wanted_sudden_deaths)'
- '_card_pressed(self, input_button_number)'
- '_game_over(self, message)'

Regarding the core ways to use Player's individual data, [Player](../src/entities/player.py) class sets up a new user and provides services to keep track of the player's key characteristics (e.g. name, points, team). Class is yet to be linked with the other classes. 

The full game logic, which starts from the _PlayGame_ class is descibed below (based on current level of implementation): 

![Package structure and classes](./pictures/architecture_package_classes.png)

## Long Term Storage of Data

Functionalities yet to be developed. 

### Files

To be defined. 

### Main Functionalities

To be defined. 

### Other Functionalities

To be defined.


## Development Areas in the Application Structure 

### User Interface

Visuals to be improved in all views. 

### Game Logic

Game logic to be finalized. 

### Repositories

Data layers to be developed.
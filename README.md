# Katakana no Geemu - Sudden Death

Purpose of the **Katakana no Geemu - Sudden Death** is to learn to read Japanese katakana symbols quickly in a fun and interactive way. 

Katakana is one of the three Japanese syllabary, along with hiragana and kanji (and in some cases the Latin script (known as roomaji)). 

The game is a modified version of a basic memory game (find the pairs game). The player needs to pick two cards with the same symbol from a set of turned over cards. There are a few "Sudden death" cards included in the set of cards, which cause the player to lose lives. There is also a timer, so the puzzle needs to be solved within a time limit. As levels become more difficult, time is reduced, number of cards and "Sudden death" cards is increased.

## Documentation

- [PreliminaryGameDesignDocument](/documentation/game_design_doc.md)
- [PreliminaryArchitureDescription](/documentation/architecture.md)
- [TimeSheet](/documentation/tyoaikakirjanpito.pdf)

## Installation

Install dependencies with the following command:

```bash
poetry install
```

Make the necessary initialization operations with the following command: 

```bash
poetry run invoke build
```

Start the application with the following command: 

```bash
poetry run invoke start
```

## Release

Get the first [release](TO BE ADDED) of the game. 

## Commands on the command line

Please see the relevant commands below.

### Running the application

The application can be started with the following command:

```bash
poetry run invoke start
```

### Testing

Tests can be run with the following command: 

```bash
poetry run invoke test
```

### Test coverage

An HTML-format test coverage report can be generated with the following command:

```bash
poetry run invoke coverage-report
```

The report is generated in the _htmlcov_ folder.

### Pylint

Checks as defined by .pylintrc can be implemented with the following command: 
```bash
poetry run invoke lint
```

### autopep8 formatting

Formats code according to pep8 standard: 
```bash
poetry run invoke format
```


Updated 25.4.2021

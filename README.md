# Katakana no Geemu - Sudden Death

Purpose of the **Katakana no Geemu - Sudden Death** is to learn to read Japanese katakana symbols quickly in a fun and interactive way. 

Katakana is one of the three Japanese syllabary, along with hiragana and kanji (and in some cases the Latin script (known as roomaji)). 

The game is a modified version of a basic memory game (find the pairs game). The player needs to pick two cards with the same symbol from a set of turned over cards. There may be a few "Sudden death" cards included in the set of cards, which cause the player to lose team members (lives). As levels become more difficult, katakana characters become more difficult, and the number of cards and "Sudden death" cards is increased.

## Documentation

- [Instructions](/documentation/preliminary_instructions.md)
- [GameDesignDocument](/documentation/game_design_doc.md)
- [ArchitureDescription](/documentation/architecture.md)
- [TestingDocument](/documentation/testing_document.md)
- [TimeSheet](/documentation/tyoaikakirjanpito.pdf)

## Installation

Install dependencies with the following command:

```bash
poetry install
```

Note: if you are running the program on Ubuntu, you may need to install Japanese fonts with the following command: 

```bash
sudo apt install fonts-takao-mincho
```

Start the application with the following command: 

```bash
poetry run invoke start
```

## Release

Get the latest [release](https://github.com/katriryt/ot-harjoitustyo/releases/tag/viikko7) of the game. 

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


Updated 16.5.2021

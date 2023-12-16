# Hangman

Hangman is a terminal game written in Python, and it runs in the Code Institute mock terminal on Heroku.

## Table of Contents


## How To Play

The player must guess letters in an attempt to discover a hidden word. For each letter they guess correctly, it appears in the word once for every occurrence of that letter. If the letter is not in the word, the player loses one of their lives, and has to guess another letter. The game ends when either the player has guessed the full word, in which case they win, or they run out of lives, in which case they lose.

## User Experience

### Project Goals

This project was created as the third Project Portfolio project for the Code Institute Diploma in Full Stack Software Development, to demonstrate the usage of Python by building a command-line application that interacts with a data model (in this case the GameData class, which stores data on the currently chosen word, progress in the game, number of lives remaining, and previous wins and losses), and queries and manipulates data from that model (e.g. adding guesses from the player, thus increasing the progress or losing a life, requesting the letters revealed so far, the guessed letters and the number of lives to display to the player).

In addition to being a solution to this assignment, the game of hangman, which this project implements in the form of a terminal game, is a popular game among a wide range of audiences. Hangman is a popular alphabetic guessing game in schools, and is also used among non-native English speakers as a way of practicing spelling of new words when learning English, making the game both a fun guessing game, as well as an educational tool for spelling and learning vocabulary. Hangman has even made its way into the world of TV, with the popular American game show "Wheel of Fortune" being inspired by hangman, with the same premise of guessing letters to spell out a word or phrase, in this case with a specific theme given for the word/phrase to be guessed.

### User Stories

- As a user, I want it to be clear what this application does.
- As a user, I want to be able to view the rules of the game.
- As a user, I want to be able to play the game when I'm ready.
- As a user, I want to be able to select a theme for the word I must guess.
- As a user, I want to see how many letters are in the word I must guess.
- As a user, I want to see how many lives I have in the game.
- As a user, I want to see if my guess was right or wrong.
- As a user, I want to see what letters I have already guessed.
- As a user, I want to see any letters I have guessed correctly display in the word.
- As a user, I want to know when I have won the game.
- As a user, I want to know when I have lost the game.
- As a user, I want to have the option to play again after winning or losing without starting the application again.
- As a user, I want to view my stats to see how often I have won and lost, and my current winning streak and win ratio.

### Design

## Features

### Theme Selection

The user can select from one of four themes, animals, foods, colours and instruments. Each of these options will start the game with a word related to one of those categories from the corresponding word list.

### Rules

### Stats

### Lives Display

### Word Progress Display

### Guessed Letters Display

### Future Features

## Technologies Used

- Languages used:
 - Python - used to create the hangman game
- Libraries used:
 - Random - a Python library used for random number generation and choosing randomly from lists. This library was needed to choose a random word from the word list corresponding to the theme selected by the user to display for the game.
- Programs used:
 - Git - used for version control
 - GitHub - used to store files for project
 - Heroku - used to deploy project 

## Testing

### Manual Testing
Tested:
Guessing letters is case-insensitive, all guesses will automatically be made lowercase in the code
Guessing right reveals a letter
Guessing wrong removes 1 life and shows no new letters
Guessing the same letter twice alerts the user, asks them to choose again, doesn't remove a life
Guessing a non-letter, i.e. numbers, punctuation, other symbols like &, $ or %, alerts the user, asks them to choose again, doesn't remove a life
Guessing a non-English letter like "é" or "ó" alerts the user, asks them to choose again, doesn't remove a life
Guessing all letters of the word results in a win and tells you what the word is
Running out of lives results in a loss and tells you what the word was
Both winning and losing allow you play again
Selecting yes takes you back to the start of the game with a new randomized word
Selecting no takes you back to the main menu
In the main menu and theme selection menu, all options are case insensitive
In the main menu:
 - Selecting P for Play will take you to the theme selection menu to choose what level you want to play
 - Selecting R for Rules will show you the rules of the game
 - Selecting S for Stats will show you your stats, i.e. your total wins, total losses, current win streak, and win ratio
 - Selecting Q for Quit will end the game
In the theme selection menu:
 - Selecting A for Animals will select a word from the animals word list
 - Selecting F for Food will select a word from the food word list
 - Selecting C for Colours will select a word from the colours word list
 - Selecting I for Instruments will select a word from the instruments word list
In the stats menu:
 - If no games have been played, win ratio is 0, and a message is shown to the player to explain they have played no games so there are no wins (this is to avoid division by zero when calculating the ratio)

### Fixed Bugs
- The wins, losses, win streak and win ratio were not displaying correctly, all displaying as 0 even after playing multiple games. This was because the class variables were not being accessed correctly (using instance variable instead of class name). This is now fixed, and the numbers are all displaying correctly.

### Unfixed Bugs
- No unfixed bugs have been found to remain in this project.

## Deployment

## Credits
The template used to create this project is from Code Institute.
All code added to the file "run.py" for this project, and all content in this Readme file, both of those are entirely of my own creation.

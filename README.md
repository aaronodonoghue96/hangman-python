# Hangman

Hangman is a terminal game written in Python, and it runs in the Code Institute mock terminal on Heroku.

The player must guess letters in an attempt to discover a hidden word. For each letter they guess correctly, it appears in the word once for every occurrence of that letter. If the letter is not in the word, the player loses one of their lives, and has to guess another letter. The game ends when either the player has guessed the full word, in which case they win, or they run out of lives, in which case they lose.

This project was created as the third Project Portfolio project for the Code Institute Diploma in Full Stack Software Development, to demonstrate the usage of Python by building a command-line application that interacts with a data model (in this case the GameData class, which stores data on the currently chosen word, progress in the game, number of lives remaining, and previous wins and losses), and queries and manipulates data from that model (e.g. adding guesses from the player, thus increasing the progress or losing a life, requesting the letters revealed so far, the guessed letters and the number of lives to display to the player).

In addition to being a solution to this assignment, the game of hangman, which this project implements in the form of a terminal game, is a popular game among a wide range of audiences. Hangman is a popular alphabetic guessing game in schools, and is also used among non-native English speakers as a way of practicing spelling of new words when learning English, making the game both a fun guessing game, as well as an educational tool for spelling and learning vocabulary. Hangman has even made its way into the world of TV, with the popular American game show "Wheel of Fortune" being inspired by hangman, with the same premise of guessing letters to spell out a word or phrase, in this case with a specific theme given for the word/phrase to be guessed.

## Table of Contents


## How To Play

## User Experience

### User Stories

### Design

## Features

### Theme Selection

### Rules

### Stats

### Lives Display

### Word Progress Display

### Guessed Letters Display

### Future Features

## Technologies Used

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

# Hangman

Hangman is a terminal game written in Python, and it runs in the Code Institute mock terminal on Heroku.

The player must guess letters in an attempt to discover a hidden word. For each letter they guess correctly, it appears in the word once for every occurrence of that letter. If the letter is not in the word, the player loses one of their lives, and has to guess another letter. The game ends when either the player has guessed the full word, in which case they win, or they run out of lives, in which case they lose.

## Table of Contents


## How To Play

## Features

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
In the main menu and difficulty selection menu, all options are case insensitive
In the main menu:
 - Selecting P for Play will take you to the difficulty selection menu to choose what level you want to play
 - Selecting R for Rules will show you the rules of the game
 - Selecting S for Stats will show you your stats, i.e. your total wins, total losses, current win streak, and win ratio
 - Selecting Q for Quit will end the game
In the difficulty selection menu:
 - Selecting E for Easy will select a word from the easy word list
 - Selecting M for Medium will select a word from the medium word list
 - Selecting H for Hard will select a word from the hard word list
 - Selecting I for Impossible will select a word from the impossible word list

## Deployment

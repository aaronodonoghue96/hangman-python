# Hangman

Hangman is a terminal game written in Python, and it runs in the Code Institute mock terminal on Heroku.

## Table of Contents
- [How To Play](#how-to-play)
- [User Experience](#user-experience)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
- [Features](#features)
  - [Main Menu](#main-menu)
  - [Theme Selection](#theme-selection)
  - [Back](#back)
  - [Rules](#rules)
  - [Stats](#stats)
  - [Quit](#quit)
  - [Timer](#timer)
  - [Lives Display](#lives-display)
  - [Word Progress Display](#word-progress-display)
  - [Guessed Letters Display](#guessed-letters-display)
  - [Validation](#validation)
  - [Future Features](#future-features)  
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## How To Play

The player must guess letters in an attempt to discover a hidden word. For each letter they guess correctly, it appears in the word once for every occurrence of that letter. If the letter is not in the word, the player loses one of their lives, and has to guess another letter. The game ends when either the player has guessed the full word, in which case they win, or they run out of lives, in which case they lose.

## User Experience

### Project Goals

This project was created as the third Project Portfolio project for the Code Institute Diploma in Full Stack Software Development, to demonstrate the usage of Python by building a command-line application that interacts with a data model (in this case the GameData class, which stores data on the currently chosen word, progress in the game, number of lives remaining, and previous wins and losses), and queries and manipulates data from that model (e.g. adding guesses from the player, thus increasing the progress or losing a life, requesting the letters revealed so far, the guessed letters and the number of lives to display to the player).

In addition to being a solution to this assignment, the game of hangman, which this project implements in the form of a terminal game, is a popular game among a wide range of audiences. Hangman is a popular alphabetic guessing game in schools, and is also used among non-native English speakers as a way of practicing spelling of new words when learning English, making the game both a fun guessing game, as well as an educational tool for spelling and learning vocabulary. Hangman has even made its way into the world of TV, with the popular American game show "Wheel of Fortune" being inspired by hangman, with the same premise of guessing letters to spell out a word or phrase, in this case with a specific theme given for the word/phrase to be guessed.

### User Stories

| User Story | Acceptance Criteria |
| --- | --- |
| As a user, I want it to be clear what this application does. | It is immediately evident to the user that the application is a hangman game. |
| As a user, I want to be able to view the rules of the game. | The user is able to view the rules of the game by entering R at the main menu. |
| As a user, I want to be able to play the game when I'm ready. | The user is able to play the game by entering P at the main menu. |
| As a user, I want to be able to select a theme for the word I must guess. | The user is able to select a theme using one of the options provided. |
| As a user, I want to be able to go back to the main menu from the theme selection screen. | The user is able to return to the main menu by entering X. |
| As a user, I want to see how many letters are in the word I must guess. | The user is shown the length of the target word in underscores at the start of the game. |
| As a user, I want to see how many lives I have in the game. | The player is shown how many lives they have at each turn. |
| As a user, I want to see if my guess was right or wrong. | The user is shown their guess is right by the letter appearing in the word, or wrong by losing a life. |
| As a user, I want to see what letters I have already guessed. | The user is shown what letters have already been guessed on each turn. |
| As a user, I want to see any letters I have guessed correctly display in the word. | The user is shown all correctly guessed letters in the word so far at each turn. |
| As a user, I want to know when I have won the game. | The user is shown a message to indicate they have won upon guessing the full word. |
| As a user, I want to know when I have lost the game. | The user is shown a message to indicate they have lost upon losing their last life. |
| As a user, I want to have the option to play again after winning or losing without starting the application again. | The user is given the option to play again after each game ends, returning to the theme selection screen in case they want to choose a different theme this time. |
| As a user, I want to view my stats to see how often I have won and lost, and my current winning streak and win ratio. | The user is able to view their stats from the main menu by entering S. |

### Design

Flowchart will go here

## Features

Screenshots of each feature to show project outcomes will go here

### Main Menu

The user sees the main menu upon starting the application, and from there, has the options to play, see the rules, see their stats, or quit.

### Theme Selection

Once the user has selected Play from the main menu by entering P and pressing Enter, they can select from one of four themes, animals, foods, colours and instruments by entering the first letter of the category followed by Enter. Each of these options will start the game with a word related to one of those categories from the corresponding word list.

### Back

The user can go back to the main menu if they are in the theme selection menu by pressing X and Enter.

### Rules

The user can view the rules of the game from the main menu by pressing R and Enter.

### Stats

The user can view their stats, i.e. wins, losses, current winning streak, and win ratio, from the main menu by pressing S and Enter.

### Quit

The user can quit the application by pressing Q and Enter in the main menu.

### Lives Display

The user is shown the number of lives they have remaining before every turn.

### Word Progress Display

The user is shown how much of the word they have filled in, and how much of the word is left, before every turn.

### Guessed Letters Display

The user is shown which letters they have already guessed before every turn.

### Validation

The user's choices are validated at several points in the game. All menus have a limited set of valid options, so entering anything outside of those, or entering nothing at all, will prompt the user to enter a valid option. The user's guesses in the hangman game are also validated, to ensure that only letters of the English alphabet that have not already been guessed will be counted, and notify the user if they enter anything else (e.g. numbers, punctuation, foreign letters, symbols, whitespace, or even nothing at all).

### Future Features

In future versions of this application, I would like to add:
- More themes as options.
- Difficulty levels for each theme.
- Multi-word phrases (and thus add logic for dealing with spaces and punctuation like apostrophes when such cases arise)
- The option for multiplayer.
- A new game mode based on the gameshow Wheel of Fortune, where rather than lives, the player(s) will instead aim to build up their score by guessing letters, with a randomly chosen number chosen by the wheel on each turn as the value for a correct guess, and correct guesses earning that number of points multiplied by the amount of the letter in the word, and wrong guesses ending the player's turn.

## Technologies Used

- Languages used:
  - Python - used to create the hangman game
  - Node.js - used in the template from Code Institute to create the Python terminal on Heroku
- Libraries used:
  - Random - a Python library used for random number generation and choosing randomly from lists. This library was needed to choose a random word from the word list corresponding to the theme selected by the user to display for the game.
- Programs used:
  - Git - used for version control
  - GitHub - used to store files for project
  - Heroku - used to deploy project
- Other technologies used:
  - JSON - used in the template from Code Institute to pass package, launch and settings data

## Testing

### Manual Testing

Tested:

| User Action | Outcome | Pass/Fail |
| --- | --- | --- |
| User enters a capital letter | Guessing letters is case-insensitive, all guesses will automatically be made lowercase in the code. | Pass |
| User guesses correctly | Guessing right reveals a letter. | Pass |
| User guesses incorrectly | Guessing wrong removes 1 life and shows no new letters. | Pass |
| User guesses the same letter twice | Guessing the same letter twice alerts the user, asks them to choose again, doesn't remove a life. | Pass |
| User guesses a non-letter | Guessing a non-letter, i.e. numbers, punctuation, other symbols like &, $ or %, alerts the user, asks them to choose again, doesn't remove a life. | Pass |
| User guesses a non-English letter | Guessing a non-English letter like "é" or "ó" alerts the user, asks them to choose again, doesn't remove a life. | Pass |
| User guesses nothing or whitespace | Guessing nothing, or any amount of whitespace, alerts the user, asking them to enter a letter, doesn't remove a life. | Pass |
| User guesses a letter but adds whitespace | All whitespace is removed and it is treated as if the user just guessed the letter on its own | Pass |
| User guesses more than one letter at a time | Guessing more than one letter at a time alerts the user, asking them to enter one letter at a time. | Pass |
| User finishes the word | Guessing all letters of the word results in a win and tells you what the word is. | Pass |
| User runs out of lives | Running out of lives results in a loss and tells you what the word was. | Pass |
| User wins or loses the game | Both winning and losing allow you play again. | Pass |
| User selects yes for the play again prompt | Selecting yes takes you back to the theme selection screen to choose a theme for the next game. | Pass |
| User selects no for the play again prompt | Selecting no takes you back to the main menu. | Pass |
| User enters a value other than Y or N for play again (or no value) | Selecting an invalid option (or no option) will prompt you for a yes/no response. | Pass |
| User enters a lowercase letter as an option in a menu | In the main menu and theme selection menu, all options are case insensitive, the expected actions will occur regardless of the inputted letter's case. | Pass |
| User selects P in the main menu | Selecting P for Play will take you to the theme selection menu to choose what level you want to play. | Pass |
| User selects R in the main menu | Selecting R for Rules will show you the rules of the game. | Pass |
| User selects S in the main menu | Selecting S for Stats will show you your stats, i.e. your total wins, total losses, current win streak, and win ratio. | Pass |
| User selects Q in the main menu | Selecting Q for Quit will end the game. | Pass |
| User selects A in the theme selection menu | Selecting A for Animals will select a word from the animals word list. | Pass |
| User selects F in the theme selection menu | Selecting F for Food will select a word from the food word list. | Pass |
| User selects C in the theme selection menu | Selecting C for Colours will select a word from the colours word list. | Pass |
| User selects I in the theme selection menu | Selecting I for Instruments will select a word from the instruments word list. | Pass |
| User views Stats before playing any games | If no games have been played, win ratio is 0, and a message is shown to the player to explain they have played no games so there are no wins (this is to avoid division by zero when calculating the ratio). | Pass |

### Validator Testing

- PEP8
   - I validated the entire contents of run.py on https://pep8ci.herokuapp.com/ and no errors were found.

### Fixed Bugs

- The wins, losses, win streak and win ratio were not displaying correctly, all displaying as 0 even after playing multiple games. This was because the class variables were not being accessed correctly (using instance variable instead of class name). This is now fixed, and the numbers are all displaying correctly.
- Selecting an invalid value in the theme selection menu returned the user to the main menu rather than the theme selection menu. This has now been fixed by putting the input and validation into a while loop to keep going until valid input is entered.

### Unfixed Bugs

- No unfixed bugs have been found to remain in this project.

## Deployment

This site is deployed using Heroku. In order to deploy to Heroku, you will need a Heroku account, a requirements.txt file, and a Procfile.

The requirements.txt file will contain all dependencies required for the project. Since my app only used the Random library, which is built into Python, I did not have any dependencies, and so my requirements.txt file was empty.

The Procfile will tell Heroku which files run the program and how to run it. Because this program uses the Python terminal, which is created using Node.js, the first file that will be run is index.js, to start up the terminal. As a result, the Procfile should have only the text "web: node index.js" in it.

Make sure of the following, so that the deployment will run correctly:
- Procfile is spelled with a capital P, and has no file extension.
- There is no blank line at the bottom of the Procfile.

Once that is done, login to Heroku, or create a new account if you don't already have one. Once you have logged in, click the New button in the top-right corner, and select "Create New App".

You will then be asked to name your app, and the name must be unique so you can't use the exact same name as the GitHub repository (I used "pp3-hangman-python" as "hangman-python" was already taken by the GitHub repository). You must then select a region, the available options being United States or Europe. Once you have done both, click "Create App" at the bottom.

You should now have the Deploy tab open, if not, select it. Once you are in the Deploy tab, select GitHub in the "Deployment method" row to deploy from GitHub. In the textbox below, enter the name of the repository you want to connect, click the Search button, and select the repository you want from the results below.

Once the repository is connected, go to the Settings tab, and go to the Buildpacks section. Make sure that there are buildpacks for both Python and Node.js there, and that Python is first. If one or both is missing, add them using the "Add buildpack" button.

If there are any config variables required for the app, add these in the Config Vars section by choosing Reveal Config Vars and then entering the key and value and pressing the Add button for each variable. I did not require any config variables for my application, so I left this empty.

Go back to the Deploy tab, and click either Enable Automatic Deploys, or Deploy Branch if you want to deploy manually. Once the branch is successfully deployed, you can click View at the bottom, or Open App at the top, and either of those will open up the Python hangman app in a new tab.

## Credits

The template used to create this project is from Code Institute, all files except for run.py and README.md are made entirely of content from Code Institute.
All code added to the file "run.py" for this project, and all content in this Readme file, both of those are entirely of my own creation.

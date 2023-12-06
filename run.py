from random import choice

class GameData():

    #Initialize the game data:
    #The answer is the chosen word from the word list
    #Progress starts with an underscore for each letter of the owrd
    #As none of the letters have been filled in yet
    #None of the letters are guessed yet so that is an empty list

    def __init__(self, word):
        self.answer = word
        self.progress = ''.join('_' for i in word)
        self.guessed = []

    def add_guess(self, letter):
        self.guessed += letter

        # Validation against numbers, punctuation, other non-alpha characters
        if letter.isalpha() is False:
            print(f"{letter} is not a letter.\n \
                    Please choose a letter in the English alphabet.")
            return
        # Validation against guessing the same letter twice
        elif letter in self.guessed:
            print(f"You have already guessed the letter {letter}")
            return

        if letter not in self.answer:
            self.lives -= 1

class Hangman():

    #List of words to choose from for the game
    words = ["absurd", "avenue", "bagpipes", "blizzard", "buffalo",
             "cryptic", "dizzy", "duplex", "embezzle", "equip",
             "faking", "fixable", "fjord", "flapjack", "galaxy",
             "galvanize", "gizmo", "hazard", "hyphen", "icebox",
             "injury", "jackpot", "jaywalking", "jigsaw", "joking",
             "jukebox", "keyhole", "kiosk", "lengths", "luxury",
             "matrix", "megahertz", "microwave", "mystery", "nightclub",
             "onyx", "oxidize", "oxygen", "polka", "psychic",
             "puzzle", "quartz", "quizzical", "rhubarb", "rickshaw",
             "scratch", "skiving", "snazzy", "sphinx", "stretch",
             "subway", "swivel", "syndrome", "topaz", "transgress",
             "transplant", "twelfth", "unknown", "uptown", "vixen",
             "vortex", "waltz", "wizard", "zephyr", "zigzag",
             "zodiac", "zombie"]

    #Pick a word at random from the list
    chosen_word = choice(words);

    game_data = GameData(chosen_word)

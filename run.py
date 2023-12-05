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

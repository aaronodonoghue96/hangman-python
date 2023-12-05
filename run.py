from random import choice

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
    chosen_word = random.choice(words);


class GameData():

    pass

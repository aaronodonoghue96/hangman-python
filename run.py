from random import choice

class GameData():

    # Alphabet for checking inputs against to ensure they are English letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #Initialize the game data:
    #The answer is the chosen word from the word list
    #Progress starts with an underscore for each letter of the owrd
    #As none of the letters have been filled in yet
    #None of the letters are guessed yet so that is an empty list

    def __init__(self, word):
        self.answer = word
        self.progress = ''.join('_' for i in word)
        self.guessed = []

    # Show the progress the player has made on guessing the word
    # by filling in every letter in the word they guessed correctly
    # while hiding the rest by leaving them blank
    def show_word_progress(self):
        progress = ''
        for i in self.answer:
            if i in self.guessed:
                progress += i
            else:
                progress += '_'
        return progress

    def add_guess(self, letter):
        # Remove any whitespace from the guess, and make it case-insensitive
        guess = letter.lower().strip()
        # Validation against empty input such as whitespace or nothing at all
        if len(guess) == 0:
            print("Please enter a letter.")
            return
        # Validation against numbers, punctuation, other non-alpha characters
        if guess.isalpha() is False:
            print(f"{guess} is not a letter.\n \
                    Please choose a letter in the English alphabet.")
            return
        # Validation against non-English letters such as é
        elif guess not in self.alphabet:
            print(f"{guess} is not in the English alphabet.\n \
                    Please choose a letter in the English alphabet.")
            return
        # Validation against guessing the same letter twice
        elif guess in self.guessed:
            print(f"You have already guessed the letter {guess}")
            return

        self.guessed += guess

        if guess not in self.answer:
            self.lives -= 1

class Hangman():

    play_again = True

    while play_again is True:
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

        # Provide either the singular "life" or plural "lives"
        # based on how many lives the player has left
        life_or_lives = "life" if game_data.lives == 1 else "lives"

        while True:
            print(f"{game_data.lives} {life_or_lives} remaining")
            print(f"You have guessed: {game_data.guessed}")
            print(f"Word: {game_data.show_word_progress()}")
            letter = input("Guess a letter: ").lower()
            game_data.add_guess(letter)

            if game_data.show_word_progress() == game_data.answer:
                print(f"You win! The word was {game_data.answer}")
                break

            if game_data.lives == 0:
                print(f"Game Over. The word was {game_data.answer}")
                break

        play_again_choice = ""

        while play_again_choice.lower() not in ['y', 'n']:
            play_again_choice = input("Play again? (y/n)")
            if play_again_choice.lower() == "n":
                play_again = False
            elif play_again_choice.lower() == "y":
                play_again = True
            else:
                print("Please select y for yes or n for no")

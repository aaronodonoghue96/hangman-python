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
        valid = True
        guess = letter.lower().strip()
        # If the validation fails, print the error message and return
        if not validate_empty(guess):
            print("Please enter a letter.")
            valid = False
        elif not validate_letter(guess):
            print(f"{guess} is not a letter.\n \
                    Please choose a letter in the English alphabet.")
            valid = False
        elif not validate_english(guess):
            print(f"{guess} is not in the English alphabet.\n \
                    Please choose a letter in the English alphabet.")
            valid = False
        elif not validate_duplicate(guess):
            print(f"You have already guessed the letter {guess}")
            valid = False

        if valid:
            self.guessed += guess

            if guess not in self.answer:
                self.lives -= 1

    # Validation against empty input such as whitespace or nothing at all
    def validate_empty(self, guess):
        return len(guess) != 0:

    # Validation against numbers, punctuation, other non-alpha characters
    def validate_letter(self, guess):
        return guess.isalpha()

    def validate_english(self, guess):
        return guess not in alphabet

    def validate_duplicate(self, guess):
        return guess not in self.guessed

class Hangman():

    def __init__(self):
        self.game_loop()

    def populate_wordlist(self):
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
        return words

    def game_loop(self):
        replay = True

        while replay is True:
            #List of words to choose from for the game
            words = self.populate_wordlist()

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
                    self.win()
                    break

                if game_data.lives == 0:
                    self.game_over()
                    break

            replay = self.play_again()

    def win(self):
        print(f"You win! The word was {self.game_data.answer}")

    def game_over(self):
        print(f"Game Over. The word was {self.game_data.answer}")

    def play_again(self):
        play_again_choice = ""

        while play_again_choice.lower() not in ['y', 'n']:
            play_again_choice = input("Play again? (y/n)")
            if play_again_choice.lower() == "n":
                return False
            elif play_again_choice.lower() == "y":
                return True
            else:
                print("Please select y for yes or n for no")

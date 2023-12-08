from random import choice


class GameData():

    # Alphabet for checking inputs against to ensure they are English letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    wins = 0
    losses = 0
    win_streak = 0

    # Initialize the game data:
    # The answer is the chosen word from the word list
    # Progress starts with an underscore for each letter of the owrd
    # As none of the letters have been filled in yet
    # None of the letters are guessed yet so that is an empty list

    def __init__(self, word):
        self.answer = word
        self.progress = ''.join('_' for i in word)
        self.guessed = ""
        self.lives = 8

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
        if not self.validate_empty(guess):
            print("Please enter a letter.")
            valid = False
        elif not self.validate_letter(guess):
            print(f"{guess} is not a letter.")
            print("Please choose a letter in the English alphabet.")
            valid = False
        elif not self.validate_english(guess):
            print(f"{guess} is not in the English alphabet.")
            print("Please choose a letter in the English alphabet.")
            valid = False
        elif not self.validate_duplicate(guess):
            print(f"You have already guessed the letter {guess}")
            valid = False

        if valid:
            self.guessed += guess

            if guess not in self.answer:
                self.lives -= 1

    # Validation against empty input such as whitespace or nothing at all
    def validate_empty(self, guess):
        return len(guess) != 0

    # Validation against numbers, punctuation, other non-alpha characters
    def validate_letter(self, guess):
        return guess.isalpha()

    # Validation against non-English letters such as é
    def validate_english(self, guess):
        return guess in self.alphabet

    # Validation against guessing the same letter twice
    def validate_duplicate(self, guess):
        return guess not in self.guessed


class Hangman():

    # Easy words have a lot of the most common letters in English,
    # such as A, E, I, N, O, R, S, and T.
    easy_words = ["answer", "artist", "blaster", "brain", "coaster",
                  "creation", "detain", "drained", "eateries", "eastern",
                  "enter", "falter", "feature", "grains", "greatest",
                  "heater", "honest", "interest", "latest", "leanest",
                  "litter", "master", "minor", "nearest", "notes",
                  "orange", "painter", "points", "rain", "relation",
                  "release", "roasted", "satin", "seat", "snare",
                  "stairs", "strain", "tanner", "trainer", "unease",
                  "user", "various", "vines", "water", "winter", "years"]

    # Medium words use slightly less common letters a bit more often,
    # and are missing some of the more common letters
    medium_words = ["allowed", "apricot", "archer", "austere", "carrot",
                    "dragon", "floating", "fraction", "pressure", "search",
                    "status", "target", "union"]

    # Hard words use more uncommon letters more often than the previous
    # categories
    hard_words = ["afford", "freeze", "major"]

    # Impossible words have a lot of rare letters like J, Q, X and Z,
    # few vowels or Y as a vowel, unusual or long consonant sequences,
    # or few distinct letters meaning fewer chances to guess right
    impossible_words = ["absurd", "avenue", "bagpipes", "blizzard", "buffalo",
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

    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print("Welcome to Hangman!")
        while True:
            option = input("Choose an option: [P]lay, [R]ules,\
[S]tats or [Q]uit ").upper()
            if option == "P":
                self.difficulty_select()
            elif option == "R":
                self.show_rules()
            elif option == "S":
                self.show_stats()
            elif option == "Q":
                break
            else:
                print("Please select a valid option.")

    def difficulty_select(self):
        level = input("Choose a level: [E]asy, [M]edium,\
[H]ard, [I]mpossible ").upper()
        if level == "E":
            self.game_loop("easy")
        elif level == "M":
            self.game_loop("medium")
        elif level == "H":
            self.game_loop("hard")
        elif level == "I":
            self.game_loop("impossible")

    def show_rules(self):
        print("Insert rules of hangman here")

    def show_stats(self):
        wins = GameData.wins
        losses = GameData.losses
        win_streak = GameData.win_streak
        win_ratio = 0 # will stay at 0 if there are no games played
        
        try:
            win_ratio = (wins / (wins + losses)) * 100
        except ZeroDivisionError:
            print("No games were played yet so there are no games won")
            
        print(f"Wins: {wins}, Losses: {losses}, Win Streak: {win_streak}, \
Win Ratio: {win_ratio}")

    def populate_wordlist(self, difficulty):
        if difficulty == "easy":
            return self.easy_words
        elif difficulty == "medium":
            return self.medium_words
        elif difficulty == "hard":
            return self.hard_words
        elif difficulty == "impossible":
            return self.impossible_words

    def game_loop(self, difficulty):
        replay = True

        while replay is True:
            # List of words to choose from for the game
            words = self.populate_wordlist(difficulty)

            # Pick a word at random from the list
            chosen_word = choice(words)

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
                    self.win(game_data)
                    break

                if game_data.lives == 0:
                    self.game_over(game_data)
                    break

            replay = self.play_again()

    def win(self, game_data):
        print(f"You win! The word was {game_data.answer}")
        GameData.wins += 1
        GameData.win_streak += 1

    def game_over(self, game_data):
        print(f"Game Over. The word was {game_data.answer}")
        GameData.losses += 1
        GameData.win_streak = 0

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

# Create a Hangman object, starting the game
Hangman()

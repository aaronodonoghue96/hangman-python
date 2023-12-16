from random import choice
# This library is needed to choose a random word from the chosen theme

class GameData():

    # Alphabet for checking inputs against to ensure they are English letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Stats for wins, losses, and win streak, set to 0 when no games played
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

        # If the validation passes, check if the letter is in the word
        # If not, lose a life, and in any case, mark it as guessed
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

    # Record the victory in the stats and the current win streak
    def win(self):
        print(f"You win! The word was {self.answer}")
        GameData.wins += 1
        GameData.win_streak += 1

    # Record the loss in the stats and reset the current win streak
    def game_over(self):
        print(f"Game Over. The word was {self.answer}")
        GameData.losses += 1
        GameData.win_streak = 0


class Hangman():

    # A list of animal names for the animals theme
    animals_words = ["alligator", "armadillo", "badger", "bear", "beetle",
                    "bird", "cat", "cobra", "cow", "dog", "elephant", "ferret",
                    "fish", "fox", "goat", "horse", "jellyfish", "koala",
                    "lemur", "monkey", "ostrich", "pig", "rabbit", "raccoon",
                    "rhino", "shark", "sheep", "snake", "squid", "squirrel",
                    "tiger", "vole", "vulture", "walrus", "whale", "zebra"]

    # A list of food names for the food theme
    food_words = ["apple", "apricot", "bacon", "banana", "blackberry",
                 "blueberry", "bread", "burger", "cake", "carrot", "cheese",
                 "chicken", "chocolate", "cookie", "croissant", "donut",
                 "egg", "fish", "grapes", "honey", "jelly", "lemon",
                 "lime", "mango", "meat", "orange", "peach", "pear", "pickle",
                 "pizza", "radish", "sandwich", "sausage", "steak", "tomato",
                 "vegetable", "watermelon"]

    # A list of colour names for the colours theme
    colours_words = ["amber", "aqua", "azure", "beige", "black", "blue",
                    "brown", "chartreuse", "copper", "cream", "cyan", "fawn",
                    "fuchsia", "gold", "green", "grey", "hazel", "jade",
                    "khaki", "lime", "magenta", "maroon", "navy", "ochre",
                    "olive", "orange", "peach", "pink", "purple", "red",
                    "silver", "tan", "teal", "turquoise", "violet", "white",
                    "yellow"]

    # A list of musical instrument names for the instruments theme
    instruments_words = ["accordion", "bagpipes", "banjo", "bass", "bassoon",
                        "bongos", "cello", "clarinet", "cymbal", "didgeridoo",
                        "drum", "fiddle", "flute", "glockenspiel", "guitar",
                        "harmonica", "harp", "keyboard", "lyre" "mandolin",
                        "marimba", "melodica", "oboe", "ocarina", "organ",
                        "piano", "recorder", "saxophone", "sitar",
                        "synthesizer", "tambourine", "triangle", "trombone",
                        "trumpet", "tuba", "ukulele", "viola", "violin",
                        "xylophone", "zither"]

    # Upon starting the application, load the main menu
    def __init__(self):
        self.main_menu()

    # Load up the main menu of the game with the four initial options
    def main_menu(self):
        option_text = "Choose an option: [P]lay, [R]ules, [S]tats or [Q]uit\n"
        print("Welcome to Hangman!")
        while True:
            # Select an option by entering the first letter. Invalid
            # letters will result in a prompt to choose a valid option
            option = input(option_text)
            option = option.upper()
            if option == "P":
                self.theme_select()
            elif option == "R":
                self.show_rules()
            elif option == "S":
                self.show_stats()
            elif option == "Q": # Quitting will end the program
                break
            else:
                print("Please select a valid option.")

    # Give the user a selection of themes to choose from, and the option
    # to go back. X is chosen as the "go back" letter as a. It is reminiscent
    # of the use of X as a "cancel" symbol, and b. It is highly unlikely to
    # clash with the initial of any future category
    def theme_select(self):
        level_text = "Choose a theme: [A]nimals, [F]oods, [C]olours, "
        level_text_contd = "[I]nstruments,\n or choose [X] to go back\n"
        while True:
            level = input(level_text + level_text_contd)
            level = level.upper()
            if level == "A":
                self.game_loop("animals")
            elif level == "F":
                self.game_loop("food")
            elif level == "C":
                self.game_loop("colours")
            elif level == "I":
                self.game_loop("instruments")
            elif level == "X":
                break
            else:
                print("Please select a valid option.")

    # Display the rules of the game to the player
    def show_rules(self):
        print("----------RULES----------")
        print("You start the game with 8 lives, and must guess a word.")
        print("You must guess a letter on each turn, if it is correct, every")
        print("occurrence of the letter in the word will appear. Otherwise,")
        print("you will lose a life. If you guess the same letter twice, or")
        print("guess an invalid letter, you will be prompted to try again,")
        print("but won't lose a life. If you run out of lives, you lose the")
        print("game. If you guess the full word, you win. In either case,")
        print("you have the option to play again or return to the main menu")
        print("--------------------")

    # Display the stats to the player on how many wins and losses they have
    # their current win streak, and win ratio
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

    # Populate the wordlist with the words from the specified theme
    def populate_wordlist(self, theme):
        if theme == "animals":
            return self.animals_words
        elif theme == "food":
            return self.food_words
        elif theme == "colours":
            return self.colours_words
        elif theme == "instruments":
            return self.instruments_words

    # Start the game with randomized word from a specified theme
    def game_loop(self, theme):
        replay = True

        # Replay will be false if you decide not to play again at the end
        while replay is True:
            # List of words to choose from for the game
            words = self.populate_wordlist(theme)

            # Pick a word at random from the list
            chosen_word = choice(words)

            game_data = GameData(chosen_word)

            # Provide either the singular "life" or plural "lives"
            # based on how many lives the player has left
            life_or_lives = "life" if game_data.lives == 1 else "lives"

            # While the game is running, display the lives left, guessed
            # letters, word progress so far, and prompt the user to guess
            while True:
                print(f"{game_data.lives} {life_or_lives} remaining")
                print(f"You have guessed: {game_data.guessed}")
                print(f"Word: {game_data.show_word_progress()}")
                letter = input("Guess a letter: ").lower()
                game_data.add_guess(letter)

                # If the guess completes the word, you have won
                if game_data.show_word_progress() == game_data.answer:
                    game_data.win()
                    break

                # If the guess costs you your last life, you have lost
                if game_data.lives == 0:
                    game_data.game_over()
                    break

            # If the user wants to play again, restart the loop, if not,
            # end the loop and return to the main menu
            replay = self.play_again()

    # Offer the player the choice to pkay again or not
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

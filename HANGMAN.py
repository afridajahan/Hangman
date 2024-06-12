import random    #random module is used to randomly select a word from the list
from abc import ABC, abstractmethod     #abc module provides tools for defining abstract base classes in Python

class WordGame(ABC):    #Abstract Base Class that provides a template for word games
    def __init__(self, words, max_guesses=7):
        self._words = words     #List of words for the game.
        self._word = random.choice(self._words).lower()     #The word randomly chosen for the current game.
        self._max_guesses = max_guesses     #Maximum number of wrong guesses allowed.
        self._remaining_guesses = max_guesses      #Number of guesses left.
        self._guessed_letters = set()       #Set of letters that have been guessed.
        self._hidden_word = ['_'] * len(self._word)     #List representing the hidden word, with unguessed letters as underscores

    @abstractmethod
    def guess(self, letter):    #Method to process a guessed letter.
        pass

    @abstractmethod
    def display_board(self):    #Method to display the current state of the game.
        pass

    @abstractmethod
    def is_game_over(self):     #Method to check if the game is over.
        pass

class Hangman(WordGame):    #Sub-class , Inherits from the WordGame class and implements the abstract methods
    def __init__(self, words, max_guesses=7):
        super().__init__(words, max_guesses)

    def guess(self, letter):
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please guess a single letter.")
            return

        letter = letter.lower()
        if letter in self._guessed_letters:
            print(f"You've already guessed '{letter}'. Try again.")
            return

        self._guessed_letters.add(letter)
        if letter in self._word:
            print(f"Good guess: '{letter}' is in the word!")
            for i in range(len(self._word)):
                if self._word[i] == letter:
                    self._hidden_word[i] = letter
        else:
            print(f"Sorry, '{letter}' is not in the word.")
            self._remaining_guesses -= 1

    def display_board(self):
        print("\nCurrent word: " + " ".join(self._hidden_word))
        print(f"Guesses left: {self._remaining_guesses}")
        print(f"Guessed letters: {', '.join(sorted(self._guessed_letters))}")

    def is_game_over(self):
        if '_' not in self._hidden_word:
            print("Congratulations! You've won!")
            return True
        elif self._remaining_guesses == 0:
            print(f"Sorry, you've run out of guesses. The word was '{self._word}'.")
            return True
        return False

# List of words for the game
words = [

    'abstraction', 'algorithm', 'array', 'boolean', 'byte', 'challenge',
    'class', 'code', 'compiler', 'computer', 'conditional', 'data',
    'dictionary', 'encapsulation', 'file', 'float', 'function', 'game',
    'hangman', 'inheritance', 'integer', 'interface', 'library', 'list',
    'loop', 'method', 'module', 'object', 'package', 'player', 'polymorphism',
    'programming', 'project', 'python', 'recursion', 'string', 'structure',
    'syntax', 'variable', 'value' 

]

# Initialize the Hangman game
def play_hangman(words, max_guesses=7):
    game = Hangman(words, max_guesses)

    # Game loop
    while not game.is_game_over():
        game.display_board()
        guess = input("Guess a letter: ").lower()
        game.guess(guess)

    # Display final board
    game.display_board()

# Start the game
if __name__ == "__main__":
    play_hangman(words)

from random_word import RandomWords
from colorama import Fore, Style

# def hangman_game():
scaffold = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Pick a random word
r = RandomWords()
word = r.get_random_word()

# Display word and length for debug purpose
# print(word, len(word))

# Welcome

# Initialize letter guess list and guess variable
letters_guessed = []
incorrect_list = []
incorrect_guesses = 0
max_incorrect_guessess = 5
display_word = '_' * len(word)

# print(word)

while True:
    # Print word with hidden letters
    print('Guess the word:', display_word)
    guess = input("Enter a letter: ")
    # Take care of already guessed letters
    if guess in letters_guessed:
        print(Fore.RED + 'Oops! You already guessed this letter. Enter a new letter to continue.')
        print(Style.RESET_ALL)
    elif guess in incorrect_list:
        print(Fore.RED + 'Oops! You already guessed this letter. Enter a new letter to continue.')
        print(Style.RESET_ALL)
    # Take care of edge case inputs, such as more than one character and integer inputs
    elif len(guess) != 1:
        print("Please enter a single letter to continue\n")
    elif guess.isdigit():
        print("Please enter a letter to continue\n")
    elif guess in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print(Fore.GREEN + 'Good guess!')
        print(Style.RESET_ALL)
        letters_guessed.append(guess)
        display_word = ''
        for i, letter in enumerate(word):
            if letter in letters_guessed:
                display_word += letter
            else:
                display_word += '_'
        appears = word.count(guess)
        remaining_letters = len(word) - len(letters_guessed)
        if '_' not in display_word:
            print(Fore.GREEN + f'Congratulations! You guessed the word: {word}')
            print(Style.RESET_ALL)
            break
        # print('remaining letters', remaining_letters)
    elif guess not in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print(Fore.RED + f'Oops! The letter ({guess}) is not in the word')
        incorrect_guesses += 1
        max_incorrect_guessess -= 1
        incorrect_list.append(guess)
        print("Guesses left: ", max_incorrect_guessess + 1)
        print(scaffold[incorrect_guesses])
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + scaffold[6])
        print("You have no more guesses available. GAME OVER!")
        print(Fore.CYAN + f'The word was: {word}')
        print(Style.RESET_ALL)
        break



# for player_guess in word:
#     if player_guess in word:
#
#
# while the word has not been guessed {
#     Show the player their current progress
#     Get a guess from the player
#     if the player wants to quit the game {
#     Quit the game
#
# } else if the guess is not a single letter {
#     Tell the player to pick a single letter
#
# } else {
#     if the guess belongs to the word {
#     Update the progress
#         }
#     }
# }
# Congratulate the player on guessing the word

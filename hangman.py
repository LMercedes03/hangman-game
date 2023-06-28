from random_word import RandomWords

# def hangman_game():


# Pick a random word
r = RandomWords()
word = r.get_random_word()
print(word)

# Get a guess form user, a single character
guess = ''
incorrect_guesses = 0
max_incorrect_guessess = 6

while True:
    letters_guessed = []
    guess = input("Enter a letter: ")
    if guess in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print(f'Your guess was: {guess}')
        print('Good guess!')
        appears = word.count(guess)
        print('Letter is in word', appears, 'times')
        letters_guessed.append(letters_guessed)
        letters_guessed = ','.join(guess * appears)
        print(letters_guessed)
        remaining_letters = len(word) - len(letters_guessed)
        print('remaining letters', remaining_letters)

    elif guess not in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print('Oops! That letter is not in the word')
        incorrect_guesses += 1
        max_incorrect_guessess -= 1
        print("Guesses left: ", max_incorrect_guessess)
    else:
        print("You have no more guesses available. GAME OVER!")
        break

    print("Please enter a single character to continue\n")

    # for i in range(len(word)):  # replace blanks with correctly guessed letters
    #     if word[i] in correctLetters:
    #         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    #
    # for letter in blanks:  # show the secret word with spaces in between each letter
    #     print(letter, end=' ')
    # print("\n")

# "Guess the word: __________"
# def
# for player_guess in word:
#     if player_guess in word:
#         guess_list.append(player_guess)
#     else:
#         print("Guess not in word. Try again!")
# def guess_checker ():
#
# while

# while the word has not been guessed {
#     Show the player their current progress


# while player_guess != word:
#     print(progress)

#     Get a guess from the player

#     if the player wants to quit the game {
#     Quit the game

# } else if the guess is not a single letter {
#     Tell the player to pick a single letter


# } else {
#     if the guess belongs to the word {
#     Update the progress
#         }

#     }
# }
# Congratulate the player on guessing the word

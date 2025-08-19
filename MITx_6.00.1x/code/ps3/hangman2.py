# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder
# input cases.

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''


    import string
    guess_remaining = 8
    lettersGuessed = []
    ALLOWED = string.ascii_lowercase

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-' * 13)

    while isWordGuessed(secretWord, lettersGuessed) == False and guess_remaining > 0:
        print('You have ' + str(guess_remaining) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess_char = str(raw_input('Please guess a letter: '))
        guess_char = guess_char.lower()

        if guess_char not in ALLOWED or len(guess_char) > 1 or len(guess_char) == 0:
            print('You must enter a valid letter!')
            print('-' * 13)
        elif len(guess_char) == 1 and guess_char in ALLOWED and guess_char not in lettersGuessed:
            lettersGuessed.append(guess_char)
            if guess_char in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                print('-' * 13)
            elif guess_char not in secretWord:
                print('Oops! That letter is not in my word:  ' + str(getGuessedWord(secretWord, lettersGuessed)))
                guess_remaining -= 1
                print('-' * 13)
        elif guess_char in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print('-' * 13)

    if guess_remaining == 0:
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
    elif isWordGuessed(secretWord, lettersGuessed) == True:
        print('Congratulations, you won!')


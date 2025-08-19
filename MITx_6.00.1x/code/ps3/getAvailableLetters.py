def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''


    import string
    letters = string.ascii_lowercase
    answer = ''
    guessedCharacter = ''
    for guess in lettersGuessed:
        guessedCharacter += guess

    for letter in letters:
        if letter not in guessedCharacter:
            answer += letter
    return answer

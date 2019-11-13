def isWordGuessed(secretWord,lettersGuessed):
    for x in lettersGuessed:
        if x not in secretWord:
            return False
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord,lettersGuessed):
    s = ''
    for x in secretWord:
        if x in lettersGuessed:
            s = s + x
        else:
            s = s + '_ '
    return s

def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    s = ''
    for x in a:
        if x not in lettersGuessed:
            s = s + x
    return s

def Hangaroo(secretWord):
    print("Let's play Hangaroo! You have 10 tries to guess the word.")
    lettersGuessed = ''
    availLetters = getAvailableLetters(lettersGuessed)        
    tries = 10
    while tries > 0:
        print()
        print("Secret Word : " + getGuessedWord(secretWord,lettersGuessed))
        letter = input("Guess a letter : ")
        if letter not in availLetters:
            print("You already used that letter.")
        else:
            if letter not in secretWord:
                print("Wrong letter")
            else:
                lettersGuessed += letter
                availLetters = getAvailableLetters(lettersGuessed)        
        if isWordGuessed(secretWord,lettersGuessed):
            print("Secret Word : " + getGuessedWord(secretWord,lettersGuessed))
            print("Congratulations! You guessed the secret word!") 
            input ("Press any key to exit")
            return
        tries -= 1
        print("Remaining tries : ", + tries)
    else:
        #if tries == 0:
        print("Sorry, game over!")
        input("Press any key to try exit")
    
               
      
    return
Hangaroo("apple")


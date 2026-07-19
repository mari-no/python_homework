def make_hangman(secret_word):
    guesses=[]
  
    def hangman_closure(letter):
        guessed_word=[]
       
        if letter not in guesses: 
            guesses.append(letter)
        for char in secret_word:
            if char in guesses:
                guessed_word.append(char)

            else:
                guessed_word.append("_")
        print("".join(guessed_word))
        if ("".join(guessed_word))==secret_word:
            return True
        else: 
            return False

    return hangman_closure


secret_word = input("Enter the secret word: ")
hangman = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ")

    if hangman(letter):
        print("You guessed the word!")
        break



print("Joshua Le's Simple Hangman Project / December 6 2021")

word = "redhotchillipeppers"
guessed = ""
tries = 15

while tries > 0: #tries starts at 15 and goes down each time a letter is not in the word
    guess = input("\nGuess a letter please: ")
    
    if guess in word: #if else statement to check if guess was in the answer
        print(f"Great job! There was a {guess} in the word\n")
    else:
        tries -= 1
        print(f"Not so great! Keep on trying, there was no {guess} in the word. You have {tries} left")

    guessed = guessed + guess #adds the guess count onto the previous guess

    wrong = 0
    for letter in word: #for loop to do check if letter is righ or wrong
        if letter in guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrong += 1

    if wrong == 0: #if statement to stop everything if the person knew the answer from the start
        print(f"You won! The word was: {word}.")
        break
    
else: #else statement if the person lost the game
    print(f"\nYou lose! The word was: {word}.")
    

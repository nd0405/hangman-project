from words import get_random_word

def display_word(word,guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """ step1"""
    print("Welcome to hangman game!!")
    secret_word=get_random_word()
    guessed_letters=set()
    attempts=6

    """step2"""
    while(attempts>0):
        print("\n"+display_word(secret_word,guessed_letters))
        print(f"Attempts left are {attempts}")
        # print('write anything here: {}'.format(attempts))
        print(f"Guessed letters:{','.join(sorted(guessed_letters))}")

        """step3"""
        guess=input("Guess a letter: ").lower()

        """step4"""
        if len(guess)!=1 or not guess.isalpha():
            print("Enter a single  valid letter.")
            continue

        """step5"""
        if guess in guessed_letters:
            print("you already guessed that letter.")
            continue

        """step6"""
        guessed_letters.add(guess)

        """step7"""
        if guess in secret_word:
            print("good game!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"Congrats you guessed the word:{secret_word}")
                break
        else:
              print("Wrong guess")
              attempts-=1
    else:
            print(f"Game over the word was:{secret_word}")

    
hangman()
    

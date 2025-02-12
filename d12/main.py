import random

def guess_the_number():
    guess_this = random.randint(1, 100)
    print("\t\tGuess the Secret Number")
  
    print("The Secret number lies between 1 and 100, try to guess it")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5
    else:
        print("This level is not found.")
        exit()

    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} guesses left to guess THE Secret Number.")
        else:
            print(f"Last try to guess THE Secret number.")
        attempt = int(input("Take you guess: "))
        if attempt > guess_this:
            print("Too high.")
        elif attempt < guess_this:
            print("Too low.")
        if guesses == 1:
            print("Game over.")
        elif attempt == guess_this:
            def game_over():
                print(f"Correct! The Secret Number was {guess_this}.")
                return guesses - guesses
            guesses = game_over()
        guesses -= 1
  
    play_again = input("\nDo you want to play again? Type 'y' to play again: ")
    if play_again == 'y':
        print("\n\n")
        guess_the_number()
    else:
        print("No more secrets!")

guess_the_number()
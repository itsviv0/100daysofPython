# 1. Import random and the word_list.
# 2. Pick a random word from the word_list.
# 3. Create blanks equal to the chosen word.
# 4. User enters the word. 
# 5. Right, wrong word case.
# 6. Display the blanks every time after each round. 
# 7. Have a track of 6 lives.

import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
    
wrong_letters = set()

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        if guess in wrong_letters:
            print("You have made this wrong guess before!")
        elif not guess.isalpha():
            print("Please enter alphabets only.")
        else:
            wrong_letters.add(guess)
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"The word is: {chosen_word}")
                print(".....You ran out of lives.")
                break

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
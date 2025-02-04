# 1. Ask the user to choose between stone, paper, scissor.
# 2. Generate random choice for computer as a opponent.
# 3. Handle wrong input other than stone, paper and scissor.
# 4. Display the winner of the round.
# 5. Keep track of the score.
# 6. Display winner of the game at the end.

import random

rock = """
    _______
___/   ____)
      (_)___)
      (_)___)
      (_)___)
```\\__(_)__)
"""

paper = """
    _______
___/   ____)____
          ______)
          _______)
         _______)
```\\__________)
"""

scissors = """
    _______
___/   ____)____
          ______)
       __________)
      (_)___)
```\\__(_)__)
"""

player_score = 0
computer_score = 0

print("Welcome to STONE PAPER SCISSOR!")
while True:
  choice = (input("\nWhat is your weapon? Type 1 for Rock, 2 for Paper or 3 for Scissors\n1/2/3:"))
  computers_choice = random.randint(1,3)
  
  if choice == 'x':
    break
  elif not choice.isdigit():
    print("You've entered an invalid value, try again and choose a number between 0-2.")
  else:
    choice = int(choice)
    if choice > 3:
      print("You've entered an invalid number, try again and choose a number between 0-2.")
    elif choice == 1 or choice == 2 or choice == 3:
      if choice == 1:
        print(f"Your weapon: Rock {rock}")
      elif choice == 2:
        print(f"Your weapon: Paper {paper}")
      elif choice == 3:
        print(f"Your weapon: Scissors {scissors}")
  
      if computers_choice == 1:
        print(f"Computer's weapon: Rock {rock}")
        if choice == 3:
          print("You lose, Rock wins against scissors.")
          computer_score += 1
        elif choice == 1:
          print("It's a draw!")
        else:
          print("You win!")
          player_score += 1
  
      elif computers_choice == 2:
        print(f"Computer's weapon: Paper {paper}")
        if choice == 1:
          print("You lose, Paper wins against rock.")
          computer_score += 1
        elif choice == 2:
          print("It's a draw!")
        else:
          print("You win!")
          player_score += 1
  
      elif computers_choice == 3:
        print(f"Computer's weapon: Scissors {scissors}")
        if choice == 2:
          print("You lose, Scissors win against paper.")
          computer_score += 1
        elif choice == 3:
          print("It's a draw!")
        else:
          print("You win!")
          player_score += 1
      
    print("Enter 'x' to stop playing.")
    
print(f"\nYour score: {player_score}")
print(f"Computer score: {computer_score}")

if player_score > computer_score:
  champion = 'Player'
elif computer_score > player_score:
  champion = 'Computer'
else:
  champion = ''
  
if champion:
  print(f"The champion is {champion}!! Congratulations")
else:
  print("The match ended in a draw...")

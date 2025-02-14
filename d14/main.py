from game_data import data
import random

def fetch_profile():
    random_number = random.randint(0, 49)
    name = data[random_number]['name']
    follower_count = data[random_number]['follower_count']
    description = data[random_number]['description']
    country = data[random_number]['country']
    compare = (f"{name}, a {description}, from {country}.")
    return compare, follower_count

def higher_lower():
    profile_a, followers_a = fetch_profile()
    profile_b, followers_b = fetch_profile()
    if followers_a == followers_b:
        profile_b, followers_b = fetch_profile()
    score = 0
    correct = True

    while correct:

        if score > 0:
            print(f"Correct! Your current score is: {score}.")
        print(f"Compare A: {profile_a}")
        print("\t\t\t\t\tvs")
        print(f"Compare B: {profile_b}")

        a_or_b = input("\nWho do you think has more followers? \t 'a', or 'b': ").lower()
        if a_or_b == 'a' and followers_a >= followers_b:
            score += 1
            profile_b, followers_b = fetch_profile()
        elif a_or_b == 'b' and followers_a <= followers_b:
            score += 1
            profile_a, followers_a = fetch_profile()
        elif a_or_b == 'a' and followers_a < followers_b:
            print(f"\nIncorrect, your final score is {score}.")
            correct = False
        elif a_or_b == 'b' and followers_a > followers_b:
            print(f"\nIncorrect, your final score is {score}.")
            correct = False
        else:
            print("\nInvalid option.")
            exit()
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        higher_lower()
    elif play_again == 'n':
        print("Thanks for playing!")
    else:
        print("Invalid choice")
        exit()
        
higher_lower()

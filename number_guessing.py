from random import randint

EASY_TURNS = 10
HARD_TURNS = 5

def check_guess(user_guess, answer,turns):
    if user_guess < answer:
        print("Your guess is too low")
        return turns - 1
    elif user_guess > answer:
        print("Your guess is too high")
        return turns - 1
    else:
        print("You got the correct number")

def set_difficulty_level():
    level = input("Choose your difficulty level (Type 'Easy' or 'Hard'): ").lower()
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100...")
    answer = randint(1,100)
    print(f"Computer's choice: {answer}")
    turns = set_difficulty_level()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} turns left")
        user_guess = int(input("Make your guess:"))
        turns = check_guess(user_guess,answer,turns)
        if turns == 0:
            print("You run out of guess, YOU LOST!")
            return
        elif user_guess != answer:
            print("Guess again")


game()

import random


def print_game_menu():
    print("Welcome to Guess the Number!")
    print()
    print(f"{' Levels ':*^50}")
    print(f"{'*  1. EASY, range: (1, 10), max moves: 7 ':<49}*")
    print(f"{'*  2. MEDIUM, range: (1, 10), max moves: 5 ':<49}*")
    print(f"{'*  3. HARD, range: (1, 100), max moves: 10 ':<49}*")
    print("*"*50)
    print()

def get_valid_level():
    """ Get valid level dificulty from user"""
    level = int(input("Select level: "))
    while True:
        if level == 1:
            print()
            print("*** Let's play EASY. Good Luck! ***") # 1..10
            print()
            break
        elif level == 2:
            print()
            print("*** Let's play MEDIUM. Good Luck! ***")
            print()
            break
        elif level == 3:
            print()
            print("*** Let's play HARD. Good Luck! ***")
            print()
            break
        else:
            print()
            print("Enter a number between 1 and 3")
            print()
            level = int(input("Select level: "))

def set_level_state():
    """ Generate random number and total moves according to level difficulty """
    if level == 1:
        random_number = random.randint(1,10)
        total_moves = 7
    elif level == 2:
        random_number = random.randint(1,10)
        total_moves = 5
    else:
        random_number = random.randint(1,100)
        total_moves = 10

# Game cycle
moves = 0

while total_moves > 0:

    user_guess = int(input("Guess the number: "))
    moves += 1
    total_moves -= 1
    if user_guess == random_number:
        print()
        print(f"*** Congratulations! You guessed it right in {moves} moves! ***")
        break
    elif user_guess > random_number:
        print(f"Too large! Moves left: {total_moves}")
        print()
        continue
    elif user_guess < random_number:
        print(f"Too small! Moves left: {total_moves}")
        print()
        continue


if total_moves < 1 and user_guess != random_number:
    print(f"""You dont have any moves left! Correct number was >>> {random_number} <<<
                    GAME OVER""")



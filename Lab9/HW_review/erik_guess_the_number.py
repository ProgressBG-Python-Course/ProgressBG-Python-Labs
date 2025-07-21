import random

def choose_difficulty():
    print("")
    print("Welcome to Guess the Number!")
    print("")
    print(f"{19*"*":<20}Levels {19*"*":<20}")
    print(f"* {'1. EASY, range: (1, 10), max moves: 7':<43}*")
    print(f"* {'2. MEDIUM, range: (1, 10), max moves: 5':<43}*")
    print(f"* {'3. HARD, range: (1, 100), max moves: 10':<43}*")
    print(f"{46*"*"}")
    print("")

    while True:
        chosen_lvl = int(input("Select level: "))

        if chosen_lvl in [1,2,3]:
            if chosen_lvl == 1:
                print("")
                print("Let's play EASY. Good Luck")
                return chosen_lvl
            if chosen_lvl == 2:
                print("")
                print("Let's play MEDIUM. Good Luck")
                return chosen_lvl
            if chosen_lvl == 3:
                print("")
                print("Let's play HARD. Good Luck!")
                return chosen_lvl
        else:
            print("Please select a valid level number (1-3)")

def generate_random_number(a,b):
    return random.randint(a,b)

def init_game(chosen_lvl):
    if chosen_lvl == 1:
         = generate_random_number(1, 10)
        max_moves = 7
        range_text = "(between 1 and 10)"
    elif chosen_lvl == 2:
        number_to_be_guessed = generate_random_number(1, 50)
        max_moves = 5
        range_text = "(between 1 and 10)"
    else:
        number_to_be_guessed = generate_random_number(1, 10)(1, 100)
        max_moves = 10
        range_text = "(between 1 and 100)"

    return number_to_be_guessed, max_moves, range_text


def play_game(chosen_lvl):
    number_to_be_guessed,max_moves,range_text = init_game(chosen_lvl)

    moves_left = max_moves

    while moves_left > 0:
        guess = int(input(f"Guess the number {range_text}: "))
        moves_left -= 1

        if guess < number_to_be_guessed:
            print(f"Too low! Moves left: {moves_left}")
        elif guess > number_to_be_guessed:
            print(f"Too high! Moves left: {moves_left}")
        else:
            print(f"Congratulations! You guessed it right with {max_moves - moves_left} moves!")
            return

    print(f"You ran out of moves! The number was {number_to_be_guessed}.")


level = choose_difficulty()
play_game(level)
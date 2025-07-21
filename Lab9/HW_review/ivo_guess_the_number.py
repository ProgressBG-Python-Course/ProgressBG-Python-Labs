
def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("Choose difficulty: easy,medium or hard")

    difficulty = input("Enter difficulty: ")

    if difficulty == "easy":
        secret_number = 4
        max_number = 5
    elif difficulty == "medium":
        secret_number = 7
        max_number = 10
    elif difficulty == "hard":
        secret_number = 14
        max_number = 20

    print(f"Generating a  number between 1 and {max_number}.")

    guess = 0
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it right.")



guess_the_number() # Run the game
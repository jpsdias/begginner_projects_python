import random

def game():
    
    # Generate a random integer between 1 and 100 (inclusive)
    random_number = random.randint(1, 100)
    # print(f"{random_number}")

    # Set the number of attempts (lives) the user has
    lives = 3
    # print(f"{lives}")

    # Display the game introduction and instructions
    print("Welcome to the guess the number game.")
    print(f"You have {lives} attemps to guess the generated number from 1 to 100.")
    print("Good Luck ;)!\n")

    # Iterate over the number of attempts (from lives down to 1)
    for attempt in range(lives, 0, -1):
        # Prompt the user for their guess
        user_guess = input("Please enter your guess: \n")
        # print(f"{user_guess}")
        
        try:
            # Attempt to convert the user's input to an integer
            iguess = int(user_guess)
            # print(f"{iguess}")
        
        except ValueError:
            # If the input is not a valid integer, display an error message
            # and skip this iteration without decrementing an attempt
            print(f"{user_guess} is not a valid integer. Please try again!\n")
            continue  # Continue to the next iteration of the loop

        # Check if the user's guess is less than the generated number
        if iguess < random_number:
            print("Go higher.\n")
        # Check if the user's guess is greater than the generated number
        elif iguess > random_number:
            print("Go lower.\n")
        # The user's guess is equal to the generated number
        else:
            print("Congratulations, You won!\n")
            break  # Exit the loop since the user has guessed correctly

        # Display the number of remaining attempts (lives)
        print(f"You have {attempt - 1} lives left.\n")
    else:
            # This block executes if the loop completes without a break (i.e., the user never guessed correctly)
            print(f"You lost, the right guess was {random_number}. Better luck next time!\n")
import random

# Main
# Takes user input for range and attempts
print("""\033[0;33mWelcome to the Number Guesser game!
please enter the start and end value of range (inclusive) and attempts you want to guess\033[0;33m""")
Start = int(input("\033[0;32mEnter the start value : \033[0;32m"))
End = int(input("\033[0;32mEnter the end value : \033[0;32m"))
Attempts = int(input("\033[0;32mEnter the number of attempts : \033[0;32m"))

# Generates random number inclusive of start and end range
# Swaps start and end if start is greater than end
if Start > End:
    Start, End = End, Start
Number = random.randint(Start, End)

# Loops through until user guesses the number or runs out of attempts
Guessed = False
for Attempt in range(Attempts, 0, -1):
    # Takes user guess
    Guess = int(input(f"\n\033[0;33mGuess a number from {Start} to {End} : \033[0;33m"))
    # Checks if guess is correct and ends loop early
    if Guess == Number:
        print(f"\033[0;32mCongratulations! You have guessed the number {Number} correctly.\033[0;32m")
        Guessed = True
        break
    # Tells user they're wrong and amount of attempts left
    else:
        # Tells the user if the number is higher or lower
        Position = "higher" if Guess < Number else "lower"
        print(f"""\033[0;31mSorry, the number you guessed is incorrect. You have {Attempt - 1} attempts left.\033[0;31m
The number to guess is {Position} than your guess of {Guess}.""")
# Returns message depending on whether user guessed correctly
if Guessed:
    print("\033[0;32mYou have won the guessing game!.\033[0;32m")
else:
    print("\033[0;31mSorry, better luck next time.\033[0;31m")
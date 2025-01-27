# Users can log into an account with limited amount of times to try it before being locked out.
# Account username and passwords are stored in a dictionary.
Accounts = {"Reese" : "s4a5x365/][;[.#/\/9-m09",
            "Sam" : "HelloWorld",
            "John" : "John",
            "Ralphs" : "ItzGrannyz4DaWin",
            "Zeke" : "password"
            "Advin" : "Advin1"}

def LogIn():
    Correct = False
    Attempts = 0
    # Loops through until user successfully logged in or has tried 3 times
    while not Correct and Attempts < 3:
        # Takes user input
        Username = input("\033[0;33mEnter your username: \033[0;33m")
        Password = input("\033[0;33mEnter your password: \033[0;33m")
        # Checks if user account exists and password correct
        if (Username in Accounts) and (Accounts[Username] == Password):
            Correct = True
            print(f"\033[0;32mYou have successfully logged in {Username}.\033[0;32m")
            break
        # Checks if user exceeds 3 attempts and locks out if so
        else:
            Attempts += 1
            print(f"\033[0;31mIncorrect username or password. You have {3 - Attempts} attempts left.\n\033[0;31m")
    if not Correct:
        print("\033[0;31mYou have been locked out.\033[0;31m")

# Main
LogIn()
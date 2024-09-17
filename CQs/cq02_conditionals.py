"""Conditionals!"""

__author__ = "730664484"


def guess_a_number() -> None:
    """This function asks the user for a number and tells you if you guessed the secret number or not!"""
    secret: int = 7  # defines the secret number
    x: int = int(input("Guess a number: "))  # asks the user for their guess
    print("Your guess was", x)
    if x == secret:  # checks if they guessed the secret number
        print("You got it!")
    elif x <= secret:  # checks if their guess was too low
        print("Your guess was too low! The secret number is", secret)
    elif x >= secret:  # checks if their guess was too high
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()

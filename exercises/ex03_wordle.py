"""Creating my own Wordle game!"""

__author__ = "730664484"


def input_guess(expected_length: int) -> str:
    """Checks whether the guessed word is the correct length, and continues asking until it is"""
    guess: str = input(
        f"Enter a {expected_length} character word: "
    )  # asks user to input their guess
    while expected_length != len(guess):
        guess = input(
            f"That wasn't {expected_length} chars! Try again: "
        )  # asks user to input new word if their guess was incorrect length
    return guess


def contains_char(secret_word: str, char: str) -> bool:
    """Checks whether the secret word contains the guessed character"""
    assert len(char) == 1  # confirms only a single character was entered
    index = 0
    while index < len(secret_word):  # checks over every character
        if (
            char == secret_word[index]
        ):  # checks if the character matches the character at the index
            return True
        index += 1
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """Output the colored emojis depending on if the characters in the guessed word are in the correct place or in the word"""
    assert len(guessed_word) == len(
        secret_word
    )  # confirms that the guessed and secret word are same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    result = ""  # creates a result to build upon as each character is checked
    while index < len(secret_word):
        if guessed_word[index] == secret_word[index]:
            result += GREEN_BOX  # if the character is in correct spot adds green square
        elif contains_char(secret_word, guessed_word[index]):
            result += YELLOW_BOX  # if the character is in the word but wrong spot add yellow square
        else:
            result += WHITE_BOX  # if character is not in word add white square
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N = 1  # variable to count how many turns used
    secret_word = secret
    max_guesses = 6
    won: bool = False  # checks if won before turns are up
    while N <= max_guesses and not won:  # runs until word is guessed or turns are up
        print(f"=== Turn {N}/6 ===")
        guessed_word = input_guess(
            len(secret_word)
        )  # confirms guessed word is correct length
        output = emojified(
            guessed_word, secret_word
        )  # finds what characters are in the word and where
        print(output)
        if guessed_word == secret_word:  # checks if correct word is guessed
            won = True
        else:
            N += 1  # adds another turn
    if won:
        print(f"You won in {N}/{max_guesses} turns!")
    else:
        print(f"X/{max_guesses} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="model")

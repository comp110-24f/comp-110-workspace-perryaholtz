"""While loops!"""

__author__ = "730664484"


def num_instances(phrase: str, search_char: str) -> int:
    """A function that counts how many  matches of a letter there are in a word."""
    count: int = 0  # creates variable for number of matches
    index: int = 0  # creates a number that can increase to eventually end the loop
    while index < len(phrase):
        if (
            search_char == phrase[index]
        ):  # checks if the character matches the letter in the word
            count = count + 1
        index = index + 1  # increases the index to make the loop not infinite
    return count


print(num_instances(phrase="hello", search_char="l"))

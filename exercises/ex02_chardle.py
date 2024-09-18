"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730664484"


def input_word() -> str:
    "Asks user for word input and confirms that it is 5 characters long."
    five_character_word: str = str(
        input("Enter a 5-character word: ")
    )  # asks for user input
    if len(five_character_word) == 5:  # checks if word is five letters long
        return five_character_word
    elif len(five_character_word) != 5:
        print(
            "Error: Word must contain 5 characters."
        )  # prints error if word if not 5 letters long
        exit()  # ends main function when there is an error
    return five_character_word


def input_letter() -> str:
    """Asks user for character input and ensures it is only a single character."""
    single_character: str = str(
        input("Enter a single character: ")
    )  # asks for user input
    if len(single_character) == 1:  # checks that the it is a single letter
        return single_character
    elif len(single_character) != 1:
        print(
            "Error: Character must be a single character."
        )  # prints error if it is not a single letter
        exit()  # ends main function when there is an error
    return single_character


def contains_char(word: str, letter: str) -> None:
    """Looks if the inputted letter is in the word, and counts the number of instances it appears."""
    print(
        "Searching for", letter, "in", word
    )  # lets user know the function is searching
    number_of_instances: int = (
        0  # defines a variable that will increase with every match
    )
    if word[0] == letter:  # asks if the first letter of the word matches the letter
        print(letter, "found at index 0")
        number_of_instances = (
            number_of_instances + 1
        )  # increases the instance if its true
    if word[1] == letter:  # asks if the second letter of the word matches the letter
        print(letter, "found at index 1")
        number_of_instances = number_of_instances + 1
    if word[2] == letter:  # asks if the third letter of the word matches the letter
        print(letter, "found at index 2")
        number_of_instances = number_of_instances + 1
    if word[3] == letter:  # asks if the fourth letter of the word matches the letter
        print(letter, "found at index 3")
        number_of_instances = number_of_instances + 1
    if word[4] == letter:  # asks if the five letter of the word matches the letter
        print(letter, "found at index 4")
        number_of_instances = number_of_instances + 1
    if number_of_instances == 0:  # checks if there were no matches
        print(
            "No instances of", letter, "found in", word
        )  # tells user there were no matches found
    if number_of_instances == 1:  # checks if there was only one match
        print(
            number_of_instances, "instance of", letter, "found in", word
        )  # tells user 1 match was found
    if number_of_instances >= 1:  # checks if there were multiple matches
        print(
            number_of_instances, "instances of", letter, "found in", word
        )  # tells users the number of matches found


def main() -> None:  # combines all the functions into one main function
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # calls the function
    main()

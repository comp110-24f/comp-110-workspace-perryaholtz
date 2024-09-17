"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730664484"


def input_word() -> str:
    five_character_word: str = str(input("Enter a 5-character word: "))
    if len(five_character_word) == 5:
        return five_character_word
    elif len(five_character_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    single_character: str = str(input("Enter a single character: "))
    if len(single_character) == 1:
        return single_character
    elif len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    print("Searching for", letter, "in", word)
    number_of_instances: int = 0
    if word[0] == letter:
        print(letter, "found at index 0")
        number_of_instances = number_of_instances + 1
    if word[1] == letter:
        print(letter, "found at index 1")
        number_of_instances = number_of_instances + 1
    if word[2] == letter:
        print(letter, "found at index 2")
        number_of_instances = number_of_instances + 1
    if word[3] == letter:
        print(letter, "found at index 3")
        number_of_instances = number_of_instances + 1
    if word[4] == letter:
        print(letter, "found at index 4")
        number_of_instances = number_of_instances + 1
    if number_of_instances == 0:
        print("No instances of", letter, "found in", word)
    if number_of_instances >= 0:
        print(number_of_instances, "instances of", letter, "found in", word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()

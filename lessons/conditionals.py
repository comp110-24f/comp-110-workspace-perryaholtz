"""Practicing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num <10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        return True  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


def wake_up(alarm: bool) -> str:
    """Returns message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it!"


# print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] is letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    weather: str = input("what is the weather?")
    if weather == "rainy" or weather == "cold":
        return "Bring a jacket!"
    elif weather == "hot":
        return "Keep cool out there!"
    else:
        return "I don't recognize this weather."


print(get_weather_report())

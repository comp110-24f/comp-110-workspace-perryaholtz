"""practicing lists"""

name: list[str] = ["perry", "ava", "rylie", "audrey"]

# print(name[0])

my_numbers: list[float] = list()  # or just []

my_numbers.append(0.12)
my_numbers.append(0.12)

game_point: list[int] = [102, 86, 94]

game_point[1] = 72  # replaces a number via index
game_point.pop(1)

print(game_point)

# print(my_numbers)


def display(list) -> None:
    index = 0
    while index < len(list):
        print(list[index])
        index += 1


display(game_point)

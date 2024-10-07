"""Learning how to reverse engineer list utility functions"""

__author__ = "730664484"


def all(a: list[int], b: int) -> bool:
    index = 0
    while index < len(a):
        if a[index] != b:
            return False
        index += 1
    return True


# print(all([1, 1, 1], 1))


def max(input: list[int]) -> int:
    index = 0
    max_value = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while index < len(input):
        if input[index] >= max_value:
            max_value = input[index]
        index += 1
    return max_value


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    index = 0
    while index < len(input_1):
        if input_1[index] != input_2[index]:
            return False
        index += 1
    return True


def extend(input_a: list[int], input_b: list[int]) -> None:
    index = 0
    while index < len(input_b):
        input_a.append(input_b[index])
        index += 1


a = [1, 2, 3]
b = [4, 5, 6]
extend(a, b)
print(a)

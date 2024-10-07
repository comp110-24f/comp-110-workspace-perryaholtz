"""Mutating functions."""

__author__ = "730664484"


def manual_append(a: list[int], b: int) -> None:
    """adds the input to the list"""
    a.append(b)


def double(c: list[int]) -> None:
    "doubles each value of the list"
    index = 0
    while index < len(c):
        c[index] = c[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)

"""for... in... loops"""

xs: list[str] = ["w", "x", "y", "z"]
idx: int = 0
"""if we used while"""
while idx < len(xs):
    print(xs[idx])
    idx += 1

"""if used  for.. in..."""
for elem in xs:
    print(elem)

"""practice of for loops"""

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for (
    elem
) in (
    my_list
):  # copying over every item in mylist to the newlist #elem is new variable in globals
    new_list.append(elem)
print(new_list)

pets: list[str] = ["Louie", "Bo", "Bear"]
for name in pets:
    print(f"Good boy,{name}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")

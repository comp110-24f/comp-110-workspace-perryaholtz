"""Practice with function."""

from random import randint

print(randint(1, 10))


# Define a function
def sum(num1: int, num2: int) -> int:  # parameter list
    """Returns sum of two integers"""
    return num1 + num2


# Call the function
print(sum(num1=1, num2=10))  # 1 and 10 are my arguments

"""Tea Party Exercise! Creating multiple functions that work together."""

__author__: str = "730664484"


def main_planner(guests: int) -> None:  # combine all created functions
    "Implement all functions to compute final cost"
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # print how many people will be at party
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # print the number of tea bags according to the inputted guests
    print(
        "Treats: " + str(treats(people=guests))
    )  # print the number of treats according to the inputted guests
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests),
                treat_count=(treats(people=guests)),
            )
        )
    )  # print the cost according to the number of tea bags and treats
    return None


def tea_bags(people: int) -> int:
    "Counts the number of tea bags needed"
    return (
        2 * people
    )  # multiply the number of people by two to get the necessary number of tea bags


def treats(people: int) -> int:
    "Counts the number of treats needed"
    return int(
        1.5 * tea_bags(people=people)
    )  # multiply the number of tea bags based on the number of people by 1.5 to get the necessary number of treats


def cost(tea_count: int, treat_count: int) -> float:
    "Computes how much it would cost based on number of tea bags and treats"
    return float(
        0.5 * tea_count + 0.75 * treat_count
    )  # multiply the number of tea bags by 0.5 and number of treats by 0.75 to get the total cost


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # ask user to input number of guests in order to run main function

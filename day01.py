"""https://adventofcode.com/2022/day/1"""

# part one
def get_max_calorie_total():
    """Get max calories from input"""

    with open("day01_input.txt", "r") as f:
        input_lines = f.readlines()
        highest_calorie_amount = 0
        current_calorie_total = 0
        for line in input_lines:
            if line == "\n":
                if current_calorie_total > highest_calorie_amount:
                    highest_calorie_amount = current_calorie_total
                current_calorie_total = 0
                continue
            current_calorie_total += int(line)
    return highest_calorie_amount


# part two
def get_top_three_max_calorie():
    with open("day01_input.txt", "r") as f:
        top_three_elves = [0, 0, 0]
        current_calorie_total = 0
        input_lines = f.readlines()
        for line in input_lines:
            if line == "\n":
                top_three_elves = compare_against_top_three_elves(
                    top_three_elves, current_calorie_total
                )
                current_calorie_total = 0
                continue
            current_calorie_total += int(line)
    return top_three_elves


def compare_against_top_three_elves(top_three_elves: list, current_calorie_total: int):
    top_three_elves.sort(reverse=True)
    if (
        current_calorie_total > top_three_elves[0]
        or current_calorie_total > top_three_elves[1]
        or current_calorie_total > top_three_elves[2]
    ):
        # delete lowest number and prepend new number to list
        del top_three_elves[2]
        return [current_calorie_total] + top_three_elves
    return top_three_elves


if __name__ == "__main__":
    highest_cal = get_max_calorie_total()
    print(highest_cal)
    highest_three_cal = get_top_three_max_calorie()
    print(highest_three_cal)
    highest_three_total = sum(highest_three_cal)
    print(highest_three_total)

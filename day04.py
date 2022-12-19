"""https://adventofcode.com/2022/day/4"""
import pandas as pd


def get_input_from_file():
    df = pd.read_csv("day04_input.txt", header=None, sep=",")
    return df.to_records(index=False)


def expand_number_range(id_range_str: str):
    ids = id_range_str.split("-")
    min = int(ids[0])
    max = int(ids[1])
    curr = min
    id_range_expanded_list = []
    while curr <= max:
        id_range_expanded_list.append(curr)
        curr += 1
    return id_range_expanded_list


def find_encompassing_ids(pair1, pair2):
    """If either remainder is none, then we have an encompassing pairing"""
    pair1_set = set(pair1)
    pair2_set = set(pair2)
    overlap = list((pair1_set & pair2_set))
    pair1_remainder = list((pair1_set - pair2_set))
    pair2_remainder = list((pair2_set - pair1_set))
    # print(f"Overlap:{overlap}, R1:{pair1_remainder}, R2:{pair2_remainder}")
    if len(pair1_remainder) == 0 or len(pair2_remainder) == 0:
        return True
    return False


def find_overlapping_ids(pair1, pair2):
    """If overlap exists return true, else return false."""
    pair1_set = set(pair1)
    pair2_set = set(pair2)
    overlap = list((pair1_set & pair2_set))
    if len(overlap) != 0:
        return True
    return False


def part_one(puzzle_input):
    num_encompassing_pairs = 0
    for pair in puzzle_input:
        if find_encompassing_ids(
            expand_number_range(pair[0]), expand_number_range(pair[1])
        ):
            num_encompassing_pairs += 1
            # print(f"True {pair[0]},{pair[1]}")
    return num_encompassing_pairs


def part_two(puzzle_input):
    num_encompassing_pairs = 0
    for pair in puzzle_input:
        if find_overlapping_ids(
            expand_number_range(pair[0]), expand_number_range(pair[1])
        ):
            num_encompassing_pairs += 1
            # print(f"True {pair[0]},{pair[1]}")
    return num_encompassing_pairs


if __name__ == "__main__":
    puzzle_input = get_input_from_file()
    part_one_result = part_one(puzzle_input)
    part_two_result = part_two(puzzle_input)

    print(f"Part 1 Result = {part_one_result}")
    print(f"Part 2 Result = {part_two_result}")

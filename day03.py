"""https://adventofcode.com/2022/day/3"""
import pandas as pd

ALPHABET_PRIORITY = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}


def get_input_from_file():
    df = pd.read_csv("day03_input.txt", header=None)
    return df.to_records()


def input_to_split_list(puzzle_input):
    input_as_list = []
    for _, line in puzzle_input:
        halfway_len = int(len(line) / 2)
        input_as_list.append([line[:halfway_len], line[halfway_len:]])
    return input_as_list


def input_to_group_list(puzzle_input: dict):
    input_as_list = []
    max_lines_per_group = 3
    line_count = 0
    group = []
    for _, line in puzzle_input:
        print(line)
        group.append(line)
        line_count += 1
        if line_count == max_lines_per_group:
            input_as_list.append(group)
            group = []
            line_count = 0
    return input_as_list


def find_matching_letter(items1, items2):
    matching_char = list(set(items1).intersection(items2))[0]
    return matching_char


def find_matching_letter_three_items(group_list):
    common_letter = list(set.intersection(*map(set, group_list)))
    return common_letter


def part_one():
    puzzle_input = get_input_from_file()
    puzzle_input_as_list = input_to_split_list(puzzle_input)
    priority_point_list = []
    for item in puzzle_input_as_list:
        matching_letter = find_matching_letter(item[0], item[1])
        priority_point = ALPHABET_PRIORITY.get(matching_letter)
        priority_point_list.append(priority_point)
        print(f"{matching_letter} -> {priority_point}")
    print(sum(priority_point_list))


def part_two():
    puzzle_input = get_input_from_file()
    puzzle_input_as_group_list = input_to_group_list(puzzle_input)
    priority_point_list = []
    for group in puzzle_input_as_group_list:
        matching_letter = find_matching_letter_three_items(group)[0]
        print(f"{matching_letter} -> {group}")
        priority_point = ALPHABET_PRIORITY.get(matching_letter)
        priority_point_list.append(priority_point)
        print(f"{matching_letter} -> {priority_point}")
    print(sum(priority_point_list))


if __name__ == "__main__":
    part_two()

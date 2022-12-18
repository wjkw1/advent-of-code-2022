from enum import Enum
import json
import os


def get_input_from_file():
    puzzle_input = []
    with open("day2_input.txt", "r") as f:
        input_lines = f.readlines()
        for line in input_lines:
            lines = line.split(" ")
            lines[1] = lines[1].rstrip(os.linesep)
            puzzle_input.append(lines)
    return puzzle_input


class Game:
    """Game of rock paper scissors"""

    def __init__(self, computer_hand, player_hand):
        self.player_hand = self.get_shape_from_letter(player_hand)
        self.computer_hand = self.get_shape_from_letter(computer_hand)
        self.status = self.play_game()
        self.total_score = self.get_total_score()

    def get_total_score(self) -> int:
        """Gets the total score"""
        return self.get_game_points() + self.get_hand_points()

    def get_shape_from_letter(self, letter: str) -> str:
        """Changes the letters into a known shape value,
        returns None if unknown shape."""
        if letter in ["A", "X"]:
            return "rock"
        if letter in ["B", "Y"]:
            return "paper"
        if letter in ["C", "Z"]:
            return "scissors"

    def play_game(self):
        """Playes the game and sets the game status,
        returns None if unknown hand pairing."""
        status = None
        if self.player_hand == self.computer_hand:
            status = "draw"

        if self.player_hand == "rock":
            if self.computer_hand == "paper":
                status = "loss"
            if self.computer_hand == "scissors":
                status = "win"

        if self.player_hand == "paper":
            if self.computer_hand == "rock":
                status = "win"
            if self.computer_hand == "scissors":
                status = "loss"

        if self.player_hand == "scissors":
            if self.computer_hand == "paper":
                status = "win"
            if self.computer_hand == "rock":
                status = "loss"

        return status

    def get_game_points(self) -> int:
        """Get the points from the game status"""
        if self.status == "win":
            return 6
        if self.status == "loss":
            return 0
        if self.status == "draw":
            return 3

    def get_hand_points(self) -> int:
        """Get the points allocated from the shape chosen"""
        if self.player_hand == "rock":
            return 1
        if self.player_hand == "paper":
            return 2
        if self.player_hand == "scissors":
            return 3

    def __repr__(self):
        return json.dumps(
            {
                "status": self.status,
                "player_hand": self.player_hand,
                "computer_hand": self.computer_hand,
                "total_score": self.total_score,
            }
        )


if __name__ == "__main__":
    puzzle_input = get_input_from_file()
    total_score = 0
    for hands in puzzle_input:
        print(hands)
        game_round = Game(hands[0], hands[1])
        print(game_round)
        total_score += game_round.total_score
    print(f"Total Score: {total_score}")

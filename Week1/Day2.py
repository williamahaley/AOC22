from dataclasses import dataclass, field
from Day2_input import actual_input


@dataclass
class Round:
    them_code: str
    you_code: str
    score: int = field(init=False)
    you: int = field(init=False)
    them: int = field(init=False)

    cypher = {
        "A": 1, "X": 1,  # rock
        "B": 2, "Y": 2,  # paper
        "C": 3, "Z": 3,  # scissors
    }

    def score_game(self):
        self.you = self.cypher[str(self.you_code).strip().upper()]
        self.them = self.cypher[str(self.them_code).strip().upper()]

        if self.you == self.them:
            return self.you + 3

        if (self.them_code, self.you_code) in [("A", "Z"), ("B", "X"), ("C", "Y")]:  # Loser
            return self.you + 0

        if (self.them_code, self.you_code) in [("A", "Y"), ("B", "Z"), ("C", "X")]:  # Winner Winner Taco Dinner
            return self.you + 6

    def __post_init__(self):
        self.score = self.score_game()


class Round2(Round):

    cypher = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors

        "X": 0,  # lose
        "Y": 3,  # draw
        "Z": 6,  # win
    }

    def score_game(self):
        self.them = self.cypher[str(self.them_code).strip().upper()]
        outcome_bonus = self.cypher[str(self.you_code).strip().upper()]
        if self.you_code == "Y":
            return outcome_bonus + self.them
        if self.you_code == "X":
            to_loss = {"C": "B", "A": "C", "B": "A"}
            play = to_loss[self.them_code]
            temp = outcome_bonus + self.cypher[play]
            return temp
        if self.you_code == "Z":
            to_win = {"B": "C", "C": "A", "A": "B"}
            temp = outcome_bonus + self.cypher[to_win[self.them_code]]
            return temp


if __name__ == "__main__":
    input = """A Y
B X
C Z
"""
    games = []
    game1_score = 0
    game2_score = 0
    for match in actual_input.splitlines():
        plays = match.strip().split(" ")
        game1 = Round(them_code=plays[0], you_code=plays[1])
        game1_score += game1.score
        game2 = Round2(them_code=plays[0], you_code=plays[1])
        game2_score += game2.score
        games.append(game2)
    print(game1_score)
    print(game2_score)



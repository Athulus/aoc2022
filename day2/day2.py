ROCK = 0
PAPER = 1
SCISSORS = 2


def parse_choice(choice: str) -> int:
    if choice == "A" or choice == "X":
        return ROCK
    if choice == "B" or choice == "Y":
        return PAPER
    if choice == "C" or choice == "Z":
        return SCISSORS


def won_match_score(you: int, opponent: int) -> int:
    """
    0 points for losing, 3 points for tie, 6 points for wi
    """
    if (you + 1) % 3 == opponent:
        return 0
    elif you == opponent:
        return 3
    else:
        return 6


def score_match_real(line: str) -> int:
    opponent = parse_choice(line[0])
    outcome = line[2]
    match outcome:
        case "X":  # lose
            return 0 + ((opponent - 1) % 3) + 1
        case "Y":  # draw
            return 3 + opponent + 1
        case "Z":  # win
            return 6 + ((opponent + 1) % 3) + 1


with open("day2/input", encoding="utf-8") as f:
    total_score: int = 0
    real_total_score: int = 0
    for match in f:
        YOU = parse_choice(match[2])
        OPP = parse_choice(match[0])
        total_score += won_match_score(YOU, OPP) + YOU + 1
        real_total_score += score_match_real(match)
    print(total_score, real_total_score)

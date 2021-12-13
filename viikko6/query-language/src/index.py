from statistics import Statistics
from player_reader import PlayerReader
from matchers import *

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)
    print("============")

    matcher = Not(All())

    for player in stats.matches(matcher):
        print(player)
    print("============")

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)
    print("============")

    matcher = And(
        HasFewerThan(5, "goals"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)
    print("============")

    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    for player in stats.matches(matcher):
        print(player)
    print("============")

if __name__ == "__main__":
    main()

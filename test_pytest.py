import pytest
from bowling_game import BowlingGame

rollsNormal = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
rollsPerfect = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
rollsSpares = [5 for i in range(21)]
rollsGutter = [0 for i in range(20)]
rollsRegular = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]

@pytest.mark.parametrize("_count_numbers,expected,rolls", [
    (3, 28, rollsNormal),
    (7, 55, rollsNormal),
    (12, 142, rollsNormal),
    (17, 190, rollsNormal),
    (12, 300, rollsPerfect),
    (21, 150, rollsSpares),
    (20, 0, rollsGutter),
    (20, 72, rollsRegular)
    ])

def testGame(_count_numbers: int, expected: int, rolls: list):

    game = BowlingGame()

    for i in range(_count_numbers):
        game.roll(rolls[i])

    assert game.score() == expected
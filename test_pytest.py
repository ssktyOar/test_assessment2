import pytest
from bowling_game import BowlingGame

rollsNormal = [10, 3, 6, 5, 5, 8, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
@pytest.mark.parametrize("_count_numbers,expected,rolls", [
    (3, 28, rollsNormal),
    (4, 55, rollsNormal)
    ])
def testGame(_count_numbers: int, expected: int, rolls: list):

    game = BowlingGame()

    for i in range(_count_numbers):
        game.roll(rolls[i])

    assert game.score() == expected

# Testing

# Frames and scoring:
# Frame 1: 10 (Strike)         | 10 + 3 + 6 = 19
# Frame 2: 3, 6                | 9
# Expected: 28
'''
def test_1():
    assert testGame(3) == 28
'''

#test

'''
    Frame 3: 5, 5 (Spare)        | 10 + 8 = 18
    Frame 4: 8, 1                | 9
'''
'''
def test_2():
    assert testGame(3) == 28
'''
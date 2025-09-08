import pytest
from bowling_game import BowlingGame

rolls = [10, 3, 6, 5, 5, 8, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]

def test_game(expectedScore, count):
    global rolls

    game = BowlingGame()

    for i in range(count):
        game.roll(rolls[i])
    assert expectedScore == game.score()


from bowling_game import BowlingGame



def testGame(_count_numbers: int):
    rolls = [10, 3, 6, 5, 5, 8, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]

    game = BowlingGame()

    for i in range(_count_numbers):
        game.roll(rolls[i])

    return game.score()
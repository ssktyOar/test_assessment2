"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """Calculate the score for the current game."""
        score = 0
        roll_index = 0
        frame_index = 0
        print(self.rolls)
        print()
        while True:
            print()
            print("Score: " + str(score))
            if not (roll_index < len(self.rolls)):
                break
            print("Frame index: " + str(roll_index))
            if frame_index == 2:
                frame_index = 0
            if self._is_strike(roll_index): #----- Strike
                if not (roll_index + 2 < len(self.rolls)):
                    break

                print("Strike!")
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
                frame_index = 0
            elif self._is_spare(roll_index) and frame_index == 0: #---- Spare

                if not (roll_index + 2 < len(self.rolls)):
                    print("Final frame index: " + str(roll_index))
                    break              
                print("Spare!")
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
                
                if (roll_index + 1) == len(self.rolls):
                    break
                frame_index = 0
            else: # ----------------------------- Open frame
                score += self.rolls[roll_index]
                print(self.rolls[roll_index])
                roll_index += 1
                frame_index += 1
        print()
        print("Final frame index: " + str(roll_index))
        print("Rolls: " + str(len(self.rolls)))
        return score

    def _is_strike(self, roll_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index):
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        return (self.rolls[roll_index + 1] + self.rolls[roll_index + 2])

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        return self.rolls[frame_index + 2]
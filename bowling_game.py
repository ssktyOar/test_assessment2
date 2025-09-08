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
        """Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """Calculate the score for the current game.
        
        
        This is an explanation of the algorythm.

        Each cycle the roll_index increases by:
            1 if it's a "Strike" or "Open frame"
            2 if it's Spare

        Similarily, frame_index:
            Increases by 1 if it's an "Open frame"
            Resets to 0 if it's a "Strike" or a "Spare"
            Resets to 0 if it's value reaches 2

        The algorythm is as follows:
            If frame_index equals to 2, it's reset to 0

            If it's a "Strike", frame index is reset to 0, index is incremented by 1 
            and "Strike" rules apply to the score

            If current and next rolls together equal to 10, it is considered "Spare",
            in which case frame index is reset to 0, index is incremented by 2 
            and "Spare" rules applied to the score

                However, if during "Spare" frame index is equals to 1, 
                this means that next roll doesn't belong to this frame, 
                therefore it isn't s spare

            If no other conditions are met this considered an "Open frame"
            roll and frame indexes are incremented by 1 
            and value of the current roll simply added to the score
        
        

        Returns:
            The total score of the game
        """
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
        """Check if the roll at roll_index is a strike.

        Args:
            roll_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        """Check if the rolls at roll_index and roll_index + 1 form a spare.

        Args:
            roll_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index):
        """Calculate the bonus for a strike.

        Args:
            roll: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        return (self.rolls[roll_index + 1] + self.rolls[roll_index + 2])

    def _spare_bonus(self, roll_index):
        """Calculate the bonus for a spare.

        Args:
            roll_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        return self.rolls[roll_index + 2]
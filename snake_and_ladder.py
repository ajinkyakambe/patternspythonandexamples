# UC1: Snake and Ladder
# game played with
# single player at start
# position 0

import random


class snake_and_ladder:
    # initial player details
    player_position = 0
    player_name = "Player 1"

    # initial position of the player
    def __init__(self):
        print(self.player_name + ": Starting the game at position:", self.player_position)

    def playGame(self):

        # UC2: The Player rolls the die
        # to get a number between 1 and 6
        # . - Use ((RANDOM)) to get the number

        die_rolling = random.randint(1, 6)
        print("Die after rolling:", die_rolling)




# driving code
snakeladder = snake_and_ladder()
snakeladder.playGame()




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

    def play_game_in_steps(self):

        # UC2: The Player rolls the die
        # to get a number between 1 and 6
        # . - Use ((RANDOM)) to get the number
        print("======================================")
        die_rolling = random.randint(1, 6)
        print("Die after rolling:", die_rolling)

        # UC3: The Player then checks for an Option.
        # They are No Play, Ladder or Snake.
        # - Use ((RANDOM)) to check for Options - In Case of No Play the player stays in the same position
        # - In Case of Ladder the player moves ahead by the
        # number of position received in the die
        #
        # - In Case of Snake the player moves behind

        check_position_move = random.randint(1, 3)
        print("We have to select the move no", check_position_move)

        if check_position_move == 1:
            print("No play")
            print(self.player_name + ": Current player position at:", self.player_position)

        elif check_position_move == 2:
            print("Using Ladder for moving postion by ", die_rolling)
            if self.player_position + die_rolling > 100:
                print("No move played because going above 100")
            else:
                self.player_position += die_rolling
            print(self.player_name + ": Current player position after ladder at:", self.player_position)
        else:
            print("Move the position below because of snake", die_rolling)
            if self.player_position - die_rolling < 0:
                self.player_position = 0
            else:
                self.player_position = self.player_position - die_rolling
            print(self.player_name + ": Current player position after snake at:", self.player_position)
        print("======================================")

    def playGame(self):

        # UC 4 Repeat till the Player
        # reaches the winning
        # position 100. - Note In case the player position moves
        # below 0, then the player restarts from 0

        while self.player_position < 100:
            self.play_game_in_steps()

        print("Game ended")


# driving code
snakeladder = snake_and_ladder()
snakeladder.playGame()



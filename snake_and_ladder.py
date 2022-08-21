# UC1: Snake and Ladder
# game played with
# single player at start
# position 0

import random


class snake_and_ladder:
    # initial player details
    player_position = 0
    player_name = ""
    no_of_times_die_rolled = 0
    replay_flag = True

    # initial position of the player
    def __init__(self, player_name_init):
        self.player_name = player_name_init
        print(self.player_name + ": Starting the game at position:", self.player_position)

    def die_rolling(self):
        self.no_of_times_die_rolled += 1
        die_rolling = random.randint(1, 6)
        return die_rolling


    def play_game_in_steps(self):

        # UC 6 Report the number of
        # times the dice was
        # played to win the game
        # and also the position
        # after every die role

        # UC2: The Player rolls the die
        # to get a number between 1 and 6
        # . - Use ((RANDOM)) to get the number
        print("======================================")
        die_rolled = self.die_rolling()
        print("Die after rolling:", die_rolled)

        # UC3: The Player then checks for an Option.
        # They are No Play, Ladder or Snake.
        # - Use ((RANDOM)) to check for Options - In Case of No Play the player stays in the same position
        # - In Case of Ladder the player moves ahead by the
        # number of position received in the die
        #
        # - In Case of Snake the player moves behind

        check_position_move = random.randrange(1, 3)
        print("We have to select the move no", check_position_move)

        if check_position_move == 1:
            print("No play")
            print(self.player_name + ": current position at:", self.player_position)
            self.replay_flag = False

        elif check_position_move == 2:
            print("Using Ladder for moving position by ", check_position_move)
            if self.player_position + check_position_move > 100:
                print("No move played because going above 100")
            else:
                self.player_position += check_position_move
            self.replay_flag = True
            print(self.player_name + ": current position after ladder at:", self.player_position)
        elif check_position_move == 3:
            print("Move the position below because of snake", check_position_move)
            if self.player_position - check_position_move < 0:
                self.player_position = 0
            else:
                self.player_position = self.player_position - check_position_move
            self.replay_flag = False
            print(self.player_name + ": current position after snake at:", self.player_position)
        print("======================================")

    # to be removed
    def play_game(self):

        # UC 4 Repeat till the Player
        # reaches the winning
        # position 100. - Note In case the player position moves
        # below 0, then the player restarts from 0

        while self.player_position < 100:
            self.play_game_in_steps()
        print("Game ended")
        print("No of times die rolled to play game", self.no_of_times_die_rolled)


# Play the game with 2
# Player. In this case if a
# Player gets a Ladder
# then plays again.
# Finally, report which
# UC 7 Player won the game
def start_multiplayer_game(player1name, player2name):
    snakeladder1 = snake_and_ladder(player1name)
    snakeladder2 = snake_and_ladder(player2name)

    while snakeladder1.player_position < 100 and snakeladder2.player_position < 100:
        if snakeladder1.replay_flag:
            snakeladder1.play_game_in_steps()

        elif snakeladder2.replay_flag:
            snakeladder2.play_game_in_steps()
        else:
            snakeladder1.replay_flag = True
            snakeladder2.replay_flag = True

    print("#########################")
    if snakeladder1.player_position == 100 :
        print("Game ended for", snakeladder1.player_name)
        print("No of times die rolled to play game", snakeladder1.no_of_times_die_rolled)
    else:
        print("Game ended for", snakeladder2.player_name)
        print("No of times 'die rolled' to play game |", snakeladder2.no_of_times_die_rolled, "|")
    print("#########################")


# driving code
start_multiplayer_game("Ajinkya", "Rahul")

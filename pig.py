
if __name__ == "__main__":
    pass
    
# PART 1

import random

def roll_die():
    return random.randint(1, 6)

def player_turn(player_score):
    turn_total = 0
    while True:
        roll = roll_die()
        if roll == 1:
            turn_total = 0
            break
        turn_total += roll
        decision = input(f"Roll again or hold? (r/h) ")
        if decision == 'h':
            break
    return turn_total

def play_game():
    player1_score = 0
    player2_score = 0
    current_player = 1
    while True:
        if current_player == 1:
            print(f"Player 1's turn. Score: {player1_score}")
            turn_total = player_turn(player1_score)
            player1_score += turn_total
            if player1_score >= 100:
                print("Player 1 wins!")
                break
            current_player = 2
        else:
            print(f"Player 2's turn. Score: {player2_score}")
            turn_total = player_turn(player2_score)
            player2_score += turn_total
            if player2_score >= 100:
                print("Player 2 wins!")
                break
            current_player = 1

play_game()

# PART 2
class Game:
    def __init__(self, player1, player2, die):
        self.player1 = player1
        self.player2 = player2
        self.die = die
        self.current_player = player1

    def play(self):
        while True:
            self.current_player.take_turn(self.die)
            if self.current_player.score >= 100:
                print(f"{self.current_player.name} wins!")
                break
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
--------------------------------------------------------------------------------------
player1 = Player("Player 1")
player2 = Player("Player 2")
die = Die()
game = Game(player1, player2, die)
game.play()

# PART 3
import random
random.seed(0)
---------------------------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_turn(self, die):
        turn_total = 0
        while True:
            roll = die.roll()
            if roll == 1:
                turn_total = 0
                break
            turn_total += roll
            decision = input(f"{self.name}, roll again or hold? (r/h) ")
            if decision == 'h':
                break
            elif decision != 'r':
                print("Invalid input. Please enter 'r' to roll again or 'h' to hold.")
        self.score += turn_total

# PART 4
class Game:
    def __init__(self, player1, player2, die):
        self.player1 = player1
        self.player2 = player2
        self.die = die
        self.current_player = player1

    def play(self):
        while True:
            self.current_player.take_turn(self.die)
            if self.current_player.score >= 100:
                print(f"{self.current_player.name} wins!")
                break
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_turn(self, die):
        turn_total = 0
        while True:
            roll = die.roll()
            print(f"You rolled a {roll}.")
            if roll == 1:
                turn_total = 0
                break
            turn_total += roll
            print(f"Turn total: {turn_total}")
            print(f"Total score: {self.score}")
            decision = input(f"{self.name}, roll again or hold? (r/h) ")
            if decision == 'h':
                break
            elif decision != 'r':
                print("Invalid input. Please enter 'r' to roll again or 'h' to hold.")
        self.score += turn_total
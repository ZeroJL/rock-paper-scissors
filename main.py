import player
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def game_score(self):
        print("Game Score")
        print(f"Player 1 - Win: {self.p1.win} Loose: {self.p1.loose} Draw: {self.p1.draw}")
        print(f"Player 2 - Win: {self.p2.win} Loose: {self.p2.loose} Draw: {self.p1.draw}")
        if self.p1.win > self.p2.win:
            print("Winner is Player1!")
        elif self.p2.win > self.p1.win:
            print("Winner is Player2!")
        else:
            print("Draw! There is no Winner")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 Win!")
            self.p1.win += 1
            self.p2.loose += 1
        elif beats(move2, move1):
            print("Player 2 Win!")
            self.p2.win += 1
            self.p1.loose += 1
        else:
            print("Draw!")
            self.p1.draw += 1
            self.p2.draw += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print("Game start!")
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        self.game_score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(player.HumanPlayer(),
                random.choice([player.Player(), player.CyclePlayer(), player.ReflectPlayer(), player.RandomPlayer()]))
    game.play_game(4)

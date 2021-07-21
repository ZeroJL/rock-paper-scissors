import random


class Player:
    l = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.win = 0
        self.loose = 0
        self.draw = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(self.l)


class HumanPlayer(Player):

    def move(self):
        return

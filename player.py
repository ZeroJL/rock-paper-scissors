import random


class Player:
    move_list = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.win = 0
        self.loose = 0
        self.draw = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.move_dictionary = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        self.next_move = random.choice(self.move_list)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = random.choice(self.move_list)


class HumanPlayer(Player):
    def move(self):
        while True:
            user_move = input("rock / paper / scissors\n")
            if user_move in ["rock", "paper", "scissors"]:
                return user_move
            print("Try again")

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(RandomPlayer):
    def learn(self, my_move, their_move):
        self.next_move = self.move_dictionary.get(my_move)


class OppositePlayer(RandomPlayer):
    def learn(self, my_move, their_move):
        self.next_move = self.move_dictionary.get(their_move)


class CyclePlayer(RandomPlayer):
    def learn(self, my_move, their_move):
        self.next_move = self.move_dictionary.get(my_move)


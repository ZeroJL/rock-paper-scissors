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
        self.next_move = self.move()

    def move(self):
        return random.choice(self.move_list)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            user_move = input("rock / parser / scissors\n")
            if user_move in ["rock", "paper", "scissors"]:
                break
            print("Wrong Input")
        return


class ReflectPlayer(RandomPlayer):
    def learn(self, my_move, their_move):
        self.next_move = self.move_dictionary.get(their_move)

    def move(self):
        return self.next_move


class CyclePlayer(RandomPlayer):
    def learn(self, my_move, their_move):
        self.next_move = self.move_dictionary.get(my_move)

    def move(self):
        return self.next_move

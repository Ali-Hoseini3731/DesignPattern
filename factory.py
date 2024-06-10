from abc import ABC, abstractmethod
from random import choice


class BasePlayer(ABC):
    choices = ["r", "p", "s"]

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(BasePlayer):
    def move(self):
        m = input("chose you next move from in [r, p, s]: ")
        return m


class SystemPlayer(BasePlayer):
    def move(self):
        return choice(self.choices)


class Game:
    @staticmethod
    def start_game():
        game_type = input("enter 's' for single and 'm' for multi player: ")
        if game_type == "s":
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == "m":
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print("invalid input")
            p1 = None
            p2 = None
        return p1, p2


if __name__ == "__main__":
    player1, player2 = Game.start_game()

    for player in [player1, player2]:
        print(player.move())


from random import randint


def check_permision(func):
    def wrapped_func(obj, user):
        if obj.turn == user:
            return func(obj, user)
        return f"Mr {user.name} is not your turn"

    return wrapped_func


class User:
    def __init__(self, name):
        self.name = name


class Dice:
    @staticmethod
    def roll():
        return randint(1, 6)


class Game:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.turn = user1
        self.dice = Dice

    def change_turn(self):
        self.turn = self.user2 if self.turn == self.user1 else self.user1

    @check_permision
    def roll_dice(self, user):
        self.change_turn()
        return f"Mr {user.name} is : {self.dice.roll()}"


if __name__ == "__main__":
    user1 = User("Ali")
    user2 = User("sajad")
    game = Game(user1, user2)

    print(game.roll_dice(user1))
    print(game.roll_dice(user1))
    print(game.roll_dice(user2))
    print(game.roll_dice(user2))
    print(game.roll_dice(user1))
    print(game.roll_dice(user2))
    print(game.roll_dice(user2))

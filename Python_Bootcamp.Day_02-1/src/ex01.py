from collections import Counter
from itertools import combinations


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def move(self, player, previous_move, count_match):
        if str(player) in ("cheater", 'cooperator'):
            player.make_move()
        elif str(player) in ("copycat", "grudger"):
            player.make_move(previous_move)
        elif str(player) == 'detective':
            player.make_move(previous_move, count_match)
        else:
            player.make_move(previous_move, count_match == self.matches - 1)

    def candy_counter(self, player1, player2) -> None:
        if player1.move == "cooperate" and player2.move == "cooperate":
            self.registry[str(player1)] += 2
            self.registry[str(player2)] += 2
        elif player1.move == "cooperate" and player2.move == "cheat":
            self.registry[str(player1)] -= 1
            self.registry[str(player2)] += 3
        elif player1.move == "cheat" and player2.move == "cooperate":
            self.registry[str(player1)] += 3
            self.registry[str(player2)] -= 1

    def play(self, player1, player2):
        for match in range(self.matches):
            previous_move1 = player1.move
            previous_move2 = player2.move
            self.move(player1, previous_move2, match)
            self.move(player2, previous_move1, match)
            self.candy_counter(player1, player2)
        player1.clear()
        player2.clear()

    def top3(self):
        for elem in self.registry.most_common(3):
            player, candies = elem
            print(player, candies)
        # print top three


class Player:
    def __init__(self) -> None:
        self.move = None

    def cheat(self) -> None:
        self.move = "cheat"

    def cooperate(self) -> None:
        self.move = "cooperate"

    def clear(self) -> None:
        self.move = None


class Cheater(Player):
    def make_move(self) -> None:
        self.cheat()

    def __str__(self) -> str:
        return "cheater"


class Cooperator(Player):
    def make_move(self) -> None:
        self.cooperate()

    def __str__(self) -> str:
        return "cooperator"


class Copycat(Player):
    def make_move(self, previous_player) -> None:
        if not previous_player or previous_player == "cooperate":
            self.cooperate()
        else:
            self.cheat()

    def __str__(self) -> str:
        return "copycat"


class Grudger(Player):
    def make_move(self, previous_player) -> None:
        if self.move == "cheat" or previous_player == "cheat":
            self.cheat()
        else:
            self.cooperate()

    def __str__(self) -> str:
        return "grudger"


class Detective(Player):
    def __init__(self) -> None:
        super().__init__()
        self.is_cheater: bool = False

    def make_move(self, previous_player, round_count) -> None:
        if previous_player == "cheat":
            self.is_cheater = True
        if round_count < 4:
            if round_count == 1:
                self.cheat()
            else:
                self.cooperate()
        elif self.is_cheater:
            Copycat.make_move(self, previous_player)
        else:
            self.cheat()

    def clear(self) -> None:
        super().clear()
        self.is_cheater = False

    def __str__(self) -> str:
        return "detective"


class SomePlayer(Copycat):
    def make_move(self, previous_player, is_last_round):
        if not is_last_round:
            super().make_move(previous_player)
        else:
            self.cheat()

    def __str__(self):
        return "somePlayer"


if __name__ == '__main__':
    print('      ТОП-3 когда есть все типы игроков:')
    game = Game()
    players = [Copycat(), Cheater(), Cooperator(),
               Grudger(), Detective(), SomePlayer()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    game.top3()

    print('      ТОП-3 Для (Copycat Cheater Cooperator Grudger Detective):')
    game = Game()
    players = [Copycat(), Cheater(), Cooperator(),
               Grudger(), Detective()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    game.top3()

    print('      ТОП-3 Для (Cheater Cooperator):')
    game = Game()
    players = [Cheater(), Cooperator()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    game.top3()

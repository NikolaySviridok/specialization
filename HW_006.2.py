# Задание 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей 
# на доске, определите, есть ли среди них пара бьющих друг 
# друга. Программа получает на вход восемь пар чисел, каждое 
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют 
# друг друга верните истину, а если бьют - ложь.

import random
from copy import copy


class FerziBoard:
    def __init__(self, length: int):
        self.length = length
        self.board = []
        self.all_variants = []
        self._place_next_ferz(0)

    def _can_we_place(self, row: int, num: int):
        for i, value in enumerate(self.board):
            if value == num or (i - row) == (value - num) or (i - row) == (num - value):
                return False
        return True

    def _place_next_ferz(self, row: int):
        if row == self.length:
            self.all_variants.append(copy(self.board))
        else:
            for col in range(self.length):
                if self._can_we_place(row, col):
                    self.board.append(col)
                    self._place_next_ferz(row + 1)
                    self.board.pop()

    def check(self, board: list[int]):
        return board in self.all_variants


def get_random_board(board=[0, 1, 2, 3, 4, 5, 6, 7]):
    random.shuffle(board)
    return board


if __name__ == '__main__':
    length_of_board = 8
    my_boards = FerziBoard(length_of_board)
    print(my_boards.all_variants)
    get_board_from_user = [0] * length_of_board
    for count in range(length_of_board):
        row, col = (int(i) - 1 for i in input(f"Введите пару координат № {count + 1} через пробел: ").split(" "))
        get_board_from_user[col] = row
    print(get_board_from_user)
    print(my_boards.check(get_board_from_user))
    count = 0
    while count < 4:
        random_board = get_random_board()
        if my_boards.check(random_board):
            print(random_board)
            count += 1
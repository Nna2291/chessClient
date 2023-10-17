from string import ascii_uppercase
from typing import Union

from colorama import Fore, Style

from src.exceptions import ImpossibleMoveException
from src.figures.figure import Figure
from src.figures.pawn import Pawn
from src.services import check_index


class Board:

    def __init__(self):
        self.len_x = 8
        self.len_y = 8
        self.current_game = []
        for i in range(self.len_y):
            self.current_game.append(['*'] * self.len_x)
        self.current_game[1] = [Pawn(False)] * self.len_x
        self.current_game[-2] = [Pawn()] * self.len_x

    def __getitem__(self, index) -> Union[str, Figure]:
        """
        Get figure from board

        To get figure from board, index them by this way

        board['e8']
        board['d1']

        :param index:
        :return: Figure from board

        :raises:
            BadIndexException: if index is not correct
        """
        x, y = check_index(index)
        return self.current_game[self.len_y - y - 1][x]

    def __setitem__(self, index, value):
        """
        Set figure to board

        To set figure to board, index them by this way

        board['e8'] = 'B'
        board['d1'] = 'P'

        :param index:
        :param value:
        :return: Set figure on board

        :raises:
            BadIndexException: if index is not correct
        """
        x, y = check_index(index)
        self.current_game[self.len_y - y - 1][x] = value

    def __str__(self):
        """
        Return pretty printed board
        :return:
        """
        game = []
        for el in range(self.len_y):
            row = self.current_game[el].copy()
            row = list(map(str, row))
            row.insert(0, str(self.len_y - el))
            row[0] = f"{Fore.GREEN}{row[0]}{Style.RESET_ALL}"
            game.append(row)
        letters = [f'{Fore.GREEN}$'] + list(ascii_uppercase[:self.len_x]) + [Style.RESET_ALL]
        game.append(letters)
        return '\n'.join([str(' '.join(
            elem
        )) for elem in game])

    def set_available_spaces(self, index: str) -> None:
        """
        Set available spaces for figure

        :param index:
        :return: None
        """
        x, y = check_index(index)
        spaces = self[index].calculate_moves(y, x)
        for space in spaces:
            self[space] = '^'

    def make_move(self, old_index: str, new_index: str) -> None:
        x, y = check_index(old_index)
        spaces = self[old_index].calculate_moves(y, x)
        if new_index not in spaces:
            raise ImpossibleMoveException()
        for space in spaces:
            self[space] = '*'
        self[new_index] = self[old_index]
        self[old_index] = '*'

    def show(self):
        print("\033c", end="")
        print(self)

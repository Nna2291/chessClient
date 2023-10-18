from string import ascii_uppercase, ascii_lowercase
from typing import Union

from colorama import Fore, Style

from src.exceptions import ImpossibleMoveException, NotAFigureException, NotYourFigureException
from src.figures.bishop import Bishop
from src.figures.figure import Figure
from src.figures.knight import Knight
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
        self['c1'] = Bishop()
        self['f1'] = Bishop()
        self['c8'] = Bishop(False)
        self['f8'] = Bishop(False)

        self['b1'] = Knight()
        self['g1'] = Knight()
        self['b8'] = Knight(False)
        self['g8'] = Knight(False)

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
        return self.current_game[y][x]

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
        self.current_game[y][x] = value

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

    def get_by_index(self, y: int, x: int):
        return self.current_game[y][x]

    def is_figure(self, index):
        return Figure in self[index].__class__.__bases__

    def set_available_spaces(self, index: str, color: bool) -> list[str]:
        """
        Set available spaces for figure

        :param color:
        :param index:
        :return: None
        """
        x, y = check_index(index)
        if not self.is_figure(index):
            raise NotAFigureException
        if not self[index].check_color(color):
            raise NotYourFigureException
        spaces = self[index].calculate_moves(y, x, self)
        for space in spaces:
            if self.is_figure(space):
                pass
            else:
                self[space] = '^'
        return spaces

    def make_move(self, old_index: str, new_index: str, color: bool) -> None:
        x, y = check_index(old_index)
        if not self[old_index].check_color(color):
            raise NotYourFigureException
        spaces = self[old_index].calculate_moves(y, x, self)
        if new_index not in spaces:
            raise ImpossibleMoveException()
        if type(self[new_index]) != str and self[new_index].check_color(color):
            raise ImpossibleMoveException()
        for space in spaces:
            if not self.is_figure(space):
                self[space] = '*'
        self[new_index] = self[old_index]
        self[old_index] = '*'

    def show(self, spaces: list[str]):
        print("\033c", end="")
        print(self)
        print(spaces)

from string import ascii_uppercase
from typing import Union

from colorama import Fore, Style

from src.exceptions import ImpossibleMoveException, NotAFigureException, NotYourFigureException
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

    def is_figure(self, index):
        return Figure in self[index].__class__.__bases__

    def get_pawn_spaces(self, index: str, x: int, y: int):
        spaces = []
        for el in self[index].calculate_moves(y, x):
            if not self.is_figure(el):
                spaces.append(el)
            else:
                break
        for el in self[index].calculate_beat(y, x):
            if self.is_figure(el):
                spaces.append(el)
        return spaces

    def set_available_spaces(self, index: str, color: bool) -> bool:
        """
        Set available spaces for figure

        :param index:
        :return: None
        """
        x, y = check_index(index)
        if not self.is_figure(index):
            raise NotAFigureException
        if not self[index].check_color(color):
            raise NotYourFigureException
        spaces = self[index].calculate_moves(self, index, y, x)
        if type(self[index]) == Pawn:
            spaces = self.get_pawn_spaces(index, x, y)
        for space in spaces:
            if self.is_figure(space):
                pass
            else:
                self[space] = '^'
        return bool(spaces)

    def make_move(self, old_index: str, new_index: str, color: bool) -> None:
        x, y = check_index(old_index)
        if not self[old_index].check_color(color):
            raise NotYourFigureException
        spaces = self[old_index].calculate_moves(y, x)
        if type(self[old_index]) == Pawn:
            spaces = self.get_pawn_spaces(old_index, x, y)
        if new_index not in spaces:
            raise ImpossibleMoveException()
        for space in spaces:
            if not self.is_figure(space):
                self[space] = '*'
        self[new_index] = self[old_index]
        self[old_index] = '*'

    def show(self):
        print("\033c", end="")
        print(self)

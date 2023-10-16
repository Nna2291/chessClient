from string import ascii_lowercase

from exceptions import *


class Board:

    def __init__(self):
        self.len_x = 8
        self.len_y = 8
        self.current_game = [[''] * self.len_x] * self.len_y

    @staticmethod
    def __check_index(index) -> (int, int):
        if len(index) != 2:
            raise BadIndexException()
        if not index[0].isalpha() or not index[1].isdigit():
            raise BadIndexException()
        x = ascii_lowercase.index(index[0].lower())
        y = int(index[1]) - 1
        if not 0 <= x <= 7 and not 0 <= y <= 7:
            raise ImpossibleIndexException()
        return x, y

    def __getitem__(self, index) -> str:
        """
        Get figure from board

        To get figure from board, index them by this way

        board['e8']
        board['d1']

        :param index:
        :return: Figure from board
        """
        x, y = self.__check_index(index)
        return self.current_game[x][y]

    def __setitem__(self, index, value):
        """
        Set figure to board

        To set figure to board, index them by this way

        board['e8'] = 'B'
        board['d1'] = 'P'

        :param index:
        :param value:
        :return: Set figure on board
        """
        x, y = self.__check_index(index)
        if value.lower() in 'kqbrp':
            self.current_game[x][y] = value.upper()
            return
        raise BadFigureException()


b = Board()
b['d3'] = 'b'
print(b['d3'])

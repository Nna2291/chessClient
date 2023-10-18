from typing import Union

from colorama import Fore, Style

import src.board


class Figure(object):
    def __init__(self, letter: str, blue: bool = True):
        self.blue = blue
        self.__letter = letter

        if self.blue:
            self.__string = f'{Fore.BLUE}{self.__letter}{Style.RESET_ALL}'
        else:
            self.__string = f'{Fore.RED}{self.__letter}{Style.RESET_ALL}'

    def __str__(self):
        return self.__string

    @staticmethod
    def check_moves(indexes: list[tuple[int, int]]):
        indexes = list(filter(lambda x: 0 <= x[0] <= 7 and 0 <= x[1] <= 7,
                              indexes))
        return indexes

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        pass

    def calculate_beat(self, y: int, x: int) -> list[tuple[int, int]]:
        pass

    def check_color(self, color: bool):
        return color == self.blue

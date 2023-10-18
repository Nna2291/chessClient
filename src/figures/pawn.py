from typing import TYPE_CHECKING

from .figure import Figure
from ..services import get_letter_index

if TYPE_CHECKING:
    from ..board import Board


class Pawn(Figure):
    def __init__(self, blue: bool = True):
        super().__init__('P', blue)

    @staticmethod
    def get_pawn_spaces(board: 'Board', index: str, x: int, y: int):
        spaces = []
        for el in board[index].calculate_moves(y, x):
            if not board.is_figure(el):
                spaces.append(el)
            else:
                break
        for el in board[index].calculate_beat(y, x):
            if board.is_figure(el):
                spaces.append(el)
        return spaces

    def calculate_moves(self, y: int, x: int) -> list[str]:
        indexes = []
        if self.blue:
            if y == 1:
                indexes.append((y + 2, x))
            indexes.append((y + 1, x))
        else:
            if y == 6:
                indexes.append((y - 2, x))
            indexes.append((y - 1, x))
        indexes = self.check_moves(indexes)
        return sorted(get_letter_index(x, y) for y, x in indexes)

    def calculate_beat(self, y: int, x: int) -> list[str]:
        if self.blue:
            indexes = [(y + 1, x + 1), (y + 1, x - 1)]
        else:
            indexes = [(y - 1, x + 1), (y - 1, x - 1)]
        indexes = self.check_moves(indexes)
        return [get_letter_index(x, y) for y, x in indexes]

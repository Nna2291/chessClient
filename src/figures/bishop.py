from typing import TYPE_CHECKING

from .figure import Figure
from ..services import get_letter_index

if TYPE_CHECKING:
    from ..board import Board


class Bishop(Figure):
    def __init__(self, blue: bool = True):
        super().__init__('B', blue)

    @staticmethod
    def calculate_moves(board: 'Board', index: str, y: int, x: int) -> list[tuple[int, int]]:
        indexes = [[(x + i, y + i) for i in range(8)], [(x + i, y - i) for i in range(8)],
                   [(x - i, y + i) for i in range(8)], [(x - i, y - i) for i in range(8)]]
        spaces = []
        for direction in indexes:
            for indexes in direction:
                x, y = indexes[0], indexes[1]
                index = get_letter_index(x, y)
                if board[index].is_figure():
                    break
                spaces.append(index)
        return spaces
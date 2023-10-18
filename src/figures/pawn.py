from .figure import Figure
from ..services import get_letter_index


class Pawn(Figure):
    def __init__(self, blue: bool = True):
        super().__init__('P', blue)

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

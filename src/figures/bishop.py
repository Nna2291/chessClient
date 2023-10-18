import src.board
from .figure import Figure
from ..services import get_letter_index


class Bishop(Figure):
    def __init__(self, color: bool = True):
        super().__init__('B', color)

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        indexes = [
            self.check_moves([(y - i, x - i) for i in range(1, 8)]),
            self.check_moves([(y - i, x + i) for i in range(1, 8)]),
            self.check_moves([(y + i, x - i) for i in range(1, 8)]),
            self.check_moves([(y + i, x + i) for i in range(1, 8)])
        ]

        answer = []

        for direction in indexes:
            for new_y, new_x in direction:
                if type(board.get_by_index(new_y, new_x)) != str:
                    answer.append((new_y, new_x))
                    break
                answer.append((new_y, new_x))

        answer = self.check_moves(answer)
        return [get_letter_index(x, y) for y, x in answer]

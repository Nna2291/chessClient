from typing import TYPE_CHECKING

from .figure import Figure
from ..services import get_letter_index

if TYPE_CHECKING:
    from ..board import Board


class Bishop(Figure):
    def __init__(self, blue: bool = True):
        super().__init__('B', blue)

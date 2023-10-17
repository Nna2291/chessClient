from src.board import Board
from src.exceptions import BadIndexException, ImpossibleMoveException
from src.services import check_index

b = Board()
b.show()

while True:
    index = input('Enter figure index: ').lower()
    # index = 'e2'

    try:
        x, y = check_index(index)
        break
    except BadIndexException:
        b.show()
        print('Invalid index!')

b.set_available_spaces(index)
b.show()

while True:
    new_index = input('Enter new index for figure: ').lower()

    # index = 'e5'
    try:
        b.make_move(index, new_index)
        b.show()
    except ImpossibleMoveException:
        b.show()
        print('Impossible move!')

from src.board import Board
from src.exceptions import BadIndexException, NotAFigureException, ImpossibleMoveException, NotYourFigureException
from src.services import check_index


def play_game(b: Board, color: bool):
    while True:
        index = input('Enter figure index: ').lower()
        try:
            check_index(index)
            spaces = b.set_available_spaces(index, color)
            assert spaces
            b.show()
            break
        # except BadIndexException:
        #     print('Invalid index!')
        except NotAFigureException:
            print('This is not a figure!')
        except NotYourFigureException:
            print('This is not your figure!')
        except AssertionError:
            print('You cant move this figure!')

    while True:
        new_index = input('Enter new index for figure: ').lower()
        try:
            b.make_move(index, new_index, color)
            b.show()
            break
        except ImpossibleMoveException:
            b.show()
            print('Impossible move!')

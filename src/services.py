from string import ascii_lowercase

from src.exceptions import BadIndexException


def get_letter_index(x: int, y: int) -> str:
    index = f'{ascii_lowercase[x]}{y + 1}'
    return index


def check_index(index) -> (int, int):
    """

    :param index:
    :return:

    :raises:
        BadIndexException: if index is not correct
    """
    if len(index) != 2:
        raise BadIndexException()
    if not index[0].isalpha() or not index[1].isdigit():
        raise BadIndexException()
    x = ascii_lowercase.index(index[0].lower())
    y = int(index[1]) - 1
    if not 0 <= x <= 7 and not 0 <= y <= 7:
        raise BadIndexException()
    return x, y

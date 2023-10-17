from colorama import Fore, Style


class Figure:
    def __init__(self, letter: str, blue: bool = True):
        self.blue = blue
        self.__letter = letter

    def __str__(self):
        if self.blue:
            return f'{Fore.BLUE}{self.__letter}{Style.RESET_ALL}'
        return f'{Fore.RED}{self.__letter}{Style.RESET_ALL}'

    def __repr__(self):
        if self.blue:
            return f'{Fore.BLUE}{self.__letter}{Style.RESET_ALL}'
        return f'{Fore.RED}{self.__letter}{Style.RESET_ALL}'

    def calculate_moves(self, y: int, x: int) -> list[tuple[int, int]]:
        pass

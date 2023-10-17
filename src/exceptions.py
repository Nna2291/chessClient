class BadIndexException(BaseException):
    def __str__(self) -> str:
        return 'Impossible way to index figure'


class ImpossibleIndexException(BaseException):
    def __str__(self) -> str:
        return 'Impossible index'


class BadFigureException(BaseException):
    def __str__(self) -> str:
        return 'Impossible name for figure'


class ImpossibleMoveException(BaseException):
    def __str__(self) -> str:
        return 'Impossible move'


class BadLetterException(BaseException):
    def __str__(self) -> str:
        return 'Incorrect Letter'

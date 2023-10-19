from src.board import Board
from src.game import play_game

b = Board()
b.show([])
i = 0
while True:
    color = i % 2 == 0
    play_game(b, color)
    i += 1
    if b.is_mate(i):
        if (i - 1) % 2 == 0:
            color = 'blue'
        else:
            color = 'red'
        b.show([], message=f'Mate! {color} wins!')
        break

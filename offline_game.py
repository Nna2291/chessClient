from src.board import Board
from src.game import play_game

b = Board()
b.show([])
i = 0
while True:
    color = i % 2 == 0
    play_game(b, color)

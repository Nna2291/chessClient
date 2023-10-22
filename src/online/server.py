import socketserver
import sys

from src.board import Board
from src.exceptions import *
from src.game import set_figure, place_figure, play_game


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        color = self.server.color
        b = self.server.board
        data = self.request.recv(1024).strip()
        data = data.decode('utf-8')
        print(data)
        if 'check' not in data.lower() and data:
            blue_ind, blue_new = data.split(';')[2], data.split(';')[3]
            place_figure(b, not color, blue_ind, blue_new)
            if b.is_mate(color):
                if color:
                    col = 'red'
                else:
                    col = 'blue'
                b.show([], message=f'Mate! {col} wins!')
                sys.exit(1)
            index, new_index = play_game(b, color)
            answer = f'MOVE;{index};{new_index}'
            self.request.sendall(bytes(answer, 'utf-8'))
        else:
            self.request.sendall(bytes('OK', 'utf-8'))

import socket
import socketserver
import time

from src.board import Board
from src.game import place_figure, play_game
from src.online.server import MyTCPHandler

PORT = int(input('Enter free port: '))

# print(f'Your addr is {socket.gethostbyname(socket.getfqdn())}:{PORT}')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = s.getsockname()[0]
print(f'Your addr is {HOST}:{PORT}')
HOST = '0.0.0.0'
s.close()
is_host = input('Are u host? [y/n]: ')

b = Board()
if is_host == 'n':
    color = True
    ip_second = input('Enter ip of HOST player: ')
    host, port = ip_second.split(':')
    port = int(port)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(60 * 60)
            sock.connect((host, port))
            quer = f'CHECK;{ip_second}'
            sock.sendall(bytes(quer, 'utf-8'))
            response = sock.recv(1024 * 8)
            response = response.decode('utf-8')
            if 'OK' in response:
                break
            raise socket.error
        except socket.error:
            print(f'Waiting for {ip_second}')
            time.sleep(3)
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(60 * 60)
        sock.connect((host, port))
        index, new_index = play_game(b, color)
        quer = f'MOVE;{ip_second};{index};{new_index}'
        sock.sendall(bytes(quer, 'utf-8'))
        response = str(sock.recv(1024), 'utf-8')
        red_ind, red_new = response.split(';')[1], response.split(';')[2]
        place_figure(b, not color, red_ind, red_new)
        if b.is_mate(not color):
            if color:
                col = 'blue'
            else:
                col = 'red'
            b.show([], message=f'Mate! {col} wins!')
else:
    color = False
    print('Waiting for connection')
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.color = color
        server.board = b
        server.serve_forever()

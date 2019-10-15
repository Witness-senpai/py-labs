import socket
import random

s = socket.socket()
s.connect(socket.gethostname(), 1234)

while True:
    if s.recv(1024).decode('utf-8') == 'go':
        pass
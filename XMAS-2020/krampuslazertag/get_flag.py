#!/usr/bin/env python3
from pwn import *

def r(a):
    a = a % 2
    if a > 1:
       a = 2 - a
    return a

def evaluator(x1, y1, x2, y2):
    xb = [(x1 + i + (x2 if i % 2 == 0 else 1 - x2)) / 2 for i in range(4)]
    yb = [(y1 + i + (y2 if i % 2 == 0 else 1 - y2)) / 2 for i in range(4)]

    position = []
    for x in xb:
        for y in yb:
            position.append([r(x), r(y)])
    
    return position

io = remote('challs.xmas.htsp.ro', 6005)

io.sendline('_')

for i in range(50):
    data = ''
    
    io.recvuntil('Your position: ')
    player_position = io.recvline().strip().decode()
    x2 = float(player_position.split(',')[0])
    y2 = float(player_position.split(',')[1])
    
    io.recvuntil('Krampus\' position: ')
    krampus_position = io.recvline().strip().decode()
    x1 = float(krampus_position.split(',')[0])
    y1 = float(krampus_position.split(',')[1])
    
    coordinates_list = evaluator(x1, y1, x2, y2)
    
    for position in coordinates_list:
        data += str(position[0]) + ',' + str(position[1])
        data += '\n'
    
    io.send(data)

io.interactive()
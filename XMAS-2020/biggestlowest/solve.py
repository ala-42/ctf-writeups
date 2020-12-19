#!/usr/bin/env python3
from pwn import *
import time

io = remote('challs.xmas.htsp.ro', 6051)

start_time = time.time()

for i in range(50):
	log.success(i)
	
	answer = ''
	
	io.recvuntil('array = ')
	array1 = (io.recvline().decode()[1:-2]).split(', ')
	array2 = array1.copy()
	print('code running time: %s' % (time.time() - start_time))
	io.recvuntil('k1 = ')
	k1 = int(io.recvline().decode().strip())

	io.recvuntil('k2 = ')
	k2 = int(io.recvline().decode().strip())
	
	array1.sort(key = int, reverse = False)
	array2.sort(key = int, reverse = True)

	for k in range(k1):
		answer += array1[k]
		if (k != k1 - 1):
			answer += ', '
		else:
			answer += '; '
		
	
	for k in range(k2):
		answer += array2[k]
		if (k != k2 - 1):
			answer += ', '
	
	io.sendline(answer)

io.interactive()

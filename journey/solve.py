from pwn import *

s = remote("p1.tjctf.org",8009)
s.sendline("one")
lastText = ''
while(1):
	try:
		s.recvuntil("'")
		lastText = s.recvuntil("'")[:-1]
		s.recvuntil(":")
		s.sendline(lastText)
		print lastText
	except:
		s.close()
		s = remote("p1.tjctf.org",8009)

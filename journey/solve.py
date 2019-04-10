from pwn import *

s = remote("p1.tjctf.org",8009)
s.sendline("drama")
lastText = ''
while(1):
	try:
		s.recvuntil("'")
		lastText = s.recvuntil("'")[:-1]
		s.recvuntil(":")
		s.sendline(lastText)
		print lastText
		if lastText.startswith("tjctf"):
			break
	except:
		s.close()
		s = remote("p1.tjctf.org",8009)
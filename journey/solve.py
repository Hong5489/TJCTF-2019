from pwn import *

s = remote("p1.tjctf.org",8009)
<<<<<<< HEAD
s.sendline("drama")
=======
s.sendline("one")
>>>>>>> 11abc4a8a9282cb83bb75dc308f663431086e76a
lastText = ''
while(1):
	try:
		s.recvuntil("'")
		lastText = s.recvuntil("'")[:-1]
		s.recvuntil(":")
		s.sendline(lastText)
		print lastText
<<<<<<< HEAD
		if lastText.startswith("tjctf"):
			break
	except:
		s.close()
		s = remote("p1.tjctf.org",8009)
=======
	except:
		s.close()
		s = remote("p1.tjctf.org",8009)
>>>>>>> 11abc4a8a9282cb83bb75dc308f663431086e76a

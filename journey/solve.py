from pwn import *

s = remote("p1.tjctf.org",8009)
f = open("wordList.txt",'w+')
s.sendline("empress")
while(1):
	s.recvuntil("'")
	text = s.recvuntil("'")[:-1]
	f.write(text+'\n')
	s.recvuntil(":")
	s.sendline(text)
	print text
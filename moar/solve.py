import requests
import re
import random
from threading import Thread
from threading import activeCount
import os
import signal

remainPath = []
url = "https://moar_horse_2.tjctf.org"
startUrl = "/4b043a01-a4b7-4141-8a99-fc94fe7e3778.html"
r = requests.get(url+startUrl)
path = []
allowed = False
def monitor():
	global allowed
	while(1):
		if activeCount() <= 600:
			allowed = True
		else:
			allowed = False

def newThread(start,r):
	while(1):
		if re.findall("tjctf{.*}",r.text):
			print start
			print re.findall("tjctf{.*}",r.text)[0]
			os.kill(os.getpid(), signal.SIGKILL)

		back = re.findall("/.*.html",r.text.split('\n')[14].strip())[0]
		forward = re.findall("/.*.html",r.text.split('\n')[15].strip())[0]
		path.append(start)
		print len(path)
		if back not in path and forward not in path:
			if allowed:
				r = requests.get(url+back)
				thread = Thread(target=newThread,args=(back,r))
				thread.start()
				r = requests.get(url+forward)
				start = forward
			else:
				if random.randint(0,1) == 0:
					r = requests.get(url+back)
					start = back
					remainPath.append(forward)
				else:
					r = requests.get(url+forward)
					start = forward
					remainPath.append(back)
		elif back not in path:
			r = requests.get(url+back)
			start = back
		elif forward not in path:
			r = requests.get(url+forward)
			start = forward
		else:
			for rmp in remainPath:
				if allowed:
					remainPath.remove(rmp)
					r = requests.get(url+rmp)
					thread = Thread(target=newThread,args=(rmp,r))
					thread.start()
			break

monitorThread = Thread(target=monitor)
monitorThread.start()
newThread(startUrl,r)
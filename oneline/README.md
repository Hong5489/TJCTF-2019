## Python in One Line
Written by boomo

It's not code golf but it's something...

This is printed when you input the flag: `.. - / .. ... -. - / -- --- .-. ... / -.-. --- -.. .`

We're given this one liner:
```python
print(' '.join([{'a':'...-', 'b':'--..', 'c':'/', 'd':'-.--', 'e':'.-.', 'f':'...', 'g':'.-..', 'h':'--', 'i':'---', 'j':'-', 'k':'-..-', 'l':'-..', 'm':'..', 'n':'.--', 'o':'-.-.', 'p':'--.-', 'q':'-.-', 'r':'.-', 's':'-...', 't':'..', 'u':'....', 'v':'--.', 'w':'.---', 'y':'..-.', 'x':'..-', 'z':'.--.', '{':'-.', '}':'.'}[i] for i in input('What do you want to secrify? ')]))
```

It's easy using Dictionary in Python:
```python
text = '.. - / .. ... -. - / -- --- .-. ... / -.-. --- -.. .'.split(' ')

d = {'a':'...-', 'b':'--..', 'c':'/', 'd':'-.--', 'e':'.-.', 'f':'...', 'g':'.-..', 'h':'--', 'i':'---', 'j':'-', 'k':'-..-', 'l':'-..', 'm':'..', 'n':'.--', 'o':'-.-.', 'p':'--.-', 'q':'-.-', 'r':'.-', 's':'-...', 't':'..', 'u':'....', 'v':'--.', 'w':'.---', 'y':'..-.', 'x':'..-', 'z':'.--.', '{':'-.', '}':'.'}
flag = []
for t in text:
	for i,j in d.items():
		if t == j:
			flag.append(i)
print ''.join(flag)
```
## Flag
> tjctf{jchiefcoil}
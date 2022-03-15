mem = [0] * 128

base32 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678")
ops = ["+", "-", "="]

a = 0
r = True
d = 0
pointer = 0

inst = "="

exit = False

code = list("vABCDEFGB*!")

for i in range(0, len(code)):
	mem[i] = code[i]

# first 64 is code
# last 64 is mem

def execute():
	global inst
	global a
	global mem
	global r
	global exit
	global pointer

	p = mem[pointer]
	if p in base32:
		if inst == "=":
			a = base32.index(p)
		elif inst == "+":
			a += base32.index(p)
		else:
			a -= base32.index(p)
	elif p in ops:
		inst = str(p)
	elif p == "^":
		r = False
	elif p == "v":
		r = True
	elif p == "*":
		if r:
			a = base32.index(pointer)
		else:
			pointer = a
	elif p == "!":
		exit = True
	print(pointer)



while exit == False:
	execute()
	pointer += 1

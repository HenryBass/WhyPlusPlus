mem = [0] * 128

base32 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678")
ops = ["+", "-", "="]

regs = [0, 0, 0]
inst = "="
reg = 0

code = list("QAB1HTRHE")

for i in range(0, len(code)):
	mem[i] = code[i]

# first 64 is code
# last 64 is mem

def execute(pointer):
	p = mem[pointer]
	print(p)
	if p in base32:
		if inst == "=":
			regs[reg] = base32.index(p)
		elif inst == "+":
			regs[reg] += base32.index(p)
		else:
			regs[reg] -= base32.index(p)
	#elif p in ops:
	#	inst = p
	print(regs)



for i in range(0, len(code)):
	execute(i)

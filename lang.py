base32 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678")
ops = ["+", "-", "="]

a = 0
r = True

pointer = 0

inst = "="

exit = False

#code = list("^=B v$+B^ & =A +87 % =B $ v$^ +B & -B +87 % !")

mem = list("^A&B&C&D!")

mem += [0] * len(mem)

data = int(len(mem)/2)

# first 64 is code
# last 64 is mem

def execute():
 global inst
 global a
 global mem
 global r
 global exit
 global pointer
 global data

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
  if r:
    r = False
  else:
    r = True
 elif p == "*":
  if r:
   a = pointer
  else:
   pointer = a
 elif p == "%":
  if r:
   a = ord(input()[0])
  else:
   print(chr(a))
 elif p == "&":
  if r:
   a = int(input())
  else:
   print(a)
 elif p == "@":
  if r:
   a = data
  else:
   data = a
 elif p == "?":
  if a != 0:
   pointer += 1
 elif p == "$":
  if r:
   a = mem[data]
  else:
   mem[data] = a
 elif p == "#":
  mem += [0]
 elif p == "!":
  exit = True

while exit == False:
 try:
  execute()
 except:
   print("you messed up")
 pointer += 1

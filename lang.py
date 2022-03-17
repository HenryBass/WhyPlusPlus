mem = [0] * 128

base32 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678")
ops = ["+", "-", "="]

a = 0
r = True
data = int(len(mem)/2)
pointer = 0

inst = "="

exit = False

code = list("^+87!")

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
  r = False
 elif p == "v":
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
 elif p == "@":
  if r:
   a = data
  else:
   data = a
 elif p == "$":
  if r:
   a = mem[data]
  else:
   mem[data] = a
 elif p == "!":
  exit = True

while exit == False:
 execute()
 pointer += 1

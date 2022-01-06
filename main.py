import math
a=float(input("Ievadi skaitli:"))
def decimal(a):
  s=int(a)
  r=a-s
  return r

def kvadrats(a):
  x=math.pow(a,2)
  return x

def sakne(a):
  if a>=0:
    z=math.sqrt(a)
  else:
    z="nav"
  return z

def pozitivs(a):
  if a>0:
    x="+"
  elif a==0:
    x=0
  else:
    x="-"
  return x


print(decimal(a))
print(kvadrats(a))
print(sakne(a))
print(pozitivs(a))
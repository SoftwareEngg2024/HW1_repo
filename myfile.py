import sys

def add(a, b):
    return a+b

def sub(c, d):
    return c - d

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
print(add(a,b)+" "+sub(c,d))
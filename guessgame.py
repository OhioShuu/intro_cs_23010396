#! /usr/bin/python
def fact(x):
 if x == 0:
  return 1
return x * fact(x - 1)
print (‘N fact(N)’)
print(“---------”)
for n in range(10):
 print(n, fact(n))


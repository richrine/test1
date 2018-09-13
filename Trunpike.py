import math
dlist = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10]
dlist.sort()
m = len(dlist)
a = 0.5
b = 0.5
c = 0-m
d = (b**2) - 4*a*c
sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b-math.sqrt(d))/(2*a)
sol = int(abs(sol1))
l = [None] * sol
m -= 1
sol -= 1

l[0] = 0

l[sol] = dlist[m]
dlist.remove(l[sol])

print(dlist)
print(l)

def permutation(l, dlist):
    for 
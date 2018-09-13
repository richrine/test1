#(x, y) = (1, 1)

#while x < 1000:
#    print(y)
#    x, y = (y, x + y)


#(x, y) = (1, 1)

#while y < 1000:
#    print(y)
 #   z = x
  #  x = y
   # y = x + z




def fibb(n):
    if n <= 0:
        print("You're an idiot!")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 10:
        raise ValueError('Size too big, back off!')
    else:
        return fibb(n-1) + fibb(n-2)

b = "H"

i = 0
sum = 0
sum1 = 0
while i < len(b):
    num = ord(b[i])
    sum += num
    i += 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 10):
    sum1 += fibb(a[i])

print (sum1)
#print(fibb(7))
#parents, babies = (1, 1)
#while babies < 1000:
#    print ('This generation has {0} babies'.format(babies))
#    parents, babies = (babies, parents + babies)

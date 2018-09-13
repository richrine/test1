#1
#for i in range(2000, 3200):
#    if i % 7 == 0:
#        if i % 5 != 0:
#            print(i, end = ',')


#2
#num = int(input("Please enter a number: "))
#i = num
#sum = 1
#while i > 0:
#    sum = sum * i
#    i -= 1
#
#print(sum)

#3
#num = int(input("Please enter a number: "))
#dict = {}
#i = 1
#for i in range(1, num+1):
#    dict[i] = i*i
#    i += 1
#print(dict)

#4
#strnum = input("Please enter a series of numbers: ")
#listnum = strnum.split(",")
#print(listnum)
#tlistnum = tuple(listnum)
#print(tlistnum)

#5
#class FirstClass:
#    def __init__(self):
#        self.stri = " "
#        self.ustri = " "
#    def getString(self):
#        self.stri = str(input("Please enter a string: "))
#    def printString(self):
#        self.ustri = str.upper(self.stri)
#        print(self.ustri)


#a = FirstClass()

#a.getString()
#a.printString()

## Testing
#from unittest import TestCase
#from tester import FirstClass


#class TestFirstClass(TestCase):
#    def test_InstanceOf(self):
#        b = FirstClass()
#        self.assertIsInstance(b, FirstClass)

#    def test_getString(self):
#       print("Test case with Hello")
#        b = FirstClass()
#        b.getString()
#        str1 = "Hello"
#        self.assertEqual(b.stri, str1)

#    def test_printString(self):
#        b = FirstClass()
#        b.getString()
#        b.printString()
#        self.assertTrue(b.ustri.isupper())

#6
#import math
#c = 50
#h = 30

#strnum = input("Please input a series of numbers: ")
#listnum = strnum.split(',')
#newlist = list()
#i = 0
#while len(listnum) > 0:
#    x = float(listnum.pop(0))
#    d = int(x)
#    y = math.sqrt((2*d*c)/h)
#    newlist.append(int(y))
#print(newlist)

#7
#strnum = input("Please input two numbers separated by a comma: ")
#listnum = strnum.split(',')

#x = int(listnum.pop(0))
#y = int(listnum.pop(0))

#listoflists = list()
#i = 0

#for i in range(x):
#    j = 0
#    flist = list()
#    for j in range(y):
#        flist.append(i*j)
#    listoflists.append(flist)

#print(listoflists)

#8
#str1 = input("Please input any number of words separated by a comma: ")
#liststr = str1.split(',')

#sortlist = sorted(liststr)

#print(sortlist)

#9
#lines = list()

#while True:
#    line = input()
#    if line:
#        lines.append(line.upper())
#    else:
#        break
#text = '\n'.join(lines)
#print(text)

#10
#a = input("Please enter a line with repeats of the same word: ")
#words = a.split(" ")
#b = (" ".join(sorted(set(words), key=words.index)))
#list1 = b.split()
#list1 = sorted(list1)
#print(list1)

#11
#a = input("Please enter comma separated binary numbers: ")
#b = a.split(",")
#c = list()
#i = 0
#while i in range(len(b)):
#    x = b.pop(0)
#    y = int(x, 2)
#    if y % 5 == 0:
#        c.append(y)

#print(c)

#12
#finlist = list()
#for i in range(1000, 3001):
#    s = str(i)
#    a = [int(x) for x in s]
#    val = True
#    for i in range(0,4):
#        if a[i] % 2 != 0:
#            val = False

#    if val:
#        finlist.append(s)

#print(finlist)

#13
#a = input("Please enter a string for analysis: ")
#b = list(a)
#letters = 0
#digits = 0
#for j in range(len(b)):
#    c = b[j]
#    if c.isalpha():
#        letters += 1
#    elif c.isdigit():
#        digits += 1

#print("LETTERS", letters, "\n", "DIGITS", digits)

#14
#a = input("Please enter a string for analysis: ")
#b = list(a)
#ucase = 0
#lcase = 0
#for j in range(len(b)):
#    c = b[j]
#    if c.isupper():
#        ucase += 1
#    elif c.islower():
#        lcase += 1

#print("UPPER CASE", ucase, "\n", "LOWER CASE", lcase)

#15
#num = input("Please enter a single digit: ")
#numlist = [num, num+num, num+num+num, num+num+num+num]
#print(numlist)
#l = 0
#for i in range(len(numlist)):
#    l += int(numlist[i])

#print(l)

#16
#strnum = input("Please input numbers separated by a comma: ")
#listnum = strnum.split(',')
#a = [int(x) for x in listnum]
#finlist = list()
#for i in range(len(a)):
#    if a[i] % 2 != 0:
#        finlist.append(a[i])

#print(finlist)

#17
#def var_args(f_arg, *argv):
#    sum = 0
#    if f_arg == 'D':
#        sum += int(argv[0])
#    elif f_arg == 'W':
#        sum -= int(argv[0])
#    for i in range(len(argv)):
#        if argv[i] == 'D':
#            sum += int(argv[i+1])
#            i += 1
#        if argv[i] == 'W':
#            sum -= int(argv[i+1])
#            i += 1

#    print(sum)
#strnum = input("Please enter the bank commands to be used: ")
#listnum = strnum.split(" ")
#fval = listnum.pop(0)
#var_args(fval, *listnum)

#18
#strlist = input("Please enter a list of passwords separated by a comma: ")
#passlist = strlist.split(",")
#finlist = list()
#for i in range(len(passlist)):
#    a = passlist[i]
#    b = list(a)
#    check1 = False
#    check2 = False
#    check3 = False
#    check4 = False
#    check5 = False
#    for j in range(len(b)):
#        if str(b[j]).isupper():
#            check1 = True
#        elif str(b[j]).islower():
#            check2 = True
#        elif str(b[j]).isdigit():
#            check3 = True
#        elif str(b[j]) in ('$','#','@'):
#            check4 = True
#        if len(b) >= 6 and len(b) <= 12:
#            check5 = True
#    if check1 and check2 and check3 and check4 and check5:
#        finlist.append(a)

#print(finlist)

#19
#from operator import itemgetter
#str1 = input("Please enter a list of users: ")
#str2 = str1.split(" ")
#finlist = list()
#for i in range(len(str2)):
#    a = str2[i].split(",")
#    finlist.append(a)

#print(sorted(finlist, key=itemgetter(0, 2)))

#20
#class hello():
#    def get_range(self):
#        for num in range(0, self.n):
#            if num % 7 == 0:
#                yield num

#    def __init__(self, n):
#        super(hello, self).__init__()
#        self.n = n

#a = hello(120).get_range()

#print(next(a))
#print(next(a))
#for num in a:
#    print(num)

#21
#import math
#def move_args(farg, *args):
#    x = 0
#    y = 0
#    if farg == 'UP':
#        y += int(args[0])
#    elif farg == 'DOWN':
#        y -= int(args[0])
#    elif farg == 'LEFT':
#        x -= int(args[0])
#    elif farg == 'RIGHT':
#        x += int(args[0])
#    for i in range(len(args)):
#        if args[i] == 'UP':
#            y += int(args[i+1])
#            i += 1
#        if args[i] == 'DOWN':
#            y -= int(args[i+1])
#            i += 1
#        if args[i] == 'LEFT':
#            x -= int(args[i+1])
#            i += 1
#        if args[i] == 'RIGHT':
#            x += int(args[i+1])
#            i += 1
#    d = math.sqrt((x*x) + (y*y))
#    print(int(d))

#strnum = input("Please enter the robot commands to be used: ")
#listnum = strnum.split(" ")
#fval = listnum.pop(0)
#move_args(fval, *listnum)

#22
#def word_count(str):
#    count = {}
#    word = str.split(" ")
#    word1 = sorted(word)

#    for i in word1:
#        if i in count:
#            count[i] += 1
#        else:
#            count[i] = 1

#    print(count)


#istr = input("Please input the string to have word counted: ")
#word_count(istr)

#23
#def calc_val(num):
#    num**=2
#    return num

#n = int(input("Enter a number to be squared: "))
#print(calc_val(n))

#24
#print(abs.__doc__)
#print(int.__doc__)
#print(input.__doc__)
#class nunya():
#    def __doc__(self):
#        print("This does nothing...")

#n = nunya()
#print(n.__doc__())

#25
#class Yo(object):
#    def __init__(self, name):
#        self.name = name

#class Yi():
#    def __init__(self):
#        self.name = name

#a = Yo("Jean")
#b = Yo(Yi)
#b.name = "John"
#print(a.name)
#print(b.name)

#26
#def sum_nums(m, n):
#    sum = m+n
#    return sum

#print(sum_nums(5, 6))

#27
#def int_to_string(n):
#    try:
#        val = int(n)
#        print(str(n))
#    except ValueError:
#        print("That is not an int!")


#int_to_string(17)
#int_to_string("r")

#29
#def add_two_strings(m, n):
#    a = int(m)
#    b = int(n)

#    c = a+b
#    print(c)

#add_two_strings("42", "5")

#30
#" coding=<unicode>"

#31
#from fractions import Fraction

#a = input("Please enter an integer: ")
#n = int(a)
#sum = float()
#i = 0
#while i <= n:
#    sum += Fraction(i/(i+1))
#    i += 1

#print("%.2f" % sum)

#32-1
#import random
#n = random.random()
#randNum = float(100*n)

#print(randNum)

#32-2
#import timeit
#print(timeit.timeit('1*1', number=100))

#32-3
#istr = input("Please enter the string to be evaluated: ")
#listr = list(istr)
#d = dict()

#for i in listr:
#    if i in d:
#        d[i] += 1
#    else:
#        d[i] = 1

#print(d)

#Advanced Exercises
#1 - Use the p and k with a while loop to just multiply the numbers piece by piece
#import timeit
#import math

#print(timeit.timeit('pow(5, 10)', number=1000))
#print(timeit.timeit('5**10', number=1000))

#2
#n = [-10, -9, -8, -6, -5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#sol = []
#n.sort()
#print(n)

#for i in n:
#    if n[i] < 0 and (n[i]*-1) in n:
#        sol.append(abs(n[i]))

#print(sol)

#3
# def ways(m):
#     n = [0]*(m)
#     n[0] = 1
#     for i in range(1, m):
#         for j in range(1, min(5, i)+1):
#             n[i] += n[i-j]
#     return n[m-1]
#
# print(ways(700))

#4
a = [[0,1,1,1,0,0],
     [0,1,1,1,0,0],
     [0,1,1,1,0,0],
     [1,0,0,0,1,1],
     [0,1,1,0,0,1],
     [1,1,1,0,0,0]]
for s in a:
    print(s)
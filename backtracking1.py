def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))
print(permute(3, ["a","b","c"]))

def permutation(m):
    m /= 2
    if m < 1:
        return m
    else:
        return permutation(m)

print(permutation(42))

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

print(fib(32))
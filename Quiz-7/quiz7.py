import sys

x = [2,3,5,7,11,13,17,19,23,29,31,37]

lst = []
for i in sys.argv[1]:
    lst.append(i)

def recursion(a):
    prime = []
    count = 0
    if a % 2 == 0:
        prime.append(2)
        a == a//2
        return recursion(a)
    return prime
for i in range(len(lst)):
    print(recursion(lst[i]))


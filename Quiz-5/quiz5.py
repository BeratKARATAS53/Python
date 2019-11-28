import sys

file = open(sys.argv[1],"r")
outfile = open(sys.argv[2],"w")

list = []
list2 = []

a = 0
for line in file.readlines():
    line = line.rstrip("\n")
    item = line.split(":")
    if item[a] == "line 1":
        list.extend(item[a:len(line)])
    elif item[a] == "line 2":
        list2.extend(item[a:len(line)])

print(list)
print(list2)


def sum(number):
    total = 0
    if int(number) == True:
        total += number
    else:
        pass
    return total

i = 0
for i in range(len(list)):
    print(sum(list))
    i += 1
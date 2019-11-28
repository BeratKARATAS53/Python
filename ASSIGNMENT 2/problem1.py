import sys
Integers = sys.argv[1]

file = open("Integers.txt", "r")

list = []

for line in file.readlines():
    items = line.split(";")
    for n in items:
        AverageFirstThreeDigit = (int(n[0]) + int(n[1]) + int(n[2])) / 3
        list.append(AverageFirstThreeDigit)

        for i in range(len(list)):
            temp = list[i]
            list[i] = list[len(list) - 1]
            list[len(list) - 1] = temp

print(list)
file.close()

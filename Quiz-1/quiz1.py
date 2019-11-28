import math

toplam = 0
output = open("outputOpen.txt", "w")
for i in range(10):
    number = int(input("Enter Number :"))
    if (number) % 2 == 1:
        toplam = toplam + number

print (toplam)
print (toplam,file=output)
output.close()

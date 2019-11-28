import sys

infile1 = open(sys.argv[1],"r")
infile2 = open(sys.argv[2],"r")
output = open(sys.argv[3],"w")

final = {}

print("Quiz 4-C: Exceptions")
output.write("Quiz 4-C: Exceptions"+"\n")

for line in infile1.readlines():
    line = line.rstrip("\n")
    item = line.split(":")
    i = item[0]
    k = int(item[1]) * int(item[2])
    final[i] = [k]

for fruit in infile2.readlines():
    fruits = fruit.rstrip("\n")
    try:
        print("Fruit",fruits,"- price",final[fruits])
        output.write("Fruit"+str(fruit)+"- price"+str(final[fruit])+"\n")
    except:
        print("This fruit does not exist in file.",fruits)
        output.write("This fruit does not exist in file."+str(fruits)+"\n")

infile1.close()
infile2.close()
output.close()
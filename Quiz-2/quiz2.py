infile = open("input.txt", "r")

outfile = open("output.txt", "w")

def even_average(input_list):
    total = 0
    count = 0
    for item in input_list:
        if int(item) % 2 == 0:
            total += int(item)
            count += 1
    return total / count

for line in infile.readlines():
    input_item = line.split(";")

    print("The average in line even numbers : ", even_average(input_item[0:]))
    outfile.write("The average in line even numbers : " +str(even_average(input_item[0:]))+ "\n")

infile.close()
outfile.close()
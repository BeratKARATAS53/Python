import sys

wordbook = open(sys.argv[1], "r")
binarian = open(sys.argv[2], "r")
english = open(sys.argv[3], "r")
binarian_message = open("binarian_message.txt", "w+")
message = open("message.txt","w+")
outfile = open("compututions.txt", "w+")

total_list = []
for items in wordbook.readlines():
    items = items.rstrip("\n")
    key = items.split()
    total_list.extend(key)

binarian_dict = []
english_dict = []

def read_dictionary1(file):
    n = 0
    for n in range(len(file) // 3):
        binarian_dict.append(file[int(3*n)])
        binarian_dict.append(file[int(3*n)+1])
    n += 1
    return binarian_dict

print(read_dictionary1(total_list))

def read_dictionary2(file):
    n = 0
    for n in range(len(file) // 3):
        english_dict.append(file[int(3*n)+1])
        english_dict.append(file[int(3*n)])
    n += 1
    return english_dict

print(read_dictionary2(total_list))

def binary_to_decimal(number):
    total = 0
    for n in range(len(str(number))):
        if int(str(number)[::-1][n]) == 1:
            i = pow(2,n)
            total += i
        else:
            continue
        n += 1
    return total

def decimal_to_binary(number):
    return bin(number)

def ly_to_km(number):
    light_year = 9460700000000
    ltk = str(light_year*number)
    return ltk

bin_list = []
outfile.write("Data about Binarian planet :"+"\n")
z = 0
for binarian2 in binarian.readlines():
    binarian2 = binarian2.rstrip("\n")
    item = binarian2.split()
    if item[z][0] == "+":
        q = 0
        for q in range(5):
            if item[z+q] == "Hata":
                btb1 = binary_to_decimal(int(item[z+q+1]))
                outfile.write("Planet temperature : "+str(btb1)+".0 degrees Celcius"+"\n")
                break
            elif item[z+q] == "bav'Do":
                btb2 = binary_to_decimal(int(item[z+q+1]))
                outfile.write("Orbital speed : "+str(btb2)+".0 km/h"+"\n")
                break
            elif item[z+q] == "chuqD":
                btb3 = ly_to_km(binary_to_decimal(int(item[z+q+1])))
                outfile.write("Distance from The Earth : "+str(btb3[0])+","+str(btb3[1:7])+"e+"+str(len(btb3)-1)+"km"+"\n")
                break
    elif item[z][0] == "#":
        pass
    else:
        bin_list.extend(item)

eng_list = []
p = 0
for binary in english.readlines():
    binary = binary.rstrip("\n")
    binary = binary.lower()
    item = binary.split()
    eng_list.extend(item)

def binarian_to_english(text):
    a = 0
    b = 0
    c = 8
    for a in range(len(text)):
        for b in range(len(binarian_dict)//2):
            i = text[a]
            if text[a] == binarian_dict[int(2*b)]:
                binarian_message.write(str(binarian_dict[int(2*b)+1])+" ")
                break
            if text[a] != binarian_dict[int(2*b)]:
                b += 1
            if b == len(binarian_dict)//2:
                binarian_message.write(str(text[a])+" ")
            b += 1
            if a == c:
                binarian_message.write("\n")
                c += 8
            else:
                continue
        a += 1
    return

def english_to_binarian(text):
    d = 0
    e = 0
    f = 11
    for d in range(len(text)):
        for e in range(len(english_dict) // 2):
            if text[d] == "Binarians,":
                message.write(str("tlhInganA")+" ")
                break
            if text[d] == "hd":
                message.write(str("HD")+" ")
                break
            if text[d] == english_dict[int(2*e)]:
                message.write(str(english_dict[int(2*e)+1]))
            if text[d] != english_dict[int(2*e)]:
                e += 1
                if text[d][-1] == "," or text[d][-1] == "." or text[d][-1] == "!" or text[d][-1] == "?":
                    if text[d][:-1] == english_dict[int(2*e)]:
                        message.write(str(english_dict[int(2*e)+1])+" ")
                        break
                    if text[d][:-1] == "xenu":
                        message.write(str("Xenu")+" ")
                        break
                    if text[d][:-1] != english_dict[int(2*e)]:
                        e += 1
                    if e == len(english_dict)//2:
                        if text[d][:-1] in message.readlines():
                            break
                if e == len(english_dict)//2:
                    if text[d][-1] == "," or text[d][-1] == ".":
                        message.write(str(text[d][:-1])+" ")
                        break
                    else:
                        message.write(str(text[d])+" ")
                        break
            if text[d] == "I":
                message.write(str(text[d])+" ")
                break
            if text[d] == english_dict[int(2*e)]:
                message.write(str(english_dict[int(2*e)+1])+" ")
                break
            if text[d][0] == "0" or text[d][0] == "1" or text[d][0] == "2" or text[d][0] == "3" or text[d][0] == "4" or text[d][0] == "5" or text[d][0] == "6" or text[d][0] == "7" or text[d][0] == "8" or text[d][0] == "9":
                v = int(text[d])
                dtb = decimal_to_binary(v)
                message.write(str(dtb[2:])+" ")
                break
            if d == f:
                message.write("\n")
                f += 11
        d += 1
    return

print(binarian_to_english(bin_list))
print(english_to_binarian(eng_list))

print("""
-------------------------------------------------------------
-------------------------------------------------------------
""")

print("""
#------------------------------------------------------------#
# Student Name: Doğukan Berat KARATAŞ
# Student ID: 21527142
# BBM103 Introduction to Programming Laboratory I, Fall 2016
# Assignment 3: Mission: Save the Earth
#------------------------------------------------------------#
""")

wordbook.close()
binarian.close()
binarian_message.close()
message.close()
english.close()
outfile.close()

binarian_message2 = open("binarian_message.txt", "r")
message2 = open("message.txt","r")
outfile2 = open("compututions.txt", "r")

print(binarian_message2.read())
print(outfile2.read())
print(message2.read(),"\n")

binarian_message2.close()
message2.close()
outfile2.close()

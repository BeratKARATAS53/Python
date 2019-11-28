from numpy.random import random_integers as r_i
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

file1 = open("reading.txt","w") ### ALL OF NOMINEES'S VOTES
reading1 = open("retrievedData.txt","w") ### DESIRED FILE in PDF
infile = open("nominees.txt","w") ### NOMINEES

cities = []
nomins = []

### STEP 1: _START_
def retrieveData(x,y):
    global cities,nomins
    nominees = [] # ALL OF NOMINEES'S VOTES
    with open(x,"r") as e_usa:
        reading = csv.reader(e_usa,delimiter=",")
        header = next(reading)
        head=[z.lower() for z in header]
        if head[2] == "electoral" and head[len(header)-1] == "others":
            nomins.extend(header[3:len(header)-1])
        elif head[2] == "electoral" and head[len(header)-1] != "others":
            nomins.extend(header[3:])
        elif head[2] != "electoral" and head[len(header)-1] == "others":
            nomins.extend(header[2:len(header)-1])
        else:
            nomins.extend(header[2:])
        for row in reading:
            cities.append(row[0])
            if head[2] == "electoral" and head[len(header)-1] == "others":
                nominees.extend(row[3:len(header)-1])
            elif head[2] == "electoral" and head[len(header)-1] != "others":
                nominees.extend(row[3:])
            elif head[2] != "electoral" and head[len(header)-1] == "others":
                nominees.extend(row[2:len(header)-1])
            else:
                nominees.extend(row[2:])
    for j in range(len(nominees)):
        if j == len(nominees)-1:
            file1.write(str(nominees[j]))
        else:
            file1.write(str(nominees[j])+",")

    for k in range(len(nomins)):
        if k == len(nomins)-1:
            infile.write(str(nomins[k]))
        else:
            infile.write(str(nomins[k])+",")

    infile.close()
    file1.close()
    file2 = open("reading.txt","r")
    infile2 = open("nominees.txt","r")

    items = []
    for line in file2:
        item = line.split(",")
        items.extend(item)

    item1 = []
    item2 = []
    ### FOR COMPARE WITH SYS.ARGV[2]
    for line in infile2:
        item2.extend(line.split(","))
        item1.append(line)
    if (y == item1[0] or y == item1) or (y == item2):
        nom = []
        a = len(items)//51
        for i in range(0,a):
            for j in range(len(items)//a):
                nom.append(items[a*j+i])
                if i== a-1 and j == len(items)//a-1:
                    reading1.write(str(items[a*j+i]))
                else:
                    reading1.write(str(items[a*j+i])+",")
    else:
        pass

    reading1.close()
    file2.close()

    file3 = open("retrievedData.txt","r") # DESIRED DOCUMENT

    list = []

    for line in file3:
        number = line.split(",")
        list.extend(number)

    return list

print(retrieveData("ElectionIran2009.csv",["Mousavi","Rezzai","Karrubi"]))
### STEP 1: _FINISH_
file3 = open("retrievedData.txt","r") # DESIRED DOCUMENT

list = []
numbers = []
for line in file3:
        number = line.split(",")
        numbers.extend(number)
        list.extend(number)
### STEP 2: _START_
n1 = [int(x) for x in numbers[:len(cities)]]  # 1. Nominee's votes
n2 = [int(x) for x in numbers[len(cities):len(cities)*2]]  # 2. Nominee's votes
n3 = [int(x) for x in numbers[len(cities)*2:len(cities)*3]]  # 3. Nominee's votes
n4 = [int(x) for x in numbers[len(cities)*3:len(cities)*4]]  # 4. Nominee's votes

z = [x for x in range(len(cities))]

x_pos = np.arange(len(z))
width = 0.35

colors = ["b","r","sage","teal","navy","darkgreen","greenyellow"]

def DispBarPlot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    nominee1 = ax.bar(x_pos-width, n1, width, color=colors[0]) # FIRST NOMINEE
    nominee2 = ax.bar(x_pos, n2, width, color=colors[1]) # SECOND NOMINEE

    ax.set_ylabel("VOTE COUNTS")
    plt.xlabel("STATES")
    plt.xlim(-0.5,len(cities)+0.5)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(cities, rotation=90)
    ax.legend((nominee1[0], nominee2[0]), (nomins[0], nomins[1]))
    plt.tight_layout()
    plt.savefig("ComparativeVotes.pdf")
    plt.close()
    pass

print(DispBarPlot())
### STEP 2: _FINISH_
### STEP 3: _START_
total = sum(n1) + sum(n2) + sum(n3) + sum(n4)
percent_of_vote = ["{:.3f}%".format(float(100*sum(n1)/total)),"{:.3f}%".format(float(100*sum(n2)/total)),
                   "{:.3f}%".format(float(100*sum(n3)/total)),"{:.3f}%".format(float(100*sum(n4)/total))]

p_of_v = [float(x[:5]) for x in percent_of_vote if x != "0.000%"]

width2 = 0.35
a = []
a.extend(percent_of_vote[:len(p_of_v)])

xpos = np.arange(len(a))

def compareVoteonBar():
    barlist = plt.bar(xpos,p_of_v,width=width2*2,align="center",color=colors)
    plt.xticks(xpos,a)
    for c in range(2,len(nomins)+1):
        if len(nomins) == c:
            plt.legend((barlist),(nomins))
    plt.ylabel("Vote Percentages")
    plt.xlabel("Nominees")
    plt.xlim(-0.5,len(a)-0.5)
    plt.savefig("CompVotePercs.pdf")
    plt.close()
    pass

print(compareVoteonBar())
### STEP 3: _FINISH_
### STEP 4: _START_
def obtainHistogram(x):
    zero,one,two,three,four,five,six,seven,eight,nine = 0,0,0,0,0,0,0,0,0,0
    list_length = []
    ob_hist = []
    f = [str(c) for c in x]
    for i in range(len(f)):
        if len(f[i]) <= 2:
            list_length.extend(f[i])
        if len(f[i]) > 2:
            list_length.extend(f[i][len(f[i])-2:len(f[i])])
        if int(f[i]) < 10:
            list_length.append("0")
    for j in range(len(list_length)):
        if list_length[j] == "0":
           zero += 1
        if list_length[j] == "1":
           one += 1
        if list_length[j] == "2":
           two += 1
        if list_length[j] == "3":
           three += 1
        if list_length[j] == "4":
           four += 1
        if list_length[j] == "5":
           five += 1
        if list_length[j] == "6":
           six += 1
        if list_length[j] == "7":
           seven += 1
        if list_length[j] == "8":
           eight += 1
        if list_length[j] == "9":
           nine += 1
    ob_hist.append(float(zero/len(list_length))),ob_hist.append(float(one/len(list_length))),ob_hist.append(float(two/len(list_length)))
    ob_hist.append(float(three/len(list_length))),ob_hist.append(float(four/len(list_length))),ob_hist.append(float(five/len(list_length)))
    ob_hist.append(float(six/len(list_length))),ob_hist.append(float(seven/len(list_length))),ob_hist.append(float(eight/len(list_length)))
    ob_hist.append(float(nine/len(list_length)))
    return ob_hist

print(obtainHistogram(list))
### STEP 4: _FINISH_
means = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
x_pos2 = [x for x in range(10)]
### STEP 5: _START_
def plotHistogram(a):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    digit = ax.plot(x_pos2,obtainHistogram(a),color="r")
    mean = ax.plot(x_pos2,means,"--",linewidth= 1,color="g")

    ax.legend((mean[0],digit[0]),("Mean","Digit Dist."))

    plt.title("Histogram of least sign. digits")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.savefig("Histogram.pdf")
    plt.close()
print(plotHistogram(list))
### STEP 5: _FINISH_
### STEP 6:
def plotHistogramWithSample():
    hist1 = r_i(0,100,10)
    hist2 = r_i(0,100,50)
    hist3 = r_i(0,100,100)
    hist4 = r_i(0,100,1000)
    hist5 = r_i(0,100,10000)

    x_pos = [x for x in range(10)]

    mean = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

    hist = plt.plot(x_pos,obtainHistogram(hist1),linewidth=3,color="b")
    means = plt.plot(x_pos,mean,"--",linewidth=2,color ="g")
    plt.title("Histogram of least sign. digits - Sample:1")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.legend((means[0],hist[0]),("Mean","Digit Dist."),loc="upper left")
    plt.savefig("HistogramofSample1.pdf")
    plt.close()

    hist = plt.plot(x_pos,obtainHistogram(hist2),linewidth=3,color="r")
    means = plt.plot(x_pos,mean,"--",linewidth=2,color ="g")
    plt.title("Histogram of least sign. digits - Sample:2")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.legend((means[0],hist[0]),("Mean","Digit Dist."),loc="upper left")
    plt.savefig("HistogramofSample2.pdf")
    plt.close()

    hist = plt.plot(x_pos,obtainHistogram(hist3),linewidth=3,color="m")
    means = plt.plot(x_pos,mean,"--",linewidth=2,color ="g")
    plt.title("Histogram of least sign. digits - Sample:3")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.legend((means[0],hist[0]),("Mean","Digit Dist."),loc="upper left")
    plt.savefig("HistogramofSample3.pdf")
    plt.close()

    hist = plt.plot(x_pos,obtainHistogram(hist4),linewidth=3,color="orange")
    means = plt.plot(x_pos,mean,"--",linewidth=2,color ="g")
    plt.title("Histogram of least sign. digits - Sample:4")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.legend((means[0],hist[0]),("Mean","Digit Dist."),loc="upper left")
    plt.savefig("HistogramofSample4.pdf")
    plt.close()

    hist = plt.plot(x_pos,obtainHistogram(hist5),linewidth=3,color="c")
    means = plt.plot(x_pos,mean,"--",linewidth=2,color ="g")
    plt.title("Histogram of least sign. digits - Sample:5")
    plt.ylabel("Distribution")
    plt.xlabel("Digits")
    plt.legend((means[0],hist[0]),("Mean","Digit Dist."),loc="upper left")
    plt.savefig("HistogramofSample5.pdf")
    plt.close()
    pass

print(plotHistogramWithSample())
### STEP 6: _FINISH_
### STEP 7: _START_
def calculatingMSE(a,b):
    total = 0
    for i in range(len(a)):
        x = (float(a[i])-float(b[i]))**2
        total += x
    return total
### STEP 7: _FINISH_
### STEP 8: _START_
print("{}".format(calculatingMSE(obtainHistogram(list),means)))
### STEP 8: _FINISH_
### STEP 9: _START_

high_low = []
def compareMSEs(x):
    high = 0
    low = 0
    random_list = []
    for i in range(10000):
        random1 = r_i(0,100,len(numbers))
        random_list.append(calculatingMSE(obtainHistogram(random1),means))
        i += 1
    for i in range(len(random_list)):
        if x >= float(random_list[i]):
            high += 1
        else:
            low += 1
    high_low.append(high),high_low.append(low)

print(compareMSEs(calculatingMSE(obtainHistogram(list),means)))
### STEP 9: _FINISH_
### STEP 10: _START
answer = open("myAnswer.txt","w")

answer.write(str("MSE value of 2012 USA election is {}".format(calculatingMSE(obtainHistogram(list),means)))+"\n"+
             str("The number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(high_low[1]))+"\n"+
             str("The number of MSE of random samples which are smaller than USA election MSE is  {}".format(high_low[0]))+"\n"+
             str("2012 USA election rejection level p is {}".format((high_low[0])/10000))+"\n")
if high_low[1] < 500:
    answer.write(str("Finding: We reject the null hypothesis at the p = {} level".format((high_low[0])/10000))+"\n")
else:
    answer.write(str("Finding: There is no statistical evidence to reject null hypothesis."))

answer.close()

answer1 = open("myAnswer.txt","r")
print("\n")
for form in answer1:
    print(form.rstrip("\n"))
### STEP 10: _FINISH_
### _END_ ###

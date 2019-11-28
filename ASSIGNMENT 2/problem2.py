import sys
HouseData = sys.argv[1]

file = open("HouseData.txt", "r")

print(" The total Cost of each house : ","\n")

BulletList = []

for line in file.readlines():
    line = line.rstrip("\n")
    items = line.split()
    BulletList.append(items)

def calculateTotalCost(list):
    resultList = []

    for j in range(len(BulletList)):
        HC = int(list[j][0])  # HC = HOUSE COST
        FC = int(list[j][1])  # FC = FUEL COST
        T = float(list[j][2]) # T = TAXES
        TC = float(HC + FC*10 + HC*T*10) # TC = TOTAL COST

        j += 1
        resultList.append(TC)
    return resultList

def displayCost(list):
    displayList = calculateTotalCost(list)
    return displayList

def selectBestBuy(list):
    BestBuyList = calculateTotalCost(list)
    return BestBuyList

for i in range(len(BulletList)):
    print("",i+1,". house's total cost: ",displayCost(BulletList)[i])
    i += 1

x = selectBestBuy(BulletList)

print("\n","You should select ",(x.index(min(x)) + 1),". house whose total cost is : ",min(x))

file.close()

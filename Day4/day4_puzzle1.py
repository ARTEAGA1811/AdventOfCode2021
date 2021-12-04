

def filterInformation(arr:list):
    bingoList = []
    aux = []
    for i in range(len(arr)):
        if arr[i] =="":
            bingoList.append(aux)
            aux = []
        else:
            sepp = arr[i].split(" ")
            #print("estoy en el " + str(i))
            aux2 = []
            for k in range(len(sepp)):
                if sepp[k] != "":
                    aux2.append(int(sepp[k]))
            aux.append(aux2)
    bingoList.append(aux)
    return bingoList

def checkBing(bingoList:list, eliminated:set):
    #check rows
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(len(bingoList[i])):
            if bingoList[i][j].count(-1) == 5:
                return i
    #check columns
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(5):
            if bingoList[i][0][j] == -1 and bingoList[i][1][j] == -1 and bingoList[i][2][j] == -1 and bingoList[i][3][j] == -1 and bingoList[i][4][j] == -1:
                return i
    return -1

def changeBingo(bingoList:list, num:int, eliminated:set):
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(len(bingoList[i])):
            for k in range(len(bingoList[i][j])):
                if bingoList[i][j][k] == num:
                    bingoList[i][j][k] = -1

def sumOthers(myWinner:list):
    sum = 0
    for i in range(len(myWinner)):
        for j in range(len(myWinner[i])):
            if myWinner[i][j] != -1:
                sum += myWinner[i][j]
    return sum  

def myPuzzleDay4():
    nums = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]
    #nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    bingoList = filterInformation(getList())
    totalInd = {int(x) for x in range(len(bingoList))}
    eliminated = set()


    for i in range(len(nums)):
        if len(eliminated) < len(totalInd)-1:
            changeBingo(bingoList, nums[i], eliminated)
            ax = checkBing(bingoList, eliminated)
            while ax != -1:
                eliminated.add(ax)
                changeBingo(bingoList, nums[i], eliminated)
                ax = checkBing(bingoList, eliminated)


        else:
            changeBingo(bingoList, nums[i], eliminated)
            fin = totalInd - eliminated
            suma = sumOthers(bingoList[list(fin)[0]])
            return suma * nums[i]

    print(eliminated)
    print(totalInd - eliminated)
    print(len(bingoList))
    print(len(nums))
    #print(totalIn)
    
        


def getList():
    with open("Day4\day4_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]
    # with open("Day4\\test.txt") as f:
    #     return [str(line.strip()) for line in f]
    


#Print the result
print(myPuzzleDay4())

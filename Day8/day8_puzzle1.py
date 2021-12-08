def myPuzzle(displayList:list):
    cont = 0
    for i in range(len(displayList)):
        output = displayList[i].split(" | ")
        output = output[1].split(" ")
        for j in range(len(output)):
            if len(output[j]) == 2 or len(output[j]) == 3 or len(output[j]) == 4 or len(output[j]) == 7:
                cont += 1
    return cont
def getList():
    with open("Day8\day8_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]


#Print solution
print(myPuzzle(getList()))
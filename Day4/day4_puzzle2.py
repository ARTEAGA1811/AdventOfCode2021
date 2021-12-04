def myPuzzleDay4():
    pass

def getList():
    with open("Day4\day4_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]



#Print the result
print(myPuzzleDay4(getList()))

#print(myPuzzleDay3(aux))
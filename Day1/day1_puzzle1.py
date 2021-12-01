def myPuzzle(scanning:list):
    cont = 0
    for i in range(1,len(scanning)):
        if scanning[i] > scanning[i-1]:
            cont+=1
    return cont
    

def getList():
    with open("Day1\day1_puzzle1_list.txt") as f:
        return [int(line.strip()) for line in f]

#Test case
aux = [199,200,208,210,200,207,240,269,260,263]
print(myPuzzle(aux))

#Print solution
print(myPuzzle(getList()))
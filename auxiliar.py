import numpy as np

def mypuzzle(arr:list):
    logIndex = []
    maxI = 0
    maxJ = 0
    for i in range(len(arr)):
        aux = arr[i].split(',')
        logIndex.append((int(aux[0]), int(aux[1])))
        maxI = max(maxI, logIndex[i][0])
        maxJ = max(maxJ, logIndex[i][1])
    
    mymatrix = np.zeros((maxJ+1, maxI+1))
    

    for i in range(len(logIndex)):
        mymatrix[logIndex[i][1]][logIndex[i][0]] = 1
    
    instructions = ["x=655", "y=447", "x=327", "y=223", "x=163", "y=111",  "x=81", "y=55", "x=40", "y=27", "y=13", "y=6"]
    #instructions = ["y=7","x=5"]
    for bucle in range(len(instructions)):

        partArr = []
        if instructions[bucle][0] == 'x':
            divX = int(instructions[bucle][2:])
            
            partArr = mymatrix[:, divX+1:2*divX+1]
            mymatrix = mymatrix[:, 0:divX]
            #add columns with zeros if necessary
            for k in range(len(mymatrix[0])-len(partArr[0])):
                partArr = np.append(partArr, np.zeros((len(partArr), 1)), axis=1)

            partArr = partArr[:, ::-1]

            
            mymatrix = mymatrix+partArr

        else:
            divY = int(instructions[bucle][2:])
            partArr = mymatrix[divY+1:2*divY+1, :]
            mymatrix = mymatrix[0:divY, :]
            #add rows with zeros if necessary
            for k in range(len(mymatrix)-len(partArr)):
                partArr = np.append(partArr, np.zeros((1, len(partArr[0]))), axis=0)
            
            partArr = partArr[::-1, :]
            
            mymatrix = mymatrix+partArr
        

    aux = []
    for i in range(len(mymatrix)):
        temp = []
        for j in range(len(mymatrix[i])):
            if mymatrix[i][j] != 0:
                mymatrix[i][j] = 1

            temp.append(int(mymatrix[i][j]))
        aux.append(temp)
    
    for i in range(len(aux)):
        print(aux[i])
    
def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day13\day13_puzzle1_list.txt"
#fileName = "Day13\\test.txt"

print(mypuzzle(getList(fileName)))

def mypuzzle(arr:list):
    newArr = []
    maxI = 0
    maxJ = 0
    for i in range(len(arr)):
        aux = arr[i].split(',')
        newArr.append((int(aux[0]), int(aux[1])))
        maxI = max(maxI, newArr[i][0])
        maxJ = max(maxJ, newArr[i][1])
    
    mymatrix = []
    for i in range(maxJ+1):
        mymatrix.append([0]*(maxI+1))
    
    for i in range(len(newArr)):
        mymatrix[newArr[i][1]][newArr[i][0]] = 1
    
    instructions = ["x=655", "y=447", "x=327", "y=223", "x=163", "y=111",  "x=81", "y=55", "x=40", "y=27", "y=13", "y=6"]
    #instructions = ["y=7","x=5"]
    for bucle in range(1):
        if instructions[bucle][0] == 'x':
            contX = 0
            contY = int(instructions[bucle][2:])-1
            for i in range(len(mymatrix)):
                contY = int(instructions[bucle][2:])-1
                for j in range(int(instructions[bucle][2:])+1,len(mymatrix[i])):
                    if contY >= 0:
                        if mymatrix[i][j] == 1:
                            mymatrix[contX][contY] = 1

                    contY -= 1
                contX += 1

        else:
            contX =  int(instructions[bucle][2:])-1
            contY = 0
            for i in range(int(instructions[bucle][2:])+1,len(mymatrix)):
                contY = 0
                for j in range(len(mymatrix[i])):
                    if mymatrix[i][j] == 1:
                        mymatrix[contX][contY] = 1

                    contY += 1
                contX -= 1
        
        #xd
        auxArr = []
        if instructions[bucle][0] == 'x':
            for i in range(len(mymatrix)):
                auxArr.append(mymatrix[i][:int(instructions[bucle][2:])])
        else:
            for i in range(0, int(instructions[bucle][2:])):
                auxArr.append(mymatrix[i])

        mymatrix = auxArr

    total = 0
    for i in range(len(mymatrix)):
        total += mymatrix[i].count(1)
    

    return total
    


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day13\day13_puzzle1_list.txt"
#fileName = "Day13\\test.txt"

print(mypuzzle(getList(fileName)))

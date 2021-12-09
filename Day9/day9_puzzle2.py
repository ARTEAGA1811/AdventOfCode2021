def myPuzzle():
    arr = getArr(getList())
    lows = []
    lowsIndex = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == 0 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))

            elif i == 0:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif j == 0:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif j == len(arr[i])-1:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            else:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
    #print(lows)
    return lowsIndex

def mypuzzleTwoCuencas(lowsIndex:list):
    arr = getArr(getList())
    logs = []
    def getNewLocations(position:tuple):
        i = position[0]
        j = position[1]
        if i == 0 and j == 0:
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))

            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))

        elif i == 0 and j == len(arr[i])-1:
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
                
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
                
        elif i == len(arr)-1 and j == 0:
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
                
            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif i == len(arr)-1 and j == len(arr[i])-1:
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))

            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif i == 0:
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
        
        elif i == len(arr)-1:
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
        
        elif j == 0:
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif j == len(arr[i])-1:
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        else:
            #right
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #left
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
            #up
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

    lenBasinsList = []
    for i in range(len(lowsIndex)):
        
        getNewLocations(lowsIndex[i])
        lenBasinsList.append(len(logs)+1)
        logs = []
    
    lenBasinsList.sort()
    return lenBasinsList[-1] * lenBasinsList[-2] * lenBasinsList[-3]
   



def getList():
    with open("Day9\day9_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

def getArr(arr:list):
    newArr = []
    for i in range(len(arr)):
        aux = [int(x) for x in arr[i]]
        newArr.append(aux)
    return newArr


#Print solution
print(mypuzzleTwoCuencas(myPuzzle()))
def mypuzzle(arr:list):
    newArr = []
    used = set()
    for i in range(len(arr)):
        aux = [int(x) for x in arr[i]]
        newArr.append(aux)
    
    def analisis(i,j):
        #base case
        if (i,j) not in used:
            if newArr[i][j] < 9:
                newArr[i][j] += 1
                return
        
        #recursive case
        if (i,j) not in used:
            used.add((i,j))
            newArr[i][j] = 0
            #call analisis for all the neighbors, including the adjacent ones
            if i > 0:
                analisis(i-1,j)
            if j > 0:
                analisis(i,j-1)
            if i < len(newArr)-1:
                analisis(i+1,j)
            if j < len(newArr[0])-1:
                analisis(i,j+1)
            #call analisis for the adjacent ones
            if i > 0 and j > 0:
                analisis(i-1,j-1)
            if i > 0 and j < len(newArr[0])-1:
                analisis(i-1,j+1)
            if i < len(newArr)-1 and j > 0:
                analisis(i+1,j-1)
            if i < len(newArr)-1 and j < len(newArr[0])-1:
                analisis(i+1,j+1)

    for buc in range(1000000):
        used = set()    
        for i in range(len(newArr)):
            for j in range(len(newArr[0])):
                analisis(i,j)
        #print(newArr)
        if len(used) == len(newArr)*len(newArr[0]):
            return buc+1

def getList():
    with open("Day11\day11_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

print(mypuzzle(getList()))
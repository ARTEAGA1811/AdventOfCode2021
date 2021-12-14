def mypuzzle(arr:list):
    template = 'KBKPHKHHNBCVCHPSPNHF'
    #template = 'NNCB'
    mylogs = {}
    for i in range(len(arr)):
        mylogs[arr[i][:2]] = arr[i][6]
    
    myList = []
    for i in template:
        myList.append(i)

    #print(myList)
    for i in range(10):
        indAux = 1
        aux = myList.copy()
        for j in range(1,len(myList)):
            aux.insert(indAux,mylogs[myList[j-1]+myList[j]])
            indAux += 2
        myList = aux
        #print(myList)
    myDict = {}
    for i in myList:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    #print(myDict)
    values = list(myDict.values())
    return max(values) - min(values)
    

def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day14\day14_puzzle_list.txt"
fileName = "Day14\\test.txt"

print(mypuzzle(getList(fileName)))
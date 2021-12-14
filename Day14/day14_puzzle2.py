def mypuzzle(arr:list):
    template = 'KBKPHKHHNBCVCHPSPNHF'
    #template = 'NNCB'
    mylogs = {}
    for i in range(len(arr)):
        mylogs[arr[i][:2]] = arr[i][6]
    
    myList = []
    for i in template:
        myList.append(i)

    memo = {}
    def recursiveFun(letters:str, cont, level):
        if (letters, level)  in memo:
            return memo[(letters, level)].copy()
                
        if cont == 40:
            return {mylogs[letters]: 1}

        #recursive call
        temp = {}
        tempTwo = {}        
        temp = recursiveFun(letters[0]+mylogs[letters], cont+1, level+1)
        tempTwo = recursiveFun(mylogs[letters]+letters[1], cont+1, level+1)
        for key, value in tempTwo.items():
            if key in temp:
                temp[key] += value
            else:
                temp[key] = value
        
        if mylogs[letters] in temp:
            temp[mylogs[letters]] += 1
        else:
            temp[mylogs[letters]] = 1

        memo[(letters, level)] = temp.copy()
        return temp

    newDict = {}
    for i in range(1,len(myList)):
        gg = recursiveFun(myList[i-1]+myList[i], 1, 1)

        for key, value in gg.items():
            if key in newDict:
                newDict[key] += value
            else:
                newDict[key] = value

    for k in range(len(myList)):
        if myList[k] in newDict:
            newDict[myList[k]] += 1
        else:
            newDict[myList[k]] = 1

    values = list(newDict.values())

    return max(values) - min(values)
    







def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day14\day14_puzzle_list.txt"
fileName = "Day14\\test.txt"

print(mypuzzle(getList(fileName)))
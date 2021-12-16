def convertHexToBinList(hexString:str):
    aux = ""
    for i in hexString:
        aux += bin(int(i, 16))[2:].zfill(4)
    return aux

def mypuzzle(arr:list):
    bitList = convertHexToBinList(arr[0])

    numVersions = []

    def getNumVersions(chain:list, curIndex:int):
        #print(chain)
        if len(chain) <6:
            return (len(chain)-1,-1)
        version = int(chain[curIndex:curIndex+3],2)
        id = int(chain[curIndex+3:curIndex+6],2)
        numVersions.append(version)
        finalInd = 0
        if id == 4:
            value = ''
            finalInd = curIndex+6
            aux = True
            while aux:            
                if chain[finalInd] == "0":
                    aux = False
                
                value+=chain[finalInd+1:finalInd+5]
                finalInd += 5
            

            return (finalInd,int(value,2))

        else:
            values = []

            lengthTypeId = int(chain[curIndex+6],2)    
            if lengthTypeId == 0:
                if len(chain) < curIndex+22:
                    return (len(chain)-1,-1)
                leBits = int(chain[curIndex+7:curIndex+22],2)
                finalInd = curIndex+22
                while finalInd < curIndex+22+leBits:
                    auxTuple = getNumVersions(chain[finalInd:finalInd+leBits],0)
                    #print(auxTuple)
                    finalInd += auxTuple[0]
                    if auxTuple[1] != -1:
                        values.append(auxTuple[1])

            else:
                if len(chain) < curIndex+18:
                    return (len(chain)-1,-1)
                numSubPackets = int(chain[curIndex+7: curIndex+18],2)
                finalInd = curIndex+18
                for i in range(numSubPackets):
                    #getNumVersions(chain[18+i*5:18+(i+1)*5])
                    if finalInd == len(chain)-1:
                        break

                    auxTuple = getNumVersions(chain[finalInd:],0)
                    finalInd += auxTuple[0]
                    if auxTuple[1] != -1:
                        values.append(auxTuple[1])
            
            if id == 0:
                return (finalInd, sum(values))
            elif id == 1:
                #print(values)
                prod = 1
                for i in values:
                    prod = prod * i
                return (finalInd, prod)
            elif id == 2:
                return (finalInd, min(values))
            elif id == 3:
                return (finalInd, max(values))
            elif id == 5:
                if values[0] > values[1]:
                    return (finalInd, 1)
                else:
                    return (finalInd, 0)
            elif id == 6:
                if values[0] < values[1]:
                    return (finalInd, 1)
                else:
                    return (finalInd, 0)
            elif id == 7:
                if values[0] == values[1]:
                    return (finalInd, 1)
                else:
                    return (finalInd, 0)

    
    myvalue = getNumVersions(bitList,0)
    return sum(numVersions), myvalue[1]


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day16\day16_puzzle_list.txt"
fileName = "Day16\\test.txt"

print(mypuzzle(getList(fileName)))

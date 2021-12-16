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
            return len(chain)-1
        version = int(chain[curIndex:curIndex+3],2)
        id = int(chain[curIndex+3:curIndex+6],2)
        numVersions.append(version)
        finalInd = 0
        if id == 4:
            finalInd = curIndex+6
            aux = True
            while aux:
                if chain[finalInd] == "0":
                    aux = False
                finalInd += 5    

            return finalInd

        else:

            lengthTypeId = int(chain[curIndex+6],2)    
            if lengthTypeId == 0:
                leBits = int(chain[curIndex+7:curIndex+22],2)
                finalInd = curIndex+22
                while finalInd < curIndex+22+leBits:
                    finalInd += getNumVersions(chain[finalInd:finalInd+leBits],0)

            else:
                numSubPackets = int(chain[curIndex+7: curIndex+18],2)
                finalInd = curIndex+18
                for i in range(numSubPackets):
                    #getNumVersions(chain[18+i*5:18+(i+1)*5])
                    if finalInd == len(chain)-1:
                        break
                    finalInd += getNumVersions(chain[finalInd:],0)

            return finalInd
    
    getNumVersions(bitList,0)
    return sum(numVersions)


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day16\day16_puzzle_list.txt"
fileName = "Day16\\test.txt"

print(mypuzzle(getList(fileName)))

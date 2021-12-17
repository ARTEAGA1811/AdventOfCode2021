def mypuzzle():
    rangeX = [155,182]
    rangeY = [-117,-67]

    return int(116*117/2) #lol, cuando me di cuenta que era una sumatoria quede .___.


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day##\day##_puzzle_list.txt"
#fileName = "Day##\\test.txt"

#print(mypuzzle(getList(fileName)))
print(mypuzzle())
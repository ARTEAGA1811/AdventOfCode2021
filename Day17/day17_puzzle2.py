def getAllStepsXx(myXx:int,myrangeX:list):
    auxSet = set()
    cont = myXx-1
    position = myXx
    step = 1
    lastInd= 0
    if myrangeX[0] <= position <= myrangeX[1]:
        auxSet.add(step)

    step += 1

    while True:
        if cont == 0:
            for m in range(600):
                auxSet.add(step)
                step += 1
            break  

        position = position + cont
        if position > myrangeX[1]:
            break 
                 
        if myrangeX[0] <= position <= myrangeX[1]:
            auxSet.add(step)
        cont -= 1
        step += 1
    return auxSet


def getAllStepsYy(myYy:int, myrangeY:list):
    auxSet = set()
    cont = myYy-1
    position = myYy
    step = 1

    if myYy>0:
        step = myYy*2 + 1
        position = 0
        cont = (myYy+1)*-1

    if myrangeY[0] <= position <= myrangeY[1]:
        auxSet.add(step)


    step += 1
    # cont = cont -1
    while True:
        position = position + cont
        if position < myrangeY[0]:
            break

        if myrangeY[0] <= position <= myrangeY[1]:
            auxSet.add(step)
        cont -= 1
        step += 1
    return auxSet

def mypuzzle():
    rangeX = [155,182]
    rangeY = [-117,-67]
    # rangeX = [20,30]
    # rangeY = [-10,-5]

    minX = 0
    i = 0
    while True:
        if (i*(i+1)/2) >= rangeX[0] and (i*(i+1)/2) <= rangeX[1]:
            minX = i
            break
        i += 1
  
    # logStepsXx = {int(x):set() for x in range(minX,rangeX[1]+1)}
    logStepsYy = {int(y):set() for y in range(rangeY[0],((rangeY[0]+1)*-1)+1,1)}
    logStepsXx = {int(x):set() for x in range(18,rangeX[1]+1)}
    #logStepsYy = {int(y):set() for y in range(-10000,10000+1)}

    for key in logStepsXx:
        logStepsXx[key] = getAllStepsXx(key,rangeX)
    for key in logStepsYy:
        logStepsYy[key] = getAllStepsYy(key,rangeY)

    total = 0
    for keyXx in logStepsXx:
        for keyYy in logStepsYy:
            # print(keyXx,keyYy)
            # print(logStepsXx[keyXx].intersection(logStepsYy[keyYy]),end="\n")
            if len(logStepsXx[keyXx].intersection(logStepsYy[keyYy])) > 0:
                total += 1
            #total += len(logStepsXx[keyXx].intersection(logStepsYy[keyYy]))

    return total


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day##\day##_puzzle_list.txt"
#fileName = "Day##\\test.txt"

#print(mypuzzle(getList(fileName)))
print(mypuzzle())
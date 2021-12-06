import collections
def mypuzzleday6():
    fishList = [3,5,1,2,5,4,1,5,1,2,5,5,1,3,1,5,1,3,2,1,5,1,1,1,2,3,1,3,1,2,1,1,5,1,5,4,5,5,3,3,1,5,1,1,5,5,1,3,5,5,3,2,2,4,1,5,3,4,2,5,4,1,2,2,5,1,1,2,4,4,1,3,1,3,1,1,2,2,1,1,5,1,1,4,4,5,5,1,2,1,4,1,1,4,4,3,4,2,2,3,3,2,1,3,3,2,1,1,1,2,1,4,2,2,1,5,5,3,4,5,5,2,5,2,2,5,3,3,1,2,4,2,1,5,1,1,2,3,5,5,1,1,5,5,1,4,5,3,5,2,3,2,4,3,1,4,2,5,1,3,2,1,1,3,4,2,1,1,1,1,2,1,4,3,1,3,1,2,4,1,2,4,3,2,3,5,5,3,3,1,2,3,4,5,2,4,5,1,1,1,4,5,3,5,3,5,1,1,5,1,5,3,1,2,3,4,1,1,4,1,2,4,1,5,4,1,5,4,2,1,5,2,1,3,5,5,4,5,5,1,1,4,1,2,3,5,3,3,1,1,1,4,3,1,1,4,1,5,3,5,1,4,2,5,1,1,4,4,4,2,5,1,2,5,2,1,3,1,5,1,2,1,1,5,2,4,2,1,3,5,5,4,1,1,1,5,5,2,1,1]
    #fishList = [3,4,3,1,2]
    #fishList.sort()
    mydict = {}
    def fOne(value:int):
        day = 0
        #Part one
        day = value+1
        #add to dictionary if not already there
        if day not in mydict:
            mydict[day] = 1
        else:
            mydict[day] += 1
        #part two
        for i in range(day+7, 80+1, 7):
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1

    def fTwo(day:int, numBorns:int):
        #Part one
        day = day+9
        if day > 80:
            return False
        else:
            #add to dictionary if not already there
            if day not in mydict:
                mydict[day] = numBorns
            else:
                mydict[day] += numBorns

        #part two
        for i in range(day+7, 80+1, 7):
            if i not in mydict:
                mydict[i] = numBorns
            else:
                mydict[i] += numBorns
    
    for i in range(len(fishList)):
        fOne(fishList[i])
    
    result = collections.OrderedDict(sorted(mydict.items()))
    print(result)
    
    for i in range(80+1):
        if i in mydict:
            fTwo(i, mydict[i])

    aux = 0
    for key, value in mydict.items():
        aux+=value

    print(mydict)
    return len(fishList) + aux
        


#print the result
print(mypuzzleday6())

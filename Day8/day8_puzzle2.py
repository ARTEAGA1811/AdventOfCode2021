def myPuzzle(displayList:list):
    solved = {}
    mymap = {}
    used = set()
    totalSum = 0
    #displayList = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    for i in range(len(displayList)):
        line = displayList[i].split(" | ")
        signals = line[0].split(" ")
        output = line[1].split(" ")
        #add 1,4,7,8 to mymap
        for j in range(len(signals)):
            if len(signals[j]) == 2:
                solved[1] = signals[j]
                used.add(j)
            elif len(signals[j]) == 3:
                solved[7] = signals[j]
                used.add(j)
            elif len(signals[j]) == 4:
                solved[4] = signals[j]
                used.add(j)
            elif len(signals[j]) == 7:
                solved[8] = signals[j]
                used.add(j)
        #get the different character from solved[1] and solved[7]
        tempOne = set(solved[7])
        tempTwo = set(solved[1])
        #map a.
        mymap["a"] = list(tempOne.difference(tempTwo))[0]

        #get the common character from solved[1] and solved[7]
        a_difSize2 = tempOne.intersection(tempTwo)

        #get signal 3.
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 5:
                    if len(set(signals[j]) | a_difSize2) == 5:
                        solved[3] = signals[j]
                        used.add(j)
                        break
        
        b_difSize2 = set(solved[3]) - (set(mymap["a"])| a_difSize2)

        #get signal 0 and map g,d.
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 6:
                    if len(set(signals[j]) | b_difSize2) != 6:
                        solved[0] = signals[j]
                        used.add(j)
                        aux = list(b_difSize2)
                        
                        if len(set(signals[j]) | set(aux[0])) == 6:
                            mymap["g"] = aux[0]
                            mymap["d"] = aux[1]
                        else:
                            mymap["g"] = aux[1]
                            mymap["d"] = aux[0]
                        break
                                
        #get signal 9.      
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 6:   
                    if len(set(signals[j]) | a_difSize2) == 6:
                        solved[9] = signals[j]
                        used.add(j)
                        break
        
        #get signal 6.
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 6:
                    solved[6] = signals[j]
                    used.add(j)
                    break
        
        aux = set(solved[9]) - (set(mymap["g"]) | set(mymap["d"]) | set(mymap["a"]) | a_difSize2)
      
        #get signal 5.
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 5:
                    if len(set(signals[j]) | aux) == 5:
                        solved[5] = signals[j]
                        used.add(j)
                        break
        #get signal 2.
        for j in range(len(signals)):
            if j not in used:
                if len(signals[j]) == 5:
                    solved[2] = signals[j]
                    used.add(j)
                    break
        
        digit = ""
        for k in range(len(output)):
            for key,value in solved.items():
                if len(solved[key]) == len(output[k]):
                    if len(set(output[k]) | set(solved[key])) == len(output[k]):
                        digit += str(key)
                        break
        totalSum += int(digit)
        solved = {}
        mymap = {}
        used = set()

    return totalSum
                    





        
def getList():
    with open("Day8\day8_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]


#Print solution
print(myPuzzle(getList()))

#1 hora hasta entender el ejercicio
#2 horas creando el algoritmo en una hoja xd
#media hora de codigo

#modo serio .__.
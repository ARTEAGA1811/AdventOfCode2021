def myPuzzleDay3(report: list):
    aux = {int(x) for x in range(0,len(report))}
    tam = len(report[0])
    mydict = {0:0, 1:0}
    oxingG = ""
    co2 = ""
    eliminated = set()
    winner = ""
    i = 0
    for i in range(tam):
        if len(eliminated) == len(report)-1:
            aux2 = aux - eliminated
            oxingG = report[list(aux2)[0]]
            break

        for j in range(len(report)):
            if j in eliminated:
                continue

            if report[j][i] == "0":
                mydict[0] += 1
            else:
                mydict[1] += 1
        if mydict[1] >= mydict[0]:
            winner = "1"
        else:
            winner = "0"
        mydict = {0:0, 1:0}

        #add to eliminated
        for j in range(len(report)):
            if report[j][i] != winner:
                eliminated.add(j)
    
    aux2 = aux - eliminated
    oxingG = report[list(aux2)[0]]

    eliminated.clear()
    mydict = {0:0, 1:0}
    for i in range(tam):
        if len(eliminated) == len(report)-1:
            aux2 = aux - eliminated
            co2 = report[list(aux2)[0]]
            break

        for j in range(len(report)):
            if j in eliminated:
                continue

            if report[j][i] == "0":
                mydict[0] += 1
            else:
                mydict[1] += 1
        if mydict[0] <= mydict[1]:
            winner = "0"
        else:
            winner = "1"
        mydict = {0:0, 1:0}

        #add to eliminated
        for j in range(len(report)):
            if report[j][i] != winner:
                eliminated.add(j)

    aux2 = aux - eliminated
    co2 = report[list(aux2)[0]]
  
    
    return int(oxingG,2) * int(co2,2)

def getList():
    with open("Day3\day3_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

#Print the result
print(myPuzzleDay3(getList()))
gg = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
print(myPuzzleDay3(gg))

#humm I think this is not my best solution, but it works. hehe

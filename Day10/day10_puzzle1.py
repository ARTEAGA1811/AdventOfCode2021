def mypuzzle(route:list):
    input = {"(","[","<","{"}
    output = {")","]",">","}"}
    aux = {")":"(","]":"[",">":"<","}":"{"}
    aux2 = {"(":")","[":"]","<":">","{":"}"}
    score = {"}":3,")":1,"]":2,">":4}
    total = 0
    myStack = []
    sumTotal = []
    for i in range(len(route)):
        
        flag = False
        for j in range(len(route[i])):
            if route[i][j] in input:
                myStack.append(route[i][j])
                
            elif route[i][j] in output:
                if len(myStack) == 0:
                    flag = True
                    break

                elif myStack[-1] == aux[route[i][j]]:
                    myStack.pop() 
                else:
                    flag = True
                    break
        if flag == False:
            total = 0
            if len(myStack) != 0:
                for k in range(len(myStack)-1,-1,-1):
                    total = total * 5
                    total = total + score[aux2[myStack[k]]]
                sumTotal.append(total)
        myStack = []
    sumTotal.sort()
    print(sumTotal)
    media = len(sumTotal)//2
    return sumTotal[media]
   
  
def getList():
    with open("Day10\day10_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

# def getList():
#     with open("Day10\\test.txt") as f:
#         return [str(line.strip()) for line in f]


print(mypuzzle(getList()))
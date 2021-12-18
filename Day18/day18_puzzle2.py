import math
import ast
import time
def convertHomework(arr:list):
    aux = []
    for i in range(len(arr)):
        if arr[i] == '[':
            aux.append(-1)
        elif arr[i] == ']':
            aux.append(-2)
        elif arr[i] == ',' or arr[i] == ' ':
            continue
        else:
            aux.append(int(arr[i]))
    return aux


def returnToitsOriginal(arr:list):
    chain = ''
    #print(arr)
    for i in range(1,len(arr)):
        if arr[i-1] == -1:
            chain += '['
        elif arr[i-1] == -2:
            chain += ']'
        else:
            chain += str(arr[i-1])
        
        op1 = arr[i-1] != -1 and arr[i-1] != -2 and arr[i] != -1 and arr[i] != -2
        op2 = arr[i-1] == -2 and arr[i] != -1 and arr[i] != -2
        op3 = arr[i-1] == -2 and arr[i] == -1
        op4 = arr[i-1] != -1 and arr[i-1] != -2 and arr[i] == -1

        if op1 or op2 or op3 or op4:
            chain += ','

    if arr[-1] == -1:
        chain += '['
    elif arr[-2] == -2:
        chain += ']'
    else:
        chain += str(arr[i])
    #print(chain)
    return list(ast.literal_eval(chain))
    

def sumMyList(currSum:list, arr:list):
    newSumArr = [-1]+ currSum + arr + [-2]
    #newSumArr = [-1]+ currSum + [-2]
    # print('hello')
    # print(returnToitsOriginal(newSumArr))
    # print('\n')
    #explode
    def explode(newSumArr:list):
        anewSumArr = newSumArr.copy()
        change = True
        iDidSomething = False
        while change:
            #print("gg")
            #print(returnToitsOriginal(anewSumArr))


            change = False
            for i in range(3,len(anewSumArr)):
                #check if there's coincidence [num,num]
                if anewSumArr[i] == -2 and anewSumArr[i-3] == -1:
                    #check if this pair is between 4 pairs
                    cont = 0
                    for k in  range(i-3-1, -1, -1):
                        if anewSumArr[k] == -1:
                            cont+=1
                        if anewSumArr[k] == -2:
                            cont -= 1

                    if cont >= 4:
                        iDidSomething = True
                        #print("selected: ", anewSumArr[i-2], anewSumArr[i-1]) 
                        #sum the element that is on the left of the pair
                        for j in range(i-3,-1,-1):
                            if anewSumArr[j] != -1 and anewSumArr[j] != -2:
                                anewSumArr[j] += anewSumArr[i-2]
                                break
                        #sum the element that is on the right of the pair
                        for j in range(i+1,len(anewSumArr)):
                            if anewSumArr[j] != -1 and anewSumArr[j] != -2:
                                anewSumArr[j] += anewSumArr[i-1]
                                break
                        #remove the pair from the list and add a zero in the place of the pair
                        anewSumArr = anewSumArr[:i-3] + [0] + anewSumArr[i+1:]
                        change = True
                        break

        return anewSumArr
    
    #divide
    def divide(newSumArr:list):
        #print("Voy a hacer el divide")
        #print(returnToitsOriginal(newSumArr))
        anewSumArr = newSumArr.copy()        

        for i in range(len(anewSumArr)):
            if anewSumArr[i] != -1 and anewSumArr[i] != -2 and anewSumArr[i] >=10:
                #print("encontre en divide uno," , anewSumArr[i])
                a = math.floor(anewSumArr[i] / 2)
                b = math.ceil(anewSumArr[i] / 2)
                #insert [a,b] in the position of newSumArr[i] and remove the old value
                anewSumArr = anewSumArr[:i] + [-1]+[a]+[b]+[-2] + anewSumArr[i+1:]
                #print("new: ", returnToitsOriginal(anewSumArr))
                return True, anewSumArr

        return False, anewSumArr

    while True:
        newSumArr = explode(newSumArr)
        tupleAux = divide(newSumArr)
        newSumArr = tupleAux[1]
        if tupleAux[0]:
            continue
        else:
            break
    
    return newSumArr


def mypuzzle(arr:list):
    #currSum = convertHomework(arr[0])
    # for i in range(1,len(arr)):
    #     temp = convertHomework(arr[i])
    #     currSum = sumMyList(currSum, temp)
    #     #print(currSum)
    #     #print("retorna")
    #     #print(returnToitsOriginal(currSum))
    #     #time.sleep(5)
    addtionList = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            currSum = sumMyList(convertHomework(arr[i]), convertHomework(arr[j]))
            aux = currSum.copy()
            addtionList.append(returnToitsOriginal(aux))

            currSum = sumMyList(convertHomework(arr[j]), convertHomework(arr[i]))
            aux = currSum.copy()
            addtionList.append(returnToitsOriginal(aux))

    #calcutate its magnitude
    magnitude = 0
    #print(currSum)
    #currSum = returnToitsOriginal(currSum)
    #print(currSum)
    #print(returnToitsOriginal(currSum))
    def getMagnitude(currSum:list):
        if type(currSum) == int:
            return currSum

        total = 0
        total+=getMagnitude(currSum[0]) * 3
        total+=getMagnitude(currSum[1]) * 2
        return total

    #magnitude = getMagnitude(currSum)

    for k in range(len(addtionList)):
        magnitude = max(magnitude, getMagnitude(addtionList[k]))
        
    return magnitude



    



def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day18\day18_puzzle_list.txt"
fileName = "Day18\\test.txt"

print(mypuzzle(getList(fileName)))
#print(sumMyList(convertHomework("[[[[0, [[4, [7, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]]]"),[]))
#print(returnToitsOriginal([-1, -1, -1, -1, -1, 0, -1, -1, 4, -1, 7, 6, -2, -2]))
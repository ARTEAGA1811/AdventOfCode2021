import numpy as np


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day15\day15_puzzle_list.txt"
fileName = "Day15\\test.txt"
arr = np.zeros((4,3))

newArr = []
for i in range(len(arr)):
    newArr.append([int(x) for x in arr[i]])
cont = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = cont
        cont += 1
gg = [0,3,6,9]
for i in range(4):
    arrAux = arr[:, gg[i]:gg[i]+3].copy()
    arrTwo = arrAux.copy()
    for i in range(len(arrTwo)):
        for j in range(len(arrTwo[i])):
            if arrTwo[i][j] == 9:
                arrTwo[i][j] = 1
                continue
            arrTwo[i][j] = arrTwo[i][j] + 1
    #add arrTwo to arr
    arr = np.concatenate((arr, arrTwo), axis=1)
#print(arr)

#I must add the new rows.
gg = [0,4,8,12]
for i in range(4):
    arrAux = arr[gg[i]:gg[i]+4, :].copy()
    arrTwo = arrAux.copy()
    for i in range(len(arrTwo)):
        for j in range(len(arrTwo[i])):
            if arrTwo[i][j] == 9:
                arrTwo[i][j] = 1
                continue
            arrTwo[i][j] = arrTwo[i][j] + 1
    #add arrTwo to arr
    arr = np.concatenate((arr, arrTwo), axis=0)
print(arr)
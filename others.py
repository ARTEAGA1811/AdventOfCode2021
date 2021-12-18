# import numpy as np


# def getList(fileName:str):
#     with open(fileName) as f:
#         return [str(line.strip()) for line in f]

# #fileName = "Day15\day15_puzzle_list.txt"
# fileName = "Day15\\test.txt"
# arr = np.zeros((4,3))

# newArr = []
# for i in range(len(arr)):
#     newArr.append([int(x) for x in arr[i]])
# cont = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j] = cont
#         cont += 1
# gg = [0,3,6,9]
# for i in range(4):
#     arrAux = arr[:, gg[i]:gg[i]+3].copy()
#     arrTwo = arrAux.copy()
#     for i in range(len(arrTwo)):
#         for j in range(len(arrTwo[i])):
#             if arrTwo[i][j] == 9:
#                 arrTwo[i][j] = 1
#                 continue
#             arrTwo[i][j] = arrTwo[i][j] + 1
#     #add arrTwo to arr
#     arr = np.concatenate((arr, arrTwo), axis=1)
# #print(arr)

# #I must add the new rows.
# gg = [0,4,8,12]
# for i in range(4):
#     arrAux = arr[gg[i]:gg[i]+4, :].copy()
#     arrTwo = arrAux.copy()
#     for i in range(len(arrTwo)):
#         for j in range(len(arrTwo[i])):
#             if arrTwo[i][j] == 9:
#                 arrTwo[i][j] = 1
#                 continue
#             arrTwo[i][j] = arrTwo[i][j] + 1
#     #add arrTwo to arr
#     arr = np.concatenate((arr, arrTwo), axis=0)
# print(arr)


# def convertHexToBinList(hexString:str):
#     aux = ""
#     for i in hexString:
#         aux += bin(int(i, 16))[2:].zfill(4)
#     return aux


    

# #print(convertHexToBinList("8A004A801A8002F478"))
# # print(convertHexToBinList("D2FE28"))
# print(convertHexToBinList("38006F45291200"))
# # print(convertHexToBinList("3"))
# # #print(bin(int("3",16))[2:].zfill(4))

# aux = [3,2,1]
# #determine if aux is a number or a list
# if type(aux) == list:
#     print("list")
# else:
#     print("number")



# [-1, -1, -1, -1, -1, 0, -1, -1, 4, -1, 7, 6, -2, -2]




def getMagnitude(currSum:list):
        if type(currSum) == int:
            return currSum

        total = 0
        total+=getMagnitude(currSum[0]) * 3
        total+=getMagnitude(currSum[1]) * 2
        return total

print(getMagnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]))
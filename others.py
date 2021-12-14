import numpy as np
arr = np.zeros((9,5))
cont = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = cont
        cont += 1

print(arr)

partOne = arr[:, 1:4]
print("Part One:")
print(partOne)

partTwo = arr[2:5, :]
print("Part Two:")
print(partTwo)

partTree = arr[5:7, 1:4]
print("Part Tree:")
print(partTree)

partFour = arr[:, 2:1000]
print("Part Four:")
print(partFour)
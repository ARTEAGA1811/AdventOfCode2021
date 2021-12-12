#principal template
def mypuzzle(arr:list):
    pass


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day##\day##_puzzle1_list.txt"
#fileName = "Day##\\test.txt"

print(mypuzzle(getList(fileName)))


#get the input as a array of numbers
arr = [[]]
newArr = []
for i in range(len(arr)):
    newArr.append([int(x) for x in arr[i]])


#this is a way I can access to the neighbors in an array

#call function for all the neighbors, including the adjacent ones
# if i > 0:
#     #analisis(i-1,j)
# if j > 0:
#     #analisis(i,j-1)
# if i < len(newArr)-1:
#     #analisis(i+1,j)
# if j < len(newArr[0])-1:
#     #analisis(i,j+1)
# #call analisis for the adjacent ones
# if i > 0 and j > 0:
#     #analisis(i-1,j-1)
# if i > 0 and j < len(newArr[0])-1:
#     #analisis(i-1,j+1)
# if i < len(newArr)-1 and j > 0:
#     #analisis(i+1,j-1)
# if i < len(newArr)-1 and j < len(newArr[0])-1:
#     #analisis(i+1,j+1)
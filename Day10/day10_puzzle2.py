def mypuzzle():
    pass
def getList():
    with open("Day10\day10_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]


print(mypuzzle(getList()))
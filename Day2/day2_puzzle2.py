def myPuzzleDay2(commands:list):
    horpos = 0
    depth = 0
    aim = 0
    for command in commands:
        aux = command.split(" ")
        if aux[0] == "up":
            aim -= int(aux[1])
        if aux[0] == "down":
            aim += int(aux[1])
        if aux[0] == "forward":
            horpos += int(aux[1])
            depth += aim*int(aux[1])

    return horpos * depth

def getList():
    with open("Day2\day2_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

#print result
print(myPuzzleDay2(getList()))
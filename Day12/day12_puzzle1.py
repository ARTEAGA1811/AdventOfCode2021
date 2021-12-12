def mypuzzle(arr:list):
    logs = {}
    visited = {"start"}
    myauz = {}
    ways = 0
    for i in arr:
        aux = i.split("-")

        if aux[0] not in logs:
            logs[aux[0]] = {aux[1]}
            
        else:
            logs[aux[0]].add(aux[1])
 
        if aux[1] not in logs:
            logs[aux[1]] = {aux[0]}

        else:
            logs[aux[1]].add(aux[0])


        if aux[0] not in myauz:
            myauz[aux[0]] = set()
        if aux[1] not in myauz:
            myauz[aux[1]] = set()
    
    def bfs(letra:str):
        #print(letra)
        #base case
        
        if letra == "end":
            return 1
        if letra in visited :
            return 0
        
        if letra.islower():
            visited.add(letra)

        #recursive case
        total = 0
        for i in logs[letra]:
            if i not in myauz[letra]:
                myauz[letra].add(i)
                total += bfs(i)
                myauz[letra].remove(i)
        if letra.islower():
            visited.remove(letra)
        return total

    for i in logs["start"]:
        ways += bfs(i)
        visited.clear()
        visited.add("start")
    
    return ways

        


def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

#fileName = "Day12\day12_puzzle_list.txt"
fileName = "Day12\\test.txt"

print(mypuzzle(getList(fileName)))
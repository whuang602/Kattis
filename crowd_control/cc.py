def getInput(street_list):
    max = 0
    inte, strts = [int(x) for x in input().split()]
    while (strts > 0):
        temp_input = [int(x) for x in input().split()]
        street_list.append(temp_input)
        strts -= 1
        if (temp_input[2] > max):
            max = temp_input[2]
    return inte, strts, max

def makeList(inte, street_list):
    nodes = []
    
    for x in range(inte):
        nodes.append([])

    for streets in street_list:
        nodes[streets[0]].append([streets[1],streets[2]])
        nodes[streets[1]].append([streets[0],streets[2]])

    return nodes

def sortStreetWeight(street_list):
    sorted_street = street_list
    for index in range(len(sorted_street)):
        for index2 in range(0, len(sorted_street)-index-1):
            if sorted_street[index2][2] < sorted_street[index2+1][2]:
                sorted_street[index2], sorted_street[index2+1] = sorted_street[index2+1], sorted_street[index2]
    return sorted_street

def maxChild(inte, nodes, vertex, visited):
    max = 0
    max_child = None
    for child in nodes[vertex]:
        if (child[0] == inte-1):
            return child[0]
        if (child[0] in visited):
            continue
        if (child[1] > max):
                max = child[1]
                max_child = child[0]
    return max_child

def findMin(path, max, nodes):
    min = max
    to_visit = path.copy()
    while len(to_visit) > 1:
        for street in nodes[to_visit[0]]:
            if (street[0] == to_visit[1] and street[1] < min):
                min = street[1]
        to_visit.pop(0)
    return min

def dijkstra(inte, max, nodes):
    paths = []
    for child in nodes[0]:
        curr_path = []
        curr_path.append(0)
        curr_path.append(child[0])
        if curr_path[-1] == inte-1:
            paths.append(curr_path)
            continue
        not_found = True
        while not_found:
            max_child = maxChild(inte, nodes, curr_path[-1], curr_path)
            if max_child == inte-1:
                not_found = False
            if max_child == None:
                continue
            curr_path.append(max_child)
        paths.append(curr_path)
    
    min = findMin(paths[0], max, nodes)
    max_path = paths[0]
    for path in paths:
        path_min = findMin(path, max, nodes)
        if (path_min > min):
            min = path_min
            max_path = path
    return max_path

def Travel_Path(street_list, max_path):
    short_street = []
    for street in street_list:
        short_street.append([street[0], street[1]])

    to_visit = max_path.copy()
    travel_path = []
    while len(to_visit) > 1:
        for street in nodes[to_visit[0]]:
            if (street[0] == to_visit[1]):
                try:
                    travel_path.append(short_street.index([to_visit[0],to_visit[1]]))
                except ValueError:
                    travel_path.append(short_street.index([to_visit[1],to_visit[0]]))
        to_visit.pop(0)
    return travel_path

def blockPaths(street_list, max_path, inte):
    blocked_paths = list(range(len(street_list)))
    block_list = street_list.copy()
    travel_path = Travel_Path(street_list, max_path)

    unvisited = list(range(inte))
    for intersection in max_path:
        unvisited.remove(intersection)
    
    index = 0
    for street in block_list:
        if ((street[0] in unvisited and street[1] in unvisited) or (street[0] in max_path and street[1] in max_path and block_list.index(street) in travel_path)):
            street = []
            blocked_paths.remove(index)
        index+=1
    
    return blocked_paths


street_list=[]
inte, strts, max = getInput(street_list)
nodes = makeList(inte,street_list)
max_path = dijkstra(inte, max, nodes)
blocked_paths = blockPaths(street_list, max_path, inte)
blocked_paths.sort()
if len(blocked_paths) == 0:
    print("none")
else:
    print(*blocked_paths)

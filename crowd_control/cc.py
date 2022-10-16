def getInput(street_list):
    inte, strts = [int(x) for x in input().split()]
    while (strts > 0):
        temp_input = [int(x) for x in input().split()]
        street_list.append(temp_input)
        strts -= 1
    return inte, strts

def makeList(inte, street_list):
    nodes = []
    
    for x in range(inte):
        nodes.append([])

    for streets in street_list:
        nodes[streets[0]].append([streets[1],streets[2]])
        nodes[streets[1]].append([streets[0],streets[2]])

    return nodes

def sortStreetWeight(street_list):
    sorted_street = street_list.copy()
    for index in range(len(sorted_street)):
        for index2 in range(0, len(sorted_street)-index-1):
            if sorted_street[index2][2] < sorted_street[index2+1][2]:
                sorted_street[index2], sorted_street[index2+1] = sorted_street[index2+1], sorted_street[index2]
    return sorted_street

def DFS(vertex, mst_nodes, inte):
    visited1 = []
    visited2 = []
    DFSrecur(vertex, mst_nodes, visited1, inte)
    DFSrecur(inte-1, mst_nodes, visited2, inte)

    path = []
    index1 = visited1.index(inte-1)
    index2 = 0
    while 0 not in path:
        while visited1.index(visited2[index2]) > index1:
            index2 +=1
        index1 = visited1.index(visited2[index2])
        path.append(visited2[index2])
        index2 += 1
    return path
    
def DFSrecur(vertex, mst_nodes, visited, inte):
    try:
        visited.append(vertex)
        for child in mst_nodes[vertex]:
            if child[0] not in visited:
                DFSrecur(child[0], mst_nodes, visited, inte)
    except TypeError:
        visited.append(vertex)

def Travel_Path(street_list, max_path):
    short_street = []
    for street in street_list:
        short_street.append([street[0], street[1]])

    travel_path = []
    for i in range(len(max_path)-1):
        try:
            travel_path.append(short_street.index([max_path[i],max_path[i+1]]))
        except ValueError:
            travel_path.append(short_street.index([max_path[i+1],max_path[i]]))
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

def inSet(inte_sets, vertex):
    if (len(inte_sets) > 0):
        for x in inte_sets:
            for y in x:
                if y == vertex:
                    return True, inte_sets.index(x)
        return False, -1
    return False, -1


def findCycle(inte, edge, path, inte_sets):
    temp_path = path.copy()
    temp_path.append(edge)
    temp_path = makeList(inte, temp_path)
    if (not inSet(inte_sets, edge[0])[0] and not inSet(inte_sets, edge[1])[0]):
        inte_sets.append([edge[0],edge[1]])
    elif (inSet(inte_sets, edge[0])[0] and not inSet(inte_sets, edge[1])[0]):
        inte_sets[inSet(inte_sets, edge[0])[1]].append(edge[1])
    elif (not inSet(inte_sets, edge[0])[0] and  inSet(inte_sets, edge[1])[0]):
        inte_sets[inSet(inte_sets, edge[1])[1]].append(edge[0])    
    elif (inSet(inte_sets, edge[0])[0] and inSet(inte_sets, edge[1])[0] and inSet(inte_sets, edge[0])[1] != inSet(inte_sets, edge[1])[1]):
        setNum = inSet(inte_sets, edge[0])[1]
        for x in inte_sets[inSet(inte_sets, edge[0])[1]]:
            inte_sets[inSet(inte_sets, edge[1])[1]].append(x)
        inte_sets.pop(setNum)
    elif (inSet(inte_sets, edge[0])[0] and inSet(inte_sets, edge[1])[0] and inSet(inte_sets, edge[0])[1] == inSet(inte_sets, edge[1])[1]):
        return True
    
    
    return False


def optimalPath(inte, nodes, street_list):
    sorted_street = sortStreetWeight(street_list)
    mst_paths = []
    inte_sets = []
    for street in sorted_street:
        if (not findCycle(inte, street, mst_paths, inte_sets)):
            mst_paths.append(street)
    
    mst_nodes = makeList(inte, mst_paths)
    path = DFS(0,mst_nodes, inte)
    path.reverse()
    return path


street_list=[]
inte, strts = getInput(street_list)
nodes = makeList(inte,street_list)
blocked_paths = blockPaths(street_list, optimalPath(inte, nodes, street_list), inte)
blocked_paths.sort()
if len(blocked_paths) == 0:
    print("none")
else:
    print(*blocked_paths)

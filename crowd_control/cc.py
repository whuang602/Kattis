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
    sorted_street = street_list.copy()
    for index in range(len(sorted_street)):
        for index2 in range(0, len(sorted_street)-index-1):
            if sorted_street[index2][2] < sorted_street[index2+1][2]:
                sorted_street[index2], sorted_street[index2+1] = sorted_street[index2+1], sorted_street[index2]
    return sorted_street

def findMin(path, max, nodes):
    min = max
    to_visit = path.copy()
    while len(to_visit) > 1:
        for street in nodes[to_visit[0]]:
            if (street[0] == to_visit[1] and street[1] < min):
                min = street[1]
        to_visit.pop(0)
    return min

# def DFS(vertex, mst_nodes):
#     visited = []
#     DFSrecur(vertex, mst_nodes, visited)
#     return visited
    
# def DFSrecur(vertex, mst_nodes, visited):
#     try:
#         visited.append(vertex)
#         for child in mst_nodes[vertex]:
#             if child[0] not in visited:
#                 DFSrecur(child[0], mst_nodes, visited)
#     except TypeError:
#         visited.append(vertex)

def BFS(vertex, mst_nodes, inte):
    visited = []
    queue = []
    queue.append(vertex)
    visited.append(vertex)
    while len(queue) > 0:
        vertex = queue.pop(0)
        for i in mst_nodes[vertex]:
            if i[0] not in visited:
                queue.append(i[0])
                visited.append(i[0])
    
    return visited

def findMaxPath(paths,max,nodes):
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
    
    
    # print(inte_sets)
    return False


# fix (findCycle) and the rest of the code works 
def optimalPath(inte, max, nodes, street_list):
    sorted_street = sortStreetWeight(street_list)
    mst_paths = []
    inte_sets = []
    # print(sorted_street)
    for street in sorted_street:
        if (not findCycle(inte, street, mst_paths, inte_sets)):
            mst_paths.append(street)
    # print(mst_paths)
    
    # test cases
    # mst_paths = [[0,1,800],[1,2,300],[0,3,100],[3,4,80],[4,5,50],[4,6,100]]
    # mst_paths = [[1,2,50],[0,3,30],[1,3,20]]
    
    mst_nodes = makeList(inte, mst_paths)
    path = []
    # visited = DFS(inte-1,mst_nodes)
    visited = BFS(0, mst_nodes, inte)
    print(visited)
    index=0
    while path[-1] != inte-1:
        path.append(visited[index])
        for x in mst_nodes[visited[index]]:
            

    
    paths = [path]
    return paths


street_list=[]
inte, strts, max = getInput(street_list)
nodes = makeList(inte,street_list)
max_path = findMaxPath(optimalPath(inte, max, nodes, street_list), max, nodes)
blocked_paths = blockPaths(street_list, max_path, inte)
blocked_paths.sort()
if len(blocked_paths) == 0:
    print("none")
else:
    print(*blocked_paths)

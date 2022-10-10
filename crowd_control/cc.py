def getInput(street_list):
    inte, strts = [int(x) for x in input().split()]
    while (strts > 0):
        temp_input = [int(x) for x in input().split()]
        street_list.append(temp_input)
        strts -= 1
    return inte, strts

def dijkstra(inte, street_list):
    nodes = []
    adj_matrix = [] 
    
    for x in range(inte):
        nodes.append([])
        adj_matrix.append([0] * inte)

    for streets in street_list:
        nodes[streets[0]].append([streets[1],streets[2], False])
        nodes[streets[1]].append([streets[0],streets[2], False])
        adj_matrix[streets[0]][streets[1]] = 1
        adj_matrix[streets[1]][streets[0]] = 1

class Node:
    def __init__(self,value,children):
        self.value = value
        self.children = children
    
    
    

    

street_list=[]
blocked_paths=[]

inte, strts = getInput(street_list)
intersections = [None] * inte 
print(street_list)
dijkstra(inte,street_list)

# Extra functions that weren't used in the actual program
# def BFS(vertex, mst_nodes, inte):
#     visited = []
#     queue = []
#     queue.append(vertex)
#     visited.append(vertex)
#     while len(queue) > 0:
#         vertex = queue.pop(0)
#         for i in mst_nodes[vertex]:
#             if i[0] not in visited:
#                 queue.append(i[0])
#                 visited.append(i[0])
    
#     return visited

# def findMin(path, max, nodes):
#     min = max
#     to_visit = path.copy()
#     while len(to_visit) > 1:
#         for street in nodes[to_visit[0]]:
#             if (street[0] == to_visit[1] and street[1] < min):
#                 min = street[1]
#         to_visit.pop(0)
#     return min

# def findMaxPath(paths,max,nodes):
#     min = findMin(paths[0], max, nodes)
#     max_path = paths[0]
#     for path in paths:
#         path_min = findMin(path, max, nodes)
#         if (path_min > min):
#             min = path_min
#             max_path = path
#     return max_path
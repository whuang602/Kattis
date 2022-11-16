def getInput():
    room_list = []
    N, K = [int(x) for x in input().split()]
    for i in range(N+1):
        room_list.append([int(x) for x in input().split()]) 
    room_list.pop(-1)
    return N, K, room_list

N, K, room_list = getInput()
dp_table1 = [[[-1 for k in range(2)] for j in range(N)] for i in range(K+1)]
dp_table2 = [[[-1 for k in range(2)] for j in range(N)] for i in range(K+1)]
flipper = [1,0]

total = 0
for j in range(2):
    for i in range(N):
        if room_list[i][j] >= 0:
            total += room_list[i][j]

def closed_cost(K, dp_table, row, column):
    if K <= 0:
        return 0

    if row > N-1:
        return 40000
    
    if dp_table[K][row][column] < 0:
        block_curr_room = room_list[row][column] + closed_cost(K-1, dp_table, row+1, column)
        dp_table[K][row][column] = min(block_curr_room, closed_cost(K, dp_table, row+1, column), closed_cost(K, dp_table, row+1, flipper[column]))
    return dp_table[K][row][column]

print(total - min(closed_cost(K, dp_table1, 0,0),closed_cost(K, dp_table2, 0,1)))
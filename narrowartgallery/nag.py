import itertools

def getInput():
    room_list = []
    N, K = [int(x) for x in input().split()]
    for i in range(N+1):
        room_list.append([int(x) for x in input().split()]) 
    room_list.pop(-1)
    return N, K, room_list

def pathExist(room_list):
    
    flipper = [1,0]
    if room_list[0][0] >= 0:
        last_room = [0,0]
    elif room_list[0][1] >= 0:
        last_room = [0,1]
    else:
        return False

    for i in range(1, len(room_list)):
        if room_list[i][0] >= 0:
            if last_room[1] == 0:
                last_room = [i,0]
            elif (last_room[1] == 1 and room_list[last_room[0]][flipper[last_room[1]]] >= 0) or (last_room[1] == 1 and room_list[i][1] >= 0):
                last_room = [i,0]
            else:
                return False
        elif room_list[i][1] >= 0:
            if last_room[1] == 1 or room_list[last_room[0]][flipper[last_room[1]]] >= 0:
                last_room = [i,1]
            else:
                return False
        else:
            return False

    return True

def totalWorth(room_list, N):
    worth = 0
    for j in range(2):
        for i in range(N):
            if room_list[i][j] >= 0:
                worth += room_list[i][j]
    return worth


def main(N, K, room_list):
    single_list = []
    location_list = []

    for j in range(2):
        for i in range(N):
            single_list.append(room_list[i][j])
            location_list.append([i,j])
    
    cost_list = []
    for subset in itertools.combinations(location_list, K):
        temp_room = [row[:] for row in room_list]
        sum = 0
        for j in subset:
            sum += temp_room[j[0]][j[1]]
            temp_room[j[0]][j[1]] = -1
        if pathExist(temp_room):
            cost_list.append(sum)

    print(totalWorth(room_list, N) - min(cost_list))


N, K, room_list = getInput()

main(N, K, room_list)
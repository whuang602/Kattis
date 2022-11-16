import numpy

def getInput():
    room_list = []
    N, K = [int(x) for x in input().split()]
    for i in range(N+1):
        room_list.append([int(x) for x in input().split()]) 
    room_list.pop(-1)
    return N, K, room_list

def pathExist(room_list, coordinate=[], K=0):
    temp = room_list[coordinate[0]][coordinate[1]]
    room_list[coordinate[0]][coordinate[1]] = -1
    
    flipper = [1,0]
    if room_list[0][0] >= 0:
        last_room = [0,0]
    elif room_list[0][1] >= 0:
        last_room = [0,1]
    else:
        room_list[coordinate[0]][coordinate[1]] = temp
        return False, K
    # print(room_list[0][:])
    for i in range(1, len(room_list)):
        # print("last room:", room_list[last_room[0]][last_room[1]])
        # print(room_list[i][:])
        if room_list[i][0] >= 0:
            if last_room[1] == 0:
                last_room = [i,0]
            elif (last_room[1] == 1 and room_list[last_room[0]][flipper[last_room[1]]] >= 0) or (last_room[1] == 1 and room_list[i][1] >= 0):
                last_room = [i,0]
            else:
                room_list[coordinate[0]][coordinate[1]] = temp
                return False, K
        elif room_list[i][1] >= 0:
            if last_room[1] == 1 or room_list[last_room[0]][flipper[last_room[1]]] >= 0:
                last_room = [i,1]
            else:
                room_list[coordinate[0]][coordinate[1]] = temp
                return False, K
        else:
            room_list[coordinate[0]][coordinate[1]] = temp
            return False, K

    return True, K-1

# def sortlist(single_list, location_list):
#     for index in range(len(single_list)):
#         for index2 in range(0, len(single_list)-index-1):
#             if single_list[index2] > single_list[index2+1]:
#                 single_list[index2], single_list[index2+1] = single_list[index2+1], single_list[index2]
#                 location_list[index2], location_list[index2+1] = location_list[index2+1], location_list[index2]

# def sortWithin(single_list, location_list, room_list, N):
#     value = 0
#     list_value = []
#     list_range = []
#     temp_range = [0,0]
#     for i in range(len(single_list)):
#         if value > single_list[-1]:
#             break

#         if single_list[i] == value:
#             temp_range[1] += 1
#         else:
#             list_value.append(value)
#             list_range.append(temp_range)
#             temp_range = [i,1]
#             value += 1

#     for i in range(len(list_value)):
#         temp_values = single_list[list_range[i][0]:list_range[i][0] + list_range[i][1]]
#         temp_range = location_list[list_range[i][0]:list_range[i][0] + list_range[i][1]]
#         # print(temp_values)
#         # print("Before sort: ", temp_range)
#         for j in range(len(temp_values)):
#             sum = 0
#             if (temp_range[j][0] > 0):
#                 sum += room_list[temp_range[j][0]-1][temp_range[j][1]]
#             if (temp_range[j][0] < N-1):
#                 sum += room_list[temp_range[j][0]+1][temp_range[j][1]]
#             temp_values[j] = sum
#             # print(temp_values)
#         sortlist(temp_values, temp_range)
#         location_list[list_range[i][0]:list_range[i][0] + list_range[i][1]] = temp_range
#         # print("After sort: ", temp_range)

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

    ################################################################

    # sortlist(single_list, location_list)

    # sortWithin(single_list, location_list, room_list, N)

    # index = 0
    # while K > 0:
    #     print(location_list[index])
    #     X, K = pathExist(room_list, location_list[index], K)
    #     print("K=",K)
    #     print(room_list)
    #     index += 1

    # print(pathExist(room_list,[1,1]))
    # print(room_list)

    ###############################################################
    
    index = 0
    closed_list = []
    for i in range(K):
        for j in location_list:
            closed_list[]


    print(totalWorth(room_list, N) - closed_cost)


N, K, room_list = getInput()

# for i in range(3,201):
#     for j in range(0,i):
#         main(i,j,100*numpy.random.random((i, 2)))

main(N, K, room_list)
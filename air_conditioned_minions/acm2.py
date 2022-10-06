def getInput(minion_list):
    minion_count = int(input())
    while (minion_count > 0):
        temp_input = [int(x) for x in input().split()]
        minion_list.append(temp_input)
        minion_count -= 1

def isOverlap(a,b,c,d):
    if ( (a <= c and b >= c) or (a <= d and b >= d) or (c <= a and d >= a) or (c <= b and d >= b)):
        return True
    return False

def sortRangeList(minion_list):
    # bubble sort with respect to temperature end range
    for index in range(len(minion_list)):
        for index2 in range(0, len(minion_list)-index-1):
            if minion_list[index2][1] > minion_list[index2+1][1]:
                minion_list[index2], minion_list[index2+1] = minion_list[index2+1], minion_list[index2]
    
    # resort based on temperature start range
    for index in range(len(minion_list)):
        for index2 in range(len(minion_list)):
            if index==index2:
                continue
            if minion_list[index][1] == minion_list[index2][1]:
                if minion_list[index][0] < minion_list[index2][0]:
                    minion_list[index], minion_list[index2] = minion_list[index2], minion_list[index]

#initate variables         
minion_list = []
min_rooms = 0

# take input and store in minion_list
getInput(minion_list)

# sort minion_list from lowest end temp
sortRangeList(minion_list)

# end point of the first temperature range 
temp_minion = minion_list[0]
overlaps = [minion_list[0]]
index = 1

while len(minion_list) > 0:
    if (index==len(minion_list)):
        min_rooms+=1
        break
    if isOverlap(*temp_minion, *minion_list[index]):
        overlaps.append(minion_list[index])
    else:
        for minion in overlaps:
            minion_list.remove(minion)
            index -= 1
        min_rooms += 1
        overlaps = []
        temp_minion = minion_list[index]
    index+=1

# The below code can completely replace line 40-57 as it does the same thing
# however min_rooms will require an additional +1
# temp_minion = minion_list[0]

# for index in range(1, len(minion_list)):
#     if not isOverlap(*temp_minion,*minion_list[index]):
#         temp_minion = minion_list[index]
#         min_rooms += 1

print(min_rooms)

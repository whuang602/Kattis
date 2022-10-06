def isOverlap(a,b,c,d):
    if ( (a <= c and b >= c) or (a <= d and b >= d) or (c <= a and d >= a) or (c <= b and d >= b)):
        return True
    return False

def findMaxIndex(overlap_list):
    max = 0
    max_index = None
    for index in range(len(overlap_list)):
        if overlap_list[index][0] > max:
            max = overlap_list[index][0]
            max_index = index
    return max, max_index

def makeOverlapList(minion_list):
    overlap_list = []
    for index in range(len(minion_list)):
        overlap_list.append([0,minion_list[index]])
        for index2 in range(len(minion_list)):
            if (index==index2):
                continue
            if isOverlap(*minion_list[index],*minion_list[index2]):
                overlap_list[index][0]+=1
                overlap_list[index].append(minion_list[index2])
    return overlap_list


minion_count = int(input())
minion_list = []

while (minion_count > 0):
    temp_input = [int(x) for x in input().split()]
    minion_list.append(temp_input)
    minion_count -= 1


min_rooms=0
while len(minion_list) > 0:
    print(minion_list)

    overlap_list = makeOverlapList(minion_list)
    max, max_index = findMaxIndex(overlap_list)

    if max >= 1:
        for minion in range(1, len(overlap_list[max_index])):
            minion_list.remove(overlap_list[max_index][minion])
    else:
        minion_list.pop(0)
    print(minion_list)
    min_rooms += 1

print(min_rooms)

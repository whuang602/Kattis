def getInput():
    count, cost = [int(x) for x in input().split()]
    comm_list = [int(x) - cost for x in input().split()]
    return comm_list

comm_list = getInput()
temp_list = []
sum = 0
for i in comm_list:
    if sum + i < 0:
        temp_list.append(sum)
        sum = 0
        continue
    if sum + i < sum:
        temp_list.append(sum)
    sum += i
    if i == comm_list[-1]:
        temp_list.append(sum)

print(max(temp_list))
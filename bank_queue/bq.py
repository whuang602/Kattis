def getInput(bank_list):
    people, time = [int(x) for x in input().split()]
    while (people > 0):
        temp_input = [int(x) for x in input().split()]
        bank_list.append(temp_input)
        people -= 1
    return time

def sortBankListByTime(bank_list):
    for index in range(len(bank_list)):
        for index2 in range(0, len(bank_list)-index-1):
            if bank_list[index2][1] > bank_list[index2+1][1]:
                bank_list[index2], bank_list[index2+1] = bank_list[index2+1], bank_list[index2]

def countPerTime(bank_list, total_time):
    peoplePerTime = [0] * (total_time+1)
    for i in range(len(bank_list)):
        peoplePerTime[bank_list[i][1]]+=1
    return peoplePerTime

def maxAtTime(bank_list, time, isMax=True):
    temp_list = []
    for person in bank_list:
        if person[1] == time:
            temp_list.append(person[0])
    if isMax:
        value = 0
        for crowns in temp_list:
            if crowns > value:
                value = crowns
    else:
        value = 100000
        for crowns in temp_list:
            if crowns < value:
                value = crowns

    return value

def timePass(bank_list):
    for person in bank_list:
        person[1]-=1


bank_list = []
max_money = 0
time = getInput(bank_list)
sortBankListByTime(bank_list)
peoplePerTime = countPerTime(bank_list, time)
print(bank_list)
index=-1

while len(bank_list) > 0:
    index+=1
    if index == len(bank_list):
        
    if (peoplePerTime[index] > index):
        max = maxAtTime(bank_list,0)
        minCmp = maxAtTime(bank_list,index,False)
        if max > minCmp:
            max_money += max
    
    




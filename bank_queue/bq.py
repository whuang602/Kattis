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

def maxAtTime(bank_list, time, isMax=True):
    temp_list = []
    for person in bank_list:
        if person[1] == time:
            temp_list.append(person[0])
    max = 0
    for crowns in temp_list:
        if crowns > max:
                max = crowns
    return max

bank_list = []
max_money = 0
time = getInput(bank_list)
sortBankListByTime(bank_list)


while len(bank_list) > 0:
        time-=1
        if time < 0:
                bank_list = []
                continue
        if (bank_list[-1][1] != time):
                continue
        max_money += maxAtTime(bank_list, time)
        bank_list.remove([maxAtTime(bank_list, time),time])
        for crown in bank_list:
                if crown[1] == time:
                        crown[1] -= 1

print(max_money)
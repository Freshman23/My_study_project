from re import findall
from json import dump
total_firms_list = [{}, {}, {}]
total_profit = 0
count_profit = 0

with open('task_7_5.txt', 'r') as firm_file:
    for firm in firm_file:
        firm_list = findall(r'\S+', firm)
        if int(firm_list[2]) > int(firm_list[3]):
            total_firms_list[0][firm_list[0]] = int(firm_list[2]) - int(firm_list[3])
            total_profit += int(firm_list[2]) - int(firm_list[3])
            count_profit += 1
        else:
            total_firms_list[2][firm_list[0]] = int(firm_list[2]) - int(firm_list[3])
    total_firms_list[1]['Average profit'] = round(total_profit / count_profit)

with open('task_7_5.json', 'w') as json_file:
    dump(total_firms_list, json_file)

print(total_firms_list)

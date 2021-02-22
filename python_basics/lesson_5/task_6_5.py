subj_dict = {}


def sum_hours(hours_str):
    hours_list = []
    num = ''
    for char in hours_str:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                hours_list.append(int(num))
                num = ''
    if num != '':
        hours_list.append(int(num))
    return sum(hours_list)


with open('task_6_5.txt', 'r') as subj_file:
    for subject in subj_file:
        subj_dict[subject.split(':')[0]] = sum_hours(subject.split(':')[1])
print(subj_dict)

# С модулем re менее читабельно, но предельно лаконично:
# from re import findall
# subj_dict = {}
# with open('task_6_5.txt', 'r') as subj_file:
#     for subject in subj_file:
#         subj_dict[subject.split(':')[0]] = sum([int(num) for num in findall(r'\d+', subject.split(':')[1])])
# print(subj_dict)

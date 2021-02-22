with open('task_3_5.txt', 'r') as stf_salary:
    total_salary = 0
    print('Next employees have a salary less than 20000$:')
    for num, employee in enumerate(stf_salary):
        total_salary = total_salary + int(employee.split(' ')[1])
        if int(employee.split(' ')[1]) < 20000:
            print(employee.split(' ')[0])
    print(f'Average salary is {total_salary / (num + 1):.2f}$')

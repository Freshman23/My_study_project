from sys import argv


def total_salary_calc(*args):
    wage_rate, hours_amount, bonus = args
    wage_rate = int(wage_rate)
    hours_amount = int(hours_amount)
    bonus = int(bonus)
    print(f'При часовой ставке = {wage_rate}$/ч, часовой выработке = {hours_amount}ч и премии = {bonus}$:\n'
          f'Зарплата = {wage_rate * hours_amount + bonus}$')


total_salary_calc(*argv[1:])

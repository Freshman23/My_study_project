def sum_two_max(*args):
    return sorted(args, reverse=True)[0] + sorted(args, reverse=True)[1]


print(sum_two_max(14, 0, 14, 10, 10, 1))

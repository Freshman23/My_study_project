def sum_two_max(term_1, term_2, term_3):
    list = [term_1, term_2, term_3]
    max_1 = max(list)
    list.remove(max_1)
    max_2 = max(list)
    return max_1 + max_2

print(sum_two_max(10, 10, 10))

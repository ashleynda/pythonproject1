def total_list(num):
    total = 0
    new_list = []
    for sums in num:
        total += sums
        new_list.append(total)
    return new_list
    print(total_list())

numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# print(total_list(numbers))

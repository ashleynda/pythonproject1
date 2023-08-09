def total_list(num):
    total = 0
    for sums in num:
        total += sums
    return total


numbers = [100, 20, 2, 70, 23, 50, 9, 71, 33, 1]
print(total_list(numbers))
def even_positions(num):
    new_list = []
    for numb in range(0, len(num), 2):
        new_list.append(numbers[numb])
    return new_list


numbers = [100, 20, 2, 70, 23, 50, 9, 71, 33, 1]
print(even_positions(numbers))
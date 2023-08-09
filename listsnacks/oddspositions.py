def odd_positions(num):
    new_list = []
    for numb in range(1, len(num), 2):
        new_list.append(numbers[numb])
    return new_list


numbers = [100, 20, 2, 70, 23, 50, 9, 71, 33, 1]
print(odd_positions(numbers))

# numbers = [100, 20, 2, 70, 23, 50, 9, 71, 33, 1]
# for sum in numbers[1::2]:
#     print(numbers)
# print(numbers[1:10:2])

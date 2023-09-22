# def sum_list(list1, value) -> list:
#     for num in range(len(list1)):
#         for number in range(1, len(list1)):
#             if list1[num] + list1[number] == value:
#                 return [num, number]
#
#
# l1 = [5, 4, 9, 7, 2, 0]
# print(sum_list(l1, value=16))

def create_tuple(l1, l2) -> list:
    new_list = []
    list_l1_len = len(l1)
    list_l2_len = len(l2)
    if list_l1_len > list_l2_len:
        for index in range(len(l2)):
            new_list.append((l1[index], l2[index]))
        new_list.append((l1[-1],))
    else:
        for index in range(len(l1)):
            new_list.append((l1[index], l2[index]))
        new_list.append((l2[-1],))
    return new_list

    # return list(zip(l1, l2))


l1 = [1, 2, 3, 4, 5, 11]
l2 = [6, 7, 8, 9, 10]

if __name__ == '__main__':
    print(create_tuple(l1, l2))

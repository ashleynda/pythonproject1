import collections


# def return_tuple():
#     result = collections.Counter(list1) & collections.Counter(list2)
#     intersected_list = list(result.elements())
#     return intersected_list
#
#
# list1 = [20, 30, 60, 65, 75, 80, 85]
# list2 = [42, 30, 80, 65, 68, 88, 95]
# print(return_tuple())


def return_tuple():
    intersected_list = []
    for ele in list1:
        if ele in list2:
            intersected_list.append(ele)
    return intersected_list


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
print(return_tuple())

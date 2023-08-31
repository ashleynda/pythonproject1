import collections


def number():
    # number = int(input('Enter numbers:  '))
    result = collections.Counter(number)
    nun_list = list(result.elements())
    return nun_list
    # num_list = []
    # for num in list:
    #     num_list.append(number)
    # return num_list


num = int(input('Enter numbers:  '))
print(number())

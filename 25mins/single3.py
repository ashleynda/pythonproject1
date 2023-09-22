def single_three(list):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
        return new_list[0]
lst = [1]
print(single_three(list))
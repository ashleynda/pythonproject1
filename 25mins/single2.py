def single_one(list):
    new_list = []
    for ele in lst:
        if ele not in new_list:
            new_list.append(ele)
        return new_list[0]


lst = [4, 3, 2, 2, 3, 3]
print(single_one(list))

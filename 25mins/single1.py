def return_one(list):
    new_list = []

    for element in num[::-1]:
        if element not in new_list:
            new_list.append(element)
        return new_list[0]

num = [2, 2, 1]
print(return_one(list))



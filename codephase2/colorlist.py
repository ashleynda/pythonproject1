def color_list():
    new_list = []
    for i in color_list_1:
        for j in color_list_2:
            if i == j:
                new_list.append(i)
    return new_list



color_list_1 = ['White', 'Black', 'Red']
color_list_2 = ['Red', 'Black']

print(color_list())

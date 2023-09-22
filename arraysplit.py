def split(lst: list) -> list:
    list1 = []
    list2 = []
    list3 = []

    for elements in range(0, len(lst),3):
        list1.append(lst[elements])
    for elements in range(1, len(lst),3):
        list2.append(lst[elements])
    for elements in range(2, len(lst),3):
        list3.append(lst[elements])
    return [list1,list2,list3]


arrays = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split(arrays))

def highest_odd_number(list1):
    odd_number = [i for i in list1 if i % 2 != 0]
    highest = odd_number[0]
    for higher in odd_number:
        if higher > highest:
            highest = higher
    return highest


print(highest_odd_number([19, 24, 33, 4, 50, 66]))

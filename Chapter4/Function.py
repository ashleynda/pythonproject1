# def square(number):
#     return number ** 2
#
#
# # square(7)
# print('The square of 7 is  ', square(7))
# print('The square of 2.5 is  ', square(2.5))


def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value
    print(f'The maximum value is {maximum}')


print(maximum(12, 27, 36))
print(maximum(12.3, 45.6, 9.7))
print(maximum('yellow', 'red', 'orange'))
print(maximum(13.5, -3, 7))
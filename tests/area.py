import math


# def area_of_a_circle(r):
#     area = math.pi * (r * r)
#     return area
#
#
# area_of_a_circle(4)


def area_of_a_circle(r):
    if r < 0:
        raise ValueError('Value Error')
    if type(r) is not int and type(r) is not float:
        raise TypeError('Invalid Type')
    return math.pi * (r * r)



area_of_a_circle(2)

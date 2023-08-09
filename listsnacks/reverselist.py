numbers = [100, 20, 2, 70, 23, 50, 9, 71, 33, 1]


def rev(num):
    r = []
    for ace in num:
        r.insert(0, ace)
    return r


print(rev([100, 20, 2, 70, 23, 50, 9, 71, 33, 1]))

# print(numbers[::-1])
# def reverse_list(num):
#     for ace in range[-1:-10:-1]:
#         for aced in range[::1]:
#             if num[aced] > num[ace]:
#                 num[aced], num[ace] = num[ace], num[aced]
#     return num
#
#
# print(reverse_list(numbers))

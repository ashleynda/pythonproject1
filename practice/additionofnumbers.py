# numbers = [10, 20, 30, 40, 50]
# total = 0
# for sums in numbers:
#     total = total + sums
# print(total)
#
# add = 0
# numbers = [10, 20, 30, 40, 50]
# for sum in numbers[0::2]:
#     add = add + sum
# print(add)
#
# two = 0
# numbers = [10, 20, 30, 40, 50]
# for sum in numbers[1::2]:
#     two = two + sum
# print(two)
#
# numbers = [10, 20, 30, 40, 50]
# for item in range(len(numbers)):
#     numbers[item] **= 2
# print(numbers)
#
#
# def largest(square1, square2, square3, square4, square5):
#     maximum = square1
#     if square2 > maximum:
#         maximum = square2
#     if square3 > maximum:
#         maximum = square3
#     if square4 > maximum:
#         maximum = square4
#     if square5 > maximum:
#         maximum = square5
#     return maximum
#     print(f'The smallest number is {maximum}')
#
#
# def smallest(square1, square2, square3, square4, square5):
#     minimum = square1
#     if square2 < square1:
#         minimum = square2
#     if square3 < square2:
#         minimum = square3
#     if square4 < square3:
#         minimum = square4
#     if square5 < square4:
#         minimum = square5
#     return minimum
#     print(f'The smallest number is {minimum}')
#
#
# print(largest(100, 400, 900, 1600, 2500))
# print(smallest(100, 400, 900, 1600, 2500))

numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]


# def sorted_list(list):
#     for ace in range(len(list)):
#         for aced in range(len(list)):
#             if list[aced] > list[ace]:
#                 list[aced], list[ace] = list[ace], list[aced]
#     return list
#
#
# print(sorted_list(numbers))

numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
print(numbers[::-1])
# def reverse_sorted_list(list):
#     for ace in range[-1:-10:-1]:
#         for aced in range[::1]:
#             if list[aced] > list[ace]:
#                 list[aced], list[ace] = list[ace], list[aced]
#     return list
#
#
# print(reverse_sorted_list(numbers))

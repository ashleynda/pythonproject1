# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def even(n):
#     return n % 2 == 0
#
#
# result = [i for i in list1 if i % 2 == 0]
# print(result)
#
# result = [y ** 2 for y in list1]
# print(result)


def palindrome(s):
    return s == s[::-1]


s = "kayak"
result = palindrome(s)
if result:
    print("Yes")
else:
    print("No")


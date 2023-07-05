# def main():
#     sum1(10)
#     sum1(10)
#     sum1(10)
# def collect():
#     num = int(input("Enter number:  "))
#     return num
#
#
# def sum1(n):
#     total = 0
#     for counter in range(1, collect() + 1):
#             total += counter
#     print(total)
#
# def sum2():
#         total = 0
#         for counter3 in range(1, 11):
#                 total += counter3
#         print(total)
#
# def greater(number1, number2):
#         maximum = number1
#         if number2 > number1:
#                 maximum = number2
#         print(maximum)
#
# main()
# greater(5, 2)

def greater(number1, number2, number3, number4):
    maximum = number1
    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    if number4 > maximum:
        maximum = number4
    return maximum
    #print(f'The greater number is {maximum}')


def small(number1, number2, number3):
    minimum = number1
    if number2 < number1:
        minimum = number2
    if number3 < number2:
        minimum = number3
    return minimum
   # print(f'The smallest number is {minimum}')


print(greater(250, 10, 102, 110))
print(small(20, 4, 8))

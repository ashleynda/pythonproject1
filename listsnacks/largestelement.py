def largest(numbers):
    maximum = numbers[0]
    if numbers[1] > maximum:
        maximum = [1]
    if numbers[2] > maximum:
        maximum = [2]
    if numbers[3] > maximum:
        maximum = [3]
    if numbers[4] > maximum:
        maximum = [4]
    if numbers[5] > maximum:
        maximum = [5]
    if numbers[6] > maximum:
        maximum = [6]
    if numbers[7] > maximum:
        maximum = [7]
    if numbers[8] > maximum:
        maximum = [8]
    if numbers[9] > maximum:
        maximum = [9]
    return maximum
    print(f'The largest number is {maximum}')


print(largest([100, 20, 2, 70, 23, 50, 9, 71, 33, 1]))



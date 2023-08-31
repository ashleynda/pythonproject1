def fibonacci(num):
    num1 = 0
    num2 = 1
    print(f'{num1}\t{num2}', end='\t')
    number = 0
    while number <= num:
        number = num1 + num2
        if number > num: break
        num1 = num2
        num2 = number
        print(number, end='\t')


fibonacci(50)

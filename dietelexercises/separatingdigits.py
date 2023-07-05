num1 = int(input('Enter number:  '))

for num1 in range(1, 6):
    number1 = num1 % 10
    number2 = (num1 // 10) %10
    number3 = (num1 // 100) %10
    number4 = (num1 // 1000) % 10
    number5 = (num1 // 10000) % 10
    print(number5,number4,number3,number2,number1)


num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number:  "))
num3 = int(input("Enter third number:  "))
num4 = int(input("Enter fourth number:  "))

for i in range(1, 4):
    print('The sum is', num1 + num2 + num3 + num4)
    print('The average is', num1 + num2 + num3 + num4 / 4)
    print('The product is', num1 * num2 * num3 * num4)
    break



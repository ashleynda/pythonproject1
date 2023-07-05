number1 = int(input( "Enter the value : "))
number3 = int(input( "Enter the value : "))
number4 = int(input( "Enter the value : "))
number2 = int(input( "Enter the value : "))
number5 = int(input( "Enter the value : "))
number6 = int(input( "Enter the value : "))


Square1 = number1 * number1
Cube1 = number1 * Square1
Square2 = number2 * number2
Cube2 = number2 * Square2
Square3 = number3 * number3
Cube3 = number3 * Square3
Square4 = number4 * number4
Cube4 = number4 * Square4
Square5 = number5 * number5
Cube5 = number5 * Square5
Square6 = number6 * number6
Cube6 = number6 * Square6


for square in range(0, 5):
    for cube in range(0, 125):
        print(f'Number\t Square\t Cube')
        print(f'\t{number1}\t\t {number1 * number1}\t\t {Cube1}')
        print(f'\t{number2}\t\t {number2 * number2}\t\t {Cube2}')
        print(f'\t{number3}\t\t {number3 * number3}\t\t {Cube3}')
        print(f'\t{number4}\t\t {number4 * number4}\t\t {Cube4}')
        print(f'\t{number5}\t\t {number5 * number5}\t\t {Cube5}')
        print(f'\t{number6}\t\t {number6 * number6}\t\t {Cube6}')
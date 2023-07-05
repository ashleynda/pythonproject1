multiples = 1

while multiples < 2000:
    multiples *= 2

print("The result is:", multiples)

num = int(input('Enter your password:  '))
size = len(num)

if size < 8:
    print('Enter password again:  ')
if size >= 8:
    print('correct password')



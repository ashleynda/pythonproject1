password = input("Enter your password:  ")


while len(password) < 8:
    password = input("Enter your password:  ")
if len(password) >= 8:
    print(f'Your password is secure, the length is {len(password)}')
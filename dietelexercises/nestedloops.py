for row in range(1, 9):
    for column in range(row+1):
        print('*', end=" ")
    print()

for row in range(1, 9):
    for column in range(1-row):
        print('*', end="")
    print()


n = int(input("Enter the number of rows:  "))
for row in range(0, 9):
    for column in range(row+1):
        print("#", end=" ")
    print()

for row in range(0, 9):
    for column in range(n-row):
        print("#", end=" ")
    print()

for row in range(0, 9):
    for column in range(n-row):
        print("#", end=" ")
    print()

for row in range(0, 9):
    for column in range(row+1):
        print("#", end=" ")
    print()

   # for symbol in range(1, row+1):
    #    print("# ", end="")

     #   print()

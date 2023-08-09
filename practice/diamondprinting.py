# for i in range(5):
#     for j in range(5 -i - 1):
#         print(" ", end="")
#         for k in range(2 * i + 1):
#             print("*")
#         print()


for row in range(5):
    for column in range(5-row+1):
        print(" ", end=" ")
    for k in range(2*row+1):
        print("*")
        print()

for row in range(9):
    for column in range(1-row):
        print("*", end=" ")
    print()

# for row in range(1, 20):
#     for column in range(n-row):
#         print("*", end=" ")
#     print()

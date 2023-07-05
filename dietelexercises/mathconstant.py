from math import acos

def printValueOfPi():
    pi = round(2 * acos(0.0), 3)
    print(pi)

if __name__ == "_main_":
    printValueOfPi()
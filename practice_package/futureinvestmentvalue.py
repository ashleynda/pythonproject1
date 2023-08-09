import math

investmentAmount = float(input('Enter investment amount:  '))
annualInterestRate = float(input('Enter annual interest rate in percentage:  '))
numberOfYears = int(input('Enter number of years:  '))

# print(annualInterestRate/1200)
print('The future investment value is %d:  ', investmentAmount * math.pow(1 + annualInterestRate/1200, numberOfYears*12))
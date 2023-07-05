yearsCounter = 0
counter = 1

while yearsCounter <= 30:
    if yearsCounter <= 30:
        p = int(input("Enter original amount invested in $:  "))
        r = int(input("Enter annual rate of return:  "))
        n = int(input("Enter the number of years:  "))

        print('Amount after years:', p*(1+r/100)**yearsCounter)
        yearsCounter += 1

    #print('Amount after 20 years:', 1000*(1+7/100)**20)
    #print('Amount after 30 years:', 1000*(1+7/100)**30)


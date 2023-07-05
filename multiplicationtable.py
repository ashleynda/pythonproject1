def ashley_ndabai(end):
    for x in range(1, 13):
        for num in range(1, end+1):
            product = num * x
            print('%i X %i = %-5i'% (num,x,product),end='\t\t')
        print('\n')

ashley_ndabai(20)
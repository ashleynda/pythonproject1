total_gallons_used = 1
total_miles_driven = 1
total = 0

#gallons_used = float(input("Enter gallons used or -1 to terminate:  "))
#miles_driven = int(input("Enter miles driven or -1 to terminate:  "))

while gallons_used != -1 and miles_driven != -1:
    total = total_gallons_used / total_miles_driven
    gallons_used = float(input("Enter gallons used or -1 to terminate:  "))
    miles_driven = int(input("Enter miles driven:  "))

    print("The overall average miles/gallon was:  ", {total})


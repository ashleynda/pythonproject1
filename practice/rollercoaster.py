age = 0
height_of_person = float(input("Enter height:  "))
if height_of_person < 6:
    print("Too short, come back when you are taller")
elif height_of_person > 6:
    age = int(input("Please put in your age:  "))
    if age < 12:
        print("Pay 100")
    elif 12 > age <= 65:
        print("pay 200")
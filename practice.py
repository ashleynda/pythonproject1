name1 = 'Esther'
print(id(name1))
name2 = name1
print(id(name2))
name3 = name1 == name2
print(id(name3))

print("welcome to python c17")

first_name = str(input("Enter first name:  "))
if first_name is None or first_name == "":
    print("first_name cannot be empty")

last_name = str(input("Enter last name:  "))
if last_name is None or last_name == "":
    print("last name cannot be empty")
age = int(input("Enter your age:  "))

if age < 0:
    print("Your age cannot be zero or less")
elif age < 18:
    print(f"Your name is {first_name} {last_name} and your age is {age}, you are underage")
elif age > 18 and age < 65:
    print(f"Your name is {first_name} {last_name} and your age is {age}, you are a youth")
else:
    print(f"Your name is {first_name} {last_name} and your age is {age}, you are an old citizen")


my_name = "Asa"
my_name = my_name + ' ' + 'Sikiru'
print(id(my_name))
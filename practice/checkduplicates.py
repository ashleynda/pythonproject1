def check_duplicates(list):
    new_list = []
    for i in fruits:
        if i not in new_list:
            new_list.append(i)
        else:
            return "No duplicates"


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates([list]))

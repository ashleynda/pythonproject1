print(" ******************************************************")
print("        Aso Rock Secondary School, Abuja Nigeria")
print(" ******************************************************")

class_name = 'SSS 3'
Number_of_Student_in_class = 20
total_score = 0

for counter in range(Number_of_Student_in_class):
        score = float(input(f'Enter students scores #{counter}:  '))
        total_score += score

average_score = total_score / Number_of_Student_in_class


print(f"class: {class_name}")
print(f"Number_of_Student_in_class: 20")
print(f"Total Score:  {total_score}")
print("Average Score:  {:.2f}".format(average_score))
print("********************************************************")
        
        
        



print("*****************************************************" )
print("       Aso Rock Secondary School, Abuja Nigeria" )
print("*****************************************************" )

class_name = 'SSS 3'
Number_of_students_in_class = 1
total_score = 0
score = int(input(f'Enter students scores or -25 to terminate:  '))
while score != -25:
    total_score += score
    score = int(input(f'Enter students scores or -25 to terminate:  '))
    Number_of_students_in_class += 1
average = total_score / Number_of_students_in_class

print(f"class: SSS 3" )

print(f"Number_of_student_in_class:  {Number_of_students_in_class}" )

print(f"Total score:  {total_score}" )

print(f'Average Score: ', average)

print("*****************************************************" )




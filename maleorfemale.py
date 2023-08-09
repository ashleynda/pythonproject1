# def gender(male, female):
#     count = 0
#     for number in male:
#         gender.count(male)
#         count += 1
#     # for female in gender:
#     #     gender.count(female)
#     # return gender

def male_and_female(students):
    count_of_male = gender.count('male')
    count_of_female = gender.count('female')

    result = [('Male', count_of_male), ('female', count_of_female)]
    return result


gender = ['male', 'female', 'female', 'male', 'male', 'male', 'female', 'male',
          'female', 'male', 'female', 'male', 'female']
print(male_and_female(gender))








# def main():
#     students = int(input('How many students do you have?  '))
#     subject = int(input('How many subjects do they offer?  '))
#     print('Saving >>>>>>>>>>>>>>>>>>>>>>')
#     print('Saved successfully')
#
#     score = []
#     for _ in range(students):
#         print(f'Entering score for student {_ + 1}')
#         students_score = []
#         for _ in range(subject):
#             scores = int(input(f'Enter score for subject {_ + 1}: '))
#             students_score.append(scores)
#         score.append(students_score)
#
#     display_table(score, subject)
#     subject_summary(score)
#
#
# def display_table(score, subject):
#     print('=================================================================================================')
#     print("STUDENT\t\t", end="")
#
#     for sub in range(1, subject + 1):
#         print(f"SUB\t\t", end="")
#
#     print("TOT\t\tAVE\t\tPOS")
#     print('=================================================================================================')
#
#     sorted_scores = sorted([(sum(student), i) for i, student in enumerate(score)], reverse=True)
#     sorted_positions = {student[1]: pos for pos, student in enumerate(sorted_scores, start=1)}
#
#     for i in range(len(score)):
#         total = sum(score[i])
#         average = total / subject
#         pos = sorted_positions[i]
#
#         print(f"Student {i + 1}", end="\t")
#         for score in score[i]:
#             print(f"{score}\t\t", end="")
#         print(f"{total}\t\t{average:.2f}\t\t{pos}")
#     print('==================================================================================================')
#
#
# def subject_summary(score):
#     print('SUBJECT SUMMARY')
#
#     for sub in range(len(score[0])):
#         highest = -1
#         lowest = 101
#         total = 0
#         passes = 0
#         failures = 0
#         highest_student = -1
#         lowest_student = -1
#
#         for sco in range(len(score)):
#             scores = score[sco][sub]
#             total += score
#
#             if scores >= 50:
#                 passes += 1
#             else:
#                 failures += 1
#
#             if scores > highest:
#                 highest = scores
#                 highest_student = sco
#             if scores < lowest:
#                 lowest = scores
#                 lowest_student = sco
#
#         average = total / len(score)
#         print(f'Subject {sub + 1}')
#         print(f'Highest scoring student is: Student {highest_student + 1} scoring {highest}')
#         print(f'Lowest scoring student is: Student {lowest_student + 1} scoring {lowest}')
#         print(f'Total Score is: {total}')
#         print(f'Average Score is: {average}2f')
#         print(f'Number of Passes: {passes}')
#         print(f'Number of Fails: {failures}')
#
#
# if __name__ == "__main__":
#     main()
#
# # student_input()
# # display_table(score, subject)
# # subject_summary(score)

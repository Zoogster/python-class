lab1_score = float(input('Enter score for lab 1: '))
lab2_score = float(input('Enter score for lab 2: '))
lab3_score = float(input('Enter score for lab 3: '))
test1_score = float(input('Enter score for test 1: '))
test2_score = float(input('Enter score for test 2: '))
lab_average = (lab1_score + lab2_score + lab3_score) / 3
test_average = (test1_score + test2_score) / 2
course_grade = (lab_average * 0.55) + (test_average * 0.45)
output_string = 'Lab average is : ' + str(lab_average) + '\n' + 'Test average is: ' + str(
    test_average) + '\n' + 'Course grade is: ' + str(course_grade)
print(output_string)

# This would be another option for the output:
#
# print('Lab average is: ', lab_average)
# print('Test average is: ', test_average)
# print('Course grade is: ', course_grade)
#
# In fact this option is what I came up with first but I was looking over lession 2 again and
# I was reminded of escape characters. Is there a reason to pick ether of them over the other?
# They return nearly the same thing with the only difference as far as I can tell is this one
# technically has 3 different outputs instead of one that is outputted on 3 different lines.

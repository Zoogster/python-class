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

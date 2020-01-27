def main():
    lab_scores = []
    test_scores = []

    num_of_labs = int(input("How many labs? "))
    for lab_score in range(num_of_labs):
        lab_score = float(input("Enter lab score: "))
        lab_scores.append(lab_score)
    print('Lab scores: ', lab_scores)

    num_of_tests = int(input("how many labs? "))
    for test_score in range(num_of_tests):
        test_score = float(input("Enter a test score: "))
        test_scores.append(test_score)
    print('Test scores: ', test_scores)

    print('The Default wights of the course grade are 50% labs and 50% tests.')
    default_question = input(
        'Enter C to change the weights or D to use defualt weights: ')
    default_question = default_question.upper()
    if default_question == 'D':
        grade_calculator(lab_scores, test_scores)
    else:
        lab_wight = float(
            input('Enter lab percentage (without the % sign): '))
        test_wight = float(
            input('Enter test percentage (without the % sign): '))
        grade_calculator(lab_scores, test_scores, lab_wight, test_wight)


def grade_calculator(lab_scores, test_scores, lab_wight=50, test_wight=50):
    lab_average = 0
    for x in range(len(lab_scores)):
        lab_average = lab_average + lab_scores[x]
    lab_average = lab_average/len(lab_scores)
    print(f'Lab average: {lab_average: .2f}')

    test_average = 0
    for x in range(len(test_scores)):
        test_average = test_average + test_scores[x]
    test_average = test_average/len(test_scores)
    print(f'Test average: {test_average: .2f}',)

    course_grade = (lab_average * (lab_wight / 100)) + \
        (test_average * (test_wight / 100))
    print(f'Course grade: {course_grade: .2f} ')


main()

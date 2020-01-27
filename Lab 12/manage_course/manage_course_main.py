from course import Course


def main():
    course_code = input('Enter course code: ')
    max_size = int(input('Enter maximum class size: '))
    course1 = Course(course_code, max_size)
    choice = -1

    while choice != 0:
        choice = int(
            input('Enter 1 for add student, 2 for drop student, 3 for crouse info, 0 for exit: '))
        if choice == 1:
            course1.add_student()
        elif choice == 2:
            course1.drop_student()
        elif choice == 3:
            print('Course code: ', course_code)
            print('Maximum class size: ', max_size)
            print('Enrollment: ', course1.enrollment)


main()

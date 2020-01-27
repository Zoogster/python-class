from course2 import Course
from student import Student


def main():

    course_list = []
    student_list = []
    admin_list = []

    init_lists(course_list, student_list)
    print(course_list[1])
    print(student_list)
    print(student_list[0].get_id())
    testing = course_list[0].__dict__.keys()
    print(testing)
    print()
    course_list[0].display_roster()
    while True:
        login_type = int(input(
            'Enter 1 if you are student, 2 if you are administrator, 0 to quit: '))
        if login_type == 1:
            u_list = student_list
            break
        elif login_type == 2:
            u_list = admin_list
            break
        elif login_type == 0:
            return
    log_in_good = login(u_list)
    if log_in_good == 'student':
        student_session(course_list, student_list)


def init_lists(c_list, s_list):

    # ------------------------------------------------------------
    # This function adds elements to course_list, student_list and
    # admin_list.  It makes testing and grading easier.  It has
    # three paramters: c_list is the list of Course objects;
    # s_list is the list of Student objects; a_list is the list of
    # Admin objects.  This function has no return value.
    # -------------------------------------------------------------

    course1 = Course("CSC121", 2)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC122", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC221", 1)
    course3.add_student("1002")
    c_list.append(course3)
    course1_code = course1.get_course_code()
    print(course1_code)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)


def login(u_list):

    # ------------------------------------------------------------
    # This function allows a student or administrator to log in.
    # It has one parameter: u_list, which is a list of User objects
    # (Student objects and Admin objects are User objects). This
    # function asks user to enter ID and PIN. If they match the data
    # of an element  in u_list, display message of verification and
    # return the index of that element (e.g. return 0 if it is the
    # first element of the list, 1 if it is the second element, and
    # so on).  Otherwise, it displays error message and returns -1.
    # -------------------------------------------------------------
    print(u_list)
    id = input('Enter ID')
    pin = input('Enter pin')

    if (id, pin) in u_list:
        return 'student'

    else:
        print('Error: Wrong ID or pin')
        return -1


def student_session(c_list, s_list):
    pass

    # ------------------------------------------------------------
    # This function creates a student session.  It has two
    # parameters: c_list is the list of Course objects; s_list is
    # the list of Student objects.  It calls the login function
    # for the student user to log in.  If login is successful, it uses
    # a loop to allow the user to add, drop and list courses until
    # the user wants to exit. It call methods of the Student object
    # to handle the tasks.  This function has no return value.
    # -------------------------------------------------------------


def admin_session(c_list, a_list):
    pass

    # ------------------------------------------------------------
    # This function creates an administrator session.  It has two
    # parameters: c_list is the list of Course objects; a_list is
    # the list of Admin objects.  It calls the login function for
    # the administrator user to log in.  If login is successful, it
    # uses a loop to allow the user to show class roster and change
    # max class size. It calls methods of the Admin object to handle
    # the tasks.  This function has no return value.
    # -------------------------------------------------------------


main()

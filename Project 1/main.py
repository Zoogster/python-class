import admin
import student

"""Allow a student to enroll/drop a course and an admin to change max size of class

Author: Matthew VanPelt
Date: 10/18/2019

main -- Allows a student or admin to login then asks what they want to do and calls the functions 
in the other modules to depending on what the user is trying to do.
login -- Allows a a student or admin to log in by verifying ID and PIN. Returns verification and ID
student_session -- Calls functions from student module allowing the student to enroll/drop a course or view
course they are registered for
admin_session -- Calls functions from admin module allowing an admin to change max class size and view roster
"""


def main():
    """Makes starting lists and calls a function depending on user choice.

    Asks user if they are a student or admin and points them to student_session or
    admin_session depending on what they pick.
    Passes along relevant lists/tuples.
    """
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    admin_list = [('7001', '777'), ('8001', '888')]
    max_size_list = [2, 2, 1]
    roster_list = [['1004', '1003'], ['1001'], ['1002']]

    while True:
        login_type = int(input(
            'Enter 1 if you are a student, 2 if you are an administrator, 0 to quit: '))
        if login_type >= 0 and login_type <= 2:
            break
        else:
            print('Invalid Choice')

    if login_type == 0:
        return
    elif login_type == 1:
        student_session(roster_list, max_size_list, student_list)
    else:
        admin_session(roster_list, max_size_list, student_list, admin_list)


def login(id_list):
    """Allows a a student or admin to log in

    Allows a user to enter an ID and PIN to log in.
    If they are a valid match return verified and ID.
    """

    while True:
        id = input('Enter ID: ')
        pin = input("Enter PIN: ")
        id_pin_combo = (id, pin)

        if id_pin_combo in id_list:
            print('Verified')
            verified = 'Yes'
            return verified, id
        else:
            print('ID or PIN incorrect')


def student_session(r_list, m_list, s_list):
    """Calls functions from student module allowing the student to enroll/drop a course or view currently registered for courses"""
    verified, id = login(s_list)

    if verified == 'Yes':
        while True:
            student_activity = int(input(
                'Enter 1 to add a course, 2 to drop a course, 3 to see what courses you have registered for, or 0 to exit: '))

            if student_activity == 1:
                student.add_course(id, r_list, m_list)
            elif student_activity == 2:
                student.drop_course(id, r_list)
            elif student_activity == 3:
                student.list_courses(id, r_list)
            else:
                print('Student session ended')
                return


def admin_session(r_list, m_list, s_list, a_list):
    """Calls functions from admin module allowing an admin to change max class size and look at roster"""
    verified = login(a_list)

    if verified == 'Yes':
        while True:
            admin_activity = int(
                input('Enter 1 to show class roster, 2 to change max class size or 0 to exit: '))
            if admin_activity == 1:
                admin.show_roster(r_list)
            elif admin_activity == 2:
                admin.change_max_size(r_list, m_list)
            else:
                print('Admin session ended')
                return


main()

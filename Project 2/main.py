from course import Course
from student import Student
from admin import Admin

"""Main module of program.

main() -- Main function.
init_lists -- Sets up all the objects.
login -- Checks inputed ID and pin against student or admin list(depending on what was passed to it).
student_session -- Allows a student to add or drop course and see what they are registered for.
admin_session -- Allows admin to view roster and change max class size.
"""


def main():
    """Main function.

    Makes empty course, student and admin lists. Triggers int_lists. Asks
    user if they are a student admin or wish to quit. If student opens student session.
    If admin opens admin session. If they couse quit the program stops. Returns nothing.
    """
    course_list = []
    student_list = []
    admin_list = []

    init_lists(course_list, student_list, admin_list)
    while True:
        login_type = int(input(
            'Enter 1 if you are student, 2 if you are administrator, 0 to quit: '))
        if login_type == 1:
            student_session(course_list, student_list)
            return
        elif login_type == 2:
            admin_session(course_list, admin_list)
            return
        elif login_type == 0:
            return


def init_lists(c_list, s_list, a_list):
    """Sets up all the objects.

    Makes course objects and puts students in them. Then adds the course to the course list.
    Makes student objects and adds them to the list of students.
    Makes admin objects and adds them to the list of admins
    """

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

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("7001", "777")
    a_list.append(admin1)
    admin2 = Admin("8001", "888")
    a_list.append(admin2)


def login(u_list):
    """Checks inputed ID and pin against student or admin list

    Asks for ID and PIN. Uses loop to see if the ID matchs one of the ID/PIN stored. If it does notes what one.
    If there wasn't a match sets it to False. If its a correct ID the PIN is checked to see if it is the right PIN.
    If ether ID or PIN is False gives error and returns -1. Otherwise returns ID/PIN location.
    """

    id = input('Enter ID: ')
    pin = input('Enter PIN: ')
    for i in range(len(u_list)):
        if u_list[i].get_id() == id:
            id_yes = u_list[i]
            id_pin_location = i
            break
        else:
            id_yes = False
    if id_yes != False:
        if u_list[id_pin_location].get_pin() == pin:
            pin_yes = True
        else:
            pin_yes = False

    if pin_yes == False or id_yes == False:
        print('Error: Wrong ID or PIN')
        return -1
    return id_pin_location


def student_session(c_list, s_list):
    """Allows a student to add or drop course and see what they are registered for.

    Calls login and passes student list to it. If login in fails returns. If info is correct asks what they want to do.
    If they pick add course calls add_course. If they pick drop course calls drop_course. If they choose to see what
    they are registered for calls list_courses. If they wish to exit returns nothing to break loop.
    """
    id_location = login(s_list)
    if id_location == -1:
        return
    else:
        while True:
            what_to_do = int(input(
                'Enter 1 to add course, 2 to drop course, 3 to see courses you have registered for, 0 to exit: '))
            if what_to_do == 1:
                s_list[id_location].add_course(c_list)
            elif what_to_do == 2:
                s_list[id_location].drop_course(c_list)
            elif what_to_do == 3:
                s_list[id_location].list_courses(c_list)
            else:
                return


def admin_session(c_list, a_list):
    """Allows admin to view roster and change max class size.

    Calls login and passes admin list to it. If login in fails returns. If info is correct asks what they want to do.
    Lets them pick between showing class roster, changing max class size, or exiting. If they pick showing class roster
    calls show_roster. If they pick change max class size calls change_max_size. If they pick exit returns nothing.
    """
    id_location = login(a_list)
    if id_location == -1:
        return
    else:
        while True:
            what_to_do = int(
                input('Enter 1 to show class roster, 2 to change max class size, 0 to exit: '))
            if what_to_do == 1:
                a_list[id_location].show_roster(c_list)
            elif what_to_do == 2:
                a_list[id_location].change_max_size(c_list)
            else:
                return


main()

"""Lets an admin look at the roster and change max class size

show_roster -- Displays roster of a course.
change_max_size -- Allows admin to change max class size
"""


def show_roster(r_list):
    """Displays the roster for a chosen course

    Checks to make sure the course entered is valid.
    If valid desplays student IDs enrolled in that course sorted
    """

    choose_course = input*('Choose a course: ')
    choose_course = choose_course.upper()

    if choose_course != 'CSC121' or choose_course != 'CSC122' or choose_course != 'CSC221':
        print('Error: Not a valid course')
        return

    if choose_course == 'CSC121':
        print('Students in CSC121: ', r_list[0].sort())
        return
    elif choose_course == 'CSC122':
        print('Students in CSC122: ', r_list[1].sort())
        return
    else:
        print('Students in CSC221: ', r_list[2].sort())
        return


def change_max_size(r_list, m_list):
    """Allows an admin to change the class size of any course

    Asks what course they wish toe change the max size of and checks to make sure it is a valid course
    Asks what the new max size should be and makes sure it isn't lower than the current amout enrolled in it

    """
    while True:
        course_to_change = input(
            'What course do you wish to change the max class size of? ')
        course_to_change = course_to_change.upper()

        if course_to_change == 'CSC121' or course_to_change == 'CSC122' or course_to_change == "CSC221":
            break
        else:
            print('Error: Invalid course')

    if course_to_change == 'CSC121':
        print(
            f'The number of students currenty enrolled in CSC121 is {len(r_list[0])} and the current max class size is {m_list[0]}.')
        new_max_size = int(
            input('What do you want to change the max class size of CSC121 to? '))
        while True:
            if new_max_size < len(r_list[0]):
                print(
                    'Error: New max class size can not be smaller than the number of current students enrolled in the course.')
                new_max_size = int(input(
                    f'Please enter a new max class size that is greater or equal to {len(r_list[0])}. '))
            else:
                break
        m_list[0] = new_max_size
        return
    elif course_to_change == 'CSC122':
        print(
            f'The number of students currenty enrolled in CSC122 is {len([1])} and the current max class size is {m_list[1]}.')
        new_max_size = int(
            input('What do you want to change the max class size of CSC122 to? '))
        while True:
            if new_max_size < len(r_list[1]):
                print(
                    'Error: New max class size can not be smaller than the number of current students enrolled in the course.')
                new_max_size = int(input(
                    f'Please enter a new max class size that is greater or equal to {len(r_list[1])}.'))
            else:
                break
        m_list[1] = new_max_size
        return
    else:
        print(
            f'The number of students currenty enrolled in CSC221 is {len(r_list[2])} and the current max class size is {m_list[2]}.')
        new_max_size = int(
            input('What do you want to change the max class size of CSC221 to? '))
        while True:
            if new_max_size < len(r_list[2]):
                print(
                    'Error: New max class size can not be smaller than the number of current students enrolled in the course.')
                new_max_size = int(input(
                    f'Please enter a new max class size that is greater or equal to {len(r_list[2])}.'))
            else:
                break
        m_list[2] = new_max_size
        return

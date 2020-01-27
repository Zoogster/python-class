"""Lets a student enroll or drop a course and see what they are enrolled in.

add_course -- Allows a student to enroll in a course.
drop_course -- Allows a student to drop a course.
list_courses --  Displays how many course they are enrolled in and what they are.
"""


def add_course(id, r_list, m_list):
    """Allow a student to enroll in a course.

    Checks to make sure they entered a valid course.
    If valid checks to see what course it is.
    Then checks to make sure they aren't already enrolled in the course.
    Then it checks to make sure the course isn't full.
    If there are no errors the student is added and given verification it worked.
    """

    while True:
        course_to_add = input('What course would you like to register for? ')
        course_to_add = course_to_add.upper()

        if course_to_add == 'CSC121' or course_to_add == 'CSC122' or course_to_add == 'CSC221':
            break
        else:
            print('Error: Invalid course')

    if course_to_add == 'CSC121':
        if id in r_list[0]:
            print('Error: You are already enrolled in that course')
            return
        elif len(r_list[0]) == m_list[0]:
            print('Error: Course is already full')
            return
        else:
            r_list[0].append(id)
            print('You have been enrolled in CSC121')
            return
    elif course_to_add == 'CSC122':
        if id in r_list[1]:
            print('Error: You are already enrolled in that course')
            return
        elif len(r_list[1]) == m_list[1]:
            print('Error: Course is already full')
            return
        else:
            r_list[1].append(id)
            print('You have been enrolled in CSC122')
            return
    else:
        if id in r_list[2]:
            print('Error: You are already enrolled in that course')
            return
        elif len(r_list[2]) == m_list[2]:
            print('Error: Course is already full')
            return
        else:
            r_list[2].append(id)
            print('You have been enrolled in CSC221')
            return


def drop_course(id, r_list):
    """Allows a student to drop a course.

    First checks if they entered a valid course.
    If valid checks what course they wish to drop.
    Then checks if they are enrolled in the course.
    If they are enrolled in the course it removes them and gives verification it worked.
    """
    while True:
        course_to_drop = input('What course do you wish to drop? ')
        course_to_drop = course_to_drop.upper()

        if course_to_drop == 'CSC121' or course_to_drop == 'CSC122' or course_to_drop == 'CSC221':
            break
        else:
            print('Error: Invalid Course')

    if course_to_drop == 'CSC121':
        if id not in r_list[0]:
            print('Error: You are not currently enrolled in this course')
            return
        else:
            r_list[0].remove(id)
            print('You have been removed from CSC121')
            return
    elif course_to_drop == 'CSC122':
        if id not in r_list[1]:
            print('Error: You are not currently enrolled in this course')
            return
        else:
            r_list[1].remove(id)
            print('You have been removed from CSC122')
            return
    else:
        if id not in r_list[2]:
            print('Error: You are not currently enrolled in this course')
            return
        else:
            r_list[2].remove(id)
            print('You have been removed from CSC221')
            return


def list_courses(id, r_list):
    """Shows how many courses the student is in and what they are

    Counts how many courses they are in.
    Puts the courses they are in into a list.
    Tells them how many courses they are in and what they are.
    """
    count = 0
    for i in range(len(r_list)):  # counting how many times their id shows up
        if id in r_list[i]:
            count = count + 1

    course_list = []
    if id in r_list[0]:
        course_list.append('CSC121')
    if id in r_list[1]:
        course_list.append('CSC122')
    if id in r_list[2]:
        course_list.append('CSC221')

    print(
        f'You are currently enrolled in {count} courses and they are: {course_list}')

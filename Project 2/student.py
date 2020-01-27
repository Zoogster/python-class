from user import User
from course import Course

"""Lets a student enroll or drop a course and see what they are enrolled in.

Student(User) -- Creates and manages Student objects.
add_course -- Allows a student to enroll in a course.
drop_course -- Allows a student to drop a course.
list_courses --  Displays how many course they are enrolled in and what they are.
"""


class Student(User):
    """Creates and manages Student objects."""

    def __init__(self, id, pin):
        super().__init__(id, pin)

    def add_course(self, c_list):
        """Allow a student to enroll in a course.

        Checks to make sure they entered a valid course. If valid it calls 
        add_student(). Returns nothing. If not valid gives error and returns.
        """

        course_to_add = input('Enter the course you wish to add: ')
        if course_to_add == 'CSC121':
            c_list[0].add_student(self._id)
            return
        elif course_to_add == 'CSC122':
            c_list[1].add_student(self._id)
            return
        elif course_to_add == 'CSC221':
            c_list[2].add_student(self._id)
            return
        else:
            print('Error: Course not offered')
            return

    def drop_course(self, c_list):
        """Allows a student to drop a course.

        First checks if they entered a valid course. If valid calls drop_student().
        Returns nothing. If not valid gives error and returns.
        """

        course_to_drop = input('What course do you wish to drop: ')
        if course_to_drop == 'CSC121':
            c_list[0].drop_student(self._id)
            print('Course dropped')
            return
        elif course_to_drop == 'CSC122':
            c_list[1].drop_student(self._id)
            return
        elif course_to_drop == 'CSC221':
            c_list[2].drop_student(self._id)
            print('Course dropped')
            return
        else:
            print('Error: Course not offered')
            return

    def list_courses(self, c_list):
        """Displays how many course they are enrolled in and what they are.

        Starts with count at 0 and empty list to put courses they are enrolled in.
        Checks every course using student_in_course. If they are in it count +1 and
        add course to the list. Lastly prints the course they are in and the count. 
        Returns nothing.
        """
        count = 0
        s_course_list = []
        if c_list[0].student_in_course(self._id) == True:
            s_course_list.append('CSC121')
            count = count + 1
        if c_list[1].student_in_course(self._id) == True:
            s_course_list.append('CSC122')
            count = count + 1
        if c_list[2].student_in_course(self._id) == True:
            s_course_list.append('CSC221')
            count = count + 1
        for i in range(len(s_course_list)):
            print(s_course_list[i])
        print('Number of courses: ', count)
        return

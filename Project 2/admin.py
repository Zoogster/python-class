from user import User
from course import Course

"""Lets an admin look at the roster and change max class size.

Admin(User) -- Creates and manages Admin objects.
show_roster -- Displays roster of a course.
change_max_size -- Allows admin to change max class size.
"""


class Admin(User):
    """Creates and manages Admin objects."""

    def __init__(self, id, pin):
        super().__init__(id, pin)

    def show_roster(self, c_list):
        """Displays the roster for a chosen course.

        Checks to make sure the course entered is valid.
        If it is valid calls display_roster(). Returns nothing.
        If not valid gives error and returns.
        """

        course_to_see = input('Enter course to see the roster of: ')
        if course_to_see == 'CSC121':
            c_list[0].display_roster()
            return
        elif course_to_see == 'CSC122':
            c_list[1].display_roster()
            return
        elif course_to_see == 'CSC221':
            c_list[2].display_rostert()
            return
        else:
            print('Error: Course not offered')
            return

    def change_max_size(self, c_list):
        """Allows an admin to change the class size of any course.

        Asks what course they wish toe change the max size of and checks to make sure it is a 
        valid course. If it is calls change_max_size(). Returns nothing. If not valid
        gives error and returns.
        """

        course_size_to_change = input(
            'Enter the course to change the size of: ')
        if course_size_to_change == 'CSC121':
            c_list[0].change_max_size()
            return
        elif course_size_to_change == 'CSC122':
            c_list[1].change_max_size()
            return
        elif course_size_to_change == 'CSC221':
            c_list[2].change_max_size()
            return
        else:
            print('Error: Course not offered')
            return
        return

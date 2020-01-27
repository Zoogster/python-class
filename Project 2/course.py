"""Creates and manages Course class objects.

Course -- Creates and manages Course objects.
add_student -- Adds student to course.
drop_student -- Removes student from course.
display_roster -- Shows student enrolled in course.
change_max_size -- Allows to change max class size.
get_course_code -- Gets course code.
student_in_course -- Tests if the ID is in course roster.
"""


class Course:
    """Creates and manages Course class objects."""

    def __init__(self, c_code, m_size):
        self._course_code = c_code
        self._max_size = m_size
        self._roster = []

    def add_student(self, id):
        """Adds student to course.

        Tests if course is full. If it is gives error and returns. Then
        tests if the student is already enrolled. If they are gives error and
        returns. If everything is fine student ID is added to course roster. 
        Tells user student was added. Returns nothing.
        """
        if self._max_size <= len(self._roster):
            print('Error: Course already full')
            return
        elif id in self._roster:
            print('Error: Student already enrolled')
            return
        else:
            self._roster.append(id)
            print(f'Student {id} was added to {self._course_code}')
            return

    def drop_student(self, id):
        """Removes student from course.

        If enrolled removes them from roster. Returns nothing.
        If not enrolled gives error and returns.
        """
        if id in self._roster:
            self._roster.remove(id)
            return

        else:
            print('Error: Student not enrolled in course')
            return

    def display_roster(self):
        """Shows students enrolled in course.

        Use loop to print each ID in course. Then prints the number of students enrolled. Returns nothing.
        """
        for i in range(len(self._roster)):
            print(self._roster[i])
        print('Number of students enrolled: ', len(self._roster))
        return

    def change_max_size(self):
        """Allows to change max class size.

        Informs user current max size. Asks them to put in desired new max size. If new max size is smaller than current
        enrollment gives error. Tells them number of students currently enrolled and asks them to make the max size equal or greater
        than it. If new max size is fine changes it and informs user that it was changed. Returns nothing.
        """
        print('Current max class size is:', self._max_size)
        new_max_size = int(input('Please enter new max class size: '))
        while True:
            if new_max_size < len(self._roster):
                print(
                    'Error: New max class size can not be smaller than the number of students currently enrolled in the course.')
                new_max_size = int(input(
                    f'Please enter a new max class size that is greater or equal to {len(self._roster)}: '))
            else:
                break
        self._max_size = new_max_size
        print('Max class size changed to: ', self._max_size)
        return

    def get_course_code(self):
        """Gets course code.

        Returns course code of course object.
        """
        return self._course_code

    def student_in_course(self, id):
        """Tests if the ID is in course roster.

        Returns True if the ID is in roster. Returns False if it is not.
        """
        if id in self._roster:
            return True
        else:
            return False

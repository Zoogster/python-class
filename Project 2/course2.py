class Course:

    def __init__(self, c_code, m_size):
        self._course_code = c_code
        self._max_size = m_size
        self._roster = []

    def add_student(self, id):
        self._roster.append(id)
        print(self._roster)
        return

    def drop_student(self, id):
        if not id in self._roster:
            print('Error: Student not enrolled in course')
            return
        else:
            self._roster.remove(id)
            return

    def display_roster(self):
        self._roster = sorted(self._roster)
        for student in self._roster:
            print(student)
        print('Number of students: ', len(self._roster))
        return

    def change_max_size(self):
        print('Current max class size is:', len(self._roster))
        new_max_size = int(input('Please enter new max class size: '))
        while True:
            if new_max_size < len(self._roster):
                print(
                    'Error: New max class size can not be smaller than the number of students currently enrolled in the course.')
                self.new_max_size = int(input(
                    f'Please enter a new max class size that is greater or equal to {len(self._roster)}:'))
            else:
                break
        self._max_size = new_max_size
        return

    def get_course_code(self):
        return self._course_code

    def student_in_course(self, id):
        if id in self._roster:
            return True
        else:
            return False

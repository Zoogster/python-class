class Course:

    def __init__(self, c_code, c_max_size):

        self.code = c_code
        self.max_size = c_max_size
        self.enrollment = 0

    def add_student(self):

        if self.enrollment < self.max_size:
            self.enrollment = self.enrollment + 1
            print('One student added')
            print('Enrollment: ', self.enrollment)
        else:
            print('Course already full')

    def drop_student(self):

        if self.enrollment > 0:
            self.enrollment = self.enrollment - 1
            print('One student dropped')
            print('Enrollment: ', self.enrollment)
        else:
            print('Course is empty')

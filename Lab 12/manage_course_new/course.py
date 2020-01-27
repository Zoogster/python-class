class Course:

    def __init__(self, c_code, c_max_size):

        self.__code = c_code
        self.__max_size = c_max_size
        self.__enrollment = 0

    def add_student(self):

        if self.__enrollment < self.__max_size:
            self.__enrollment = self.__enrollment + 1
            print('One student added')
            print('Enrollment: ', self.__enrollment)
        else:
            print('Course already full')

    def drop_student(self):

        if self.__enrollment > 0:
            self.__enrollment = self.__enrollment - 1
            print('One student dropped')
            print('Enrollment: ', self.__enrollment)
        else:
            print('Course is empty')

    def getCode(self):
        return self.__code

    def getMax_size(self):
        return self.__max_size

    def getEnrollment(self):
        return self.__enrollment

    def setMax_size(self, new_max_size):
        if new_max_size < 0:
            print('Maximum class size cannot be negative')
        elif new_max_size < self.__enrollment:
            print('Maximum class size cannot be lower than current enrollment')
        else:
            self.__max_size = new_max_size

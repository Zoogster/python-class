from user import User

class Student(User):

    def __init__(self, id, pin):

        # ------------------------------------------------------------
        # This method takes two arguments: id and pin.  It calls the
        # constructor of the base class.
        # -------------------------------------------------------------




    def add_course(self, c_list):

        # ------------------------------------------------------------
        # This method adds a student to a course. It has one
        # parameter: c_list, which is the list of Course objects. It
        # asks user to enter the course he/she wants to add. If the
        # course is not offered, display error message and stop.
        # Otherwise, call the add_student method of the course to add
        # the student. This method has no return value.
        # -------------------------------------------------------------




    def drop_course(self, c_list):

        # ------------------------------------------------------------
        # This method drops a student from a course. It has one
        # parameter: c_list, which is the list of Course objects. It
        # asks user to enter the course he/she wants to drop.  If the
        # course is not offered, display error message and stop.
        # Otherwise, call the drop_student method of the course to drop
        # the student. This method has no return value.
        # -------------------------------------------------------------




    def list_courses(self, c_list):

        # ------------------------------------------------------------
        # This method displays and counts courses a student has
        # registered for.  It has one parameter: c_list, which is the
        # list of Course objects.  It iterates over c_list to display
        # and count courses the student is in the roster. This method
        # has no return value.
        # -------------------------------------------------------------



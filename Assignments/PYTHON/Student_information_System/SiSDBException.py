class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Duplicate Enrollment"):
        self.message = message
        super().__init__(self.message)


class CourseNotFoundException(Exception):
    def __init__(self, message="Course Not Found"):
        self.message = message
        super().__init__(self.message)


class StudentNotFoundException(Exception):
    def __init__(self, message="Student Not Found"):
        self.message = message
        super().__init__(self.message)


#

class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher Not Found"):
        self.message = message
        super().__init__(self.message)


class PaymentValidationException(Exception):
    def __init__(self, message=" Invalid Payment "):
        self.message = message
        super().__init__(self.message)


class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid Student Data"):
        self.message = message
        super().__init__(self.message)


class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid Course Data"):
        self.message = message
        super().__init__(self.message)

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid Enrollment Data"):
        self.message = message
        super().__init__(self.message)


class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid Teacher Data"):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(Exception):
    def __init__(self, message=" Insufficient Funds"):
        self.message = message
        super().__init__(self.message)

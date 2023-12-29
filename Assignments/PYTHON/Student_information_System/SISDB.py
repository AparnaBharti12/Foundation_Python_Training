
class student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    @property
    def student_id(self):
        return self.student_id

    @student_id.setter
    def student_id(self, id):
        student_id = id

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, first_name):
        first_name = first_name

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

    @property
    def date_of_birth(self):
        return self.date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.phone_number = phone_number


# Course class with the following attributes:
# • Course ID
# • Course Name
# • Course Code
# • Instructor Name

class course:
    def __int__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    @property
    def course_id(self):
        return self.course_id

    @course_id.setter
    def course_id(self, course_id):
        self.course_id = course_id

    @property
    def course_name(self):
        return self.course_name

    @course_name.setter
    def course_name(self, course_name):
        self.course_name = course_name

    @property
    def course_code(self):
        return self.course_code

    @course_code.setter
    def course_code(self, course_code):
        self.course_code = course_code

    @property
    def instructor_name(self):
        return self.instructor_name

    @instructor_name.setter
    def instructor_name(self, instructor_name):
        self.instructor_name = instructor_name


class enrollment(student, course):
    def __init__(self, enroll_id, student_id, course_id, enrollment_date):
        self.enroll_id = enroll_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    @property
    def enroll_id(self):
        return self.enroll_id

    @enroll_id.setter
    def enroll_id(self, enroll_id):
        self.enroll_id = enroll_id

    @property
    def student_id(self):
        return self.student_id

    @student_id.setter
    def student_id(self, student_id):
        self.student_id = student_id

    @property
    def course_id(self):
        return self.course_id

    @course_id.setter
    def course_id(self, course_id):
        self.course_id = course_id

    @property
    def enrollment_date(self):
        return self.enrollment_date

    @enrollment_date.setter
    def enrollment_date(self, enrollment_date):
        self.enrollment_date = enrollment_date


# Teacher class with the following attributes:
# • Teacher ID
# • First Name
# • Last Name
# • Email
class teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self._teacher_id = teacher_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self._teacher_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


class payment(student):
    def __init__(self, payment_id, student_id, amount, payment_date):
        self._payment_id = payment_id
        self._student_id = student_id  # Reference to a Student object
        self._amount = amount
        self._payment_date = payment_date

    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

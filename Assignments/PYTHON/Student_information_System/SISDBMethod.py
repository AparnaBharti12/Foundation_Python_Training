import SiSDBException
from DatabaseConnection import create_connection
from SISDB import course, student, enrollment, teacher, payment
from datetime import datetime
connection = create_connection()
cur = connection.cursor(buffered=True)


# cursor = cnx.cursor(cursor = cnx.cursor(buffered=True))
def enrollment_course():
    if connection:
        try:
            stu_id = int(input("enter student id "))
            cou_id = int(input("enter course id "))
            donation_date = datetime.now().strftime("%Y-%m-%d")
            enroll_id = int(input("enter enrollment number "))
            #
            q1 = "select enrollment_id  from enrollments;"
            cur.execute(q1)
            val1 = cur.fetchall()
            for i in val1:
                if i[0] == enroll_id:
                    return True
                else:
                    raise SiSDBException.DuplicateEnrollmentException('Duplicate enrollment entered ')
            #
            cur.execute(
                "insert into enrollments(enrollment_id,student_id,course_id,enrollment_date) values(%s,%s,%s,%s)",
                (enroll_id, stu_id, cou_id, donation_date))
            connection.commit()
            print("enrollment added successfully")

        except Exception as e:
            print(f"Exception details  :{e}")
        finally:
            connection.close()
def updateStudentInfo():
    try:
        print("enter id of student to be updated ")
        stu_id = int(input("enter student id "))
        print("enter details ")
        first_name = input("enter student first name ")
        last_name = input("enter student last name ")
        date_of_birth = input("enter date of birth ")
        email = input("enter student email ")
        phone_number = int(input("enter student phone number "))

        if(stu_id==None or first_name=="" or last_name=="" or date_of_birth==None or email=="" or phone_number==None):
              raise SiSDBException.InvalidStudentDataException("Student information is missing ")

        q1 = (
            "update students set first_name  = %s,last_name  =%s,date_of_birth = %s,email = %s, phone_number  = %s "
            "where"
            "student_id  = %s")
        val1 = (first_name, last_name, date_of_birth, email, phone_number, stu_id)

        cur.execute(q1, val1)
        connection.commit()

    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()

def generate_payment_id():
    q1 = "select payment_id from payments order by payment_id desc"
    cur.execute(q1)
    var = cur.fetchone()
    return int(var[0]) + 1

def MakePayment():
    try:
        print("enter values")
        stu_id = int(input("enter student id "))
        amount = int(input("enter amount "))
        donation_date = datetime.now().strftime("%Y-%m-%d")
        if(amount<100):
            raise SiSDBException.InsufficientFundsException("Entered amount is invalid")

        q1 = "insert into payments(payment_id,student_id,amount,payment_date) values(%s,%s,%s,%s)"
        q2 = (generate_payment_id(), stu_id, amount, donation_date)
        cur.execute(q1, q2)
        connection.commit()
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()

def DisplayStudentInfo():
    try:
        cur.execute("select  * from students;")
        var = cur.fetchall()
        for i in var:
            print(f"Details OF {i[1]} {i[2]}  :")
            print(f"\n\n\tStudent ID : {i[0]}")
            print(f"\tFirst_Name : {i[1]}")
            print(f"\tLast_Name : {i[2]}")
            print(f"\tDate_Of_Birth : {i[2]}")
            print(f"\tEmail : {i[3]}")
            print(f"\tPhone_Number : {i[3]}\n\n")

    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def GetEnrolledCourses():
    try:
        cur.execute("select  * from enrollments;")
        enroll = cur.fetchall()
        cur.execute("select  * from courses;")
        courses = cur.fetchall()
        print("\n\nlist of enrolled courses : \n")
        for i in courses:
            flag = False
            for j in enroll:
                if i[0] == j[2]:
                    flag = True
                    break
            if flag == True:
                print(f"\t{i[1]}")

    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()

def GetPaymentHistory():
    try:
        cur.execute("select  * from payments;")
        var = cur.fetchall()
        print(f"Payment Details :")
        for i in var:
            print(f"\n\n\tPayment ID : {i[0]}")
            print(f"\tAmount : {i[2]}")
            print(f"\tPayment_Date : {i[3]}\n\n")

    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def AssignTeacher():
    try:
        teacher_id = int(input("enter teacher to enroll in specific course "))
        course_id = int(input("enter course id to enroll the teacher "))

        if teacher_id==None or teacher_id==0:
            raise SiSDBException.InvalidStudentDataException("invalid teacher_id")
        if course_id==None or course_id==0:
            raise SiSDBException.InvalidCourseDataException("invalid course_id")

        q1 = "update courses set teacher_id  = %s where course_id = %s"
        q2 = (teacher_id, course_id)
        cur.execute(q1, q2)
        connection.commit()
    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()

def UpdateCourseInfo():
    try:
        course_id = int(input("enter course_id to be updated  "))
        print("\nenter details ")
        q1   = "select course_id from courses ; "
        cur.execute(q1)
        val  = cur.fetchall()
        if course_id not in val:
            raise SiSDBException.CourseNotFoundException("invalid course_id")
        teacher_id = int(input("enter teacher  id "))
        q2 = "select teacher_id from teacher ; "
        cur.execute(q2)
        val1 = cur.fetchall()
        if teacher_id not in val1:
            raise SiSDBException.TeacherNotFoundException("invalid teacher id")
        course_name = input("enter course name ")
        credit = input("enter credits ")
        q1 = (
            "update courses set teacher_id  = %s,course_name  =%s,credits = %s where "
            "course_id  = %s")
        val1 = (teacher_id, course_name, credit, course_id)

        cur.execute(q1, val1)
        connection.commit()

    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()

def DisplayCourseInfo():
    try:
        cur.execute("select  * from courses")
        val = cur.fetchall()
        for i in val:
            print(f"Course_id : {i[0]}")
            print(f"Course_name : {i[1]}")
            print(f"Credits : {i[2]}")
            print(f"teacher_id : {i[3]}")

    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def GetEnrollments():
    global j
    try:
        q1 = "select * from enrollments;"
        cur.execute(q1)
        enroll_info = cur.fetchall()
        q2 = "select *from students "
        cur.execute(q2)
        student_info = cur.fetchall()
        print("\n\nlist  of students enrolled in courses : \n\n")
        for i in enroll_info:
            flag = False
            for j in student_info:
                if i[1] == j[0]:
                    flag = True
                    break
            if flag:
                print(f"{j[1]} {j[2]}")
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()


def GetTeacher():
    try:
        q1 = "select * from courses;"
        cur.execute(q1)
        courses_info = cur.fetchall()
        q2 = "select * from teacher;"
        cur.execute(q2)
        teacher_info = cur.fetchall()
        print("\n\nlist  of teachers  in courses : \n\n")
        for i in teacher_info:
            flag = False
            for j in courses_info:
                if i[0] == j[3]:
                    flag = True
                    break
            if flag:
                print(f"teacher name  : {i[1]} {i[2]}  course name  : {j[1]}")
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()


def GetCourses():
    try:
        q1 = "select * from courses;"
        cur.execute(q1)
        courses_info = cur.fetchall()
        q2 = "select * from enrollments;"
        cur.execute(q2)
        enrollments_info = cur.fetchall()
        print("\n\nlist  of courses associated with enrollments : \n\n")
        for i in courses_info:
            flag = False
            for j in enrollments_info:
                if i[0] == j[2]:
                    flag = True
                    break
            if flag:
                print(f"course name  : {i[1]} enrollment id  : {j[0]}   enrooment date   : {j[3]}")
    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def UpdateTeacherInfo():
    try:
        teacher_id = int(input("enter teacher ID of record to be updated \n\n"))
        q1  = "select teacher_id from teacher;"
        cur.execute(q1)
        val1  = cur.fetchall()

        if teacher_id not in val1:
            raise SiSDBException.InvalidTeacherDataException("invalid teacher id ")

        first_name = input("enter first name ")
        last_name = input("enter last name ")

        email = input("enter email ")

        if(first_name =="" or last_name=="" or email==""):
            raise SiSDBException.InvalidTeacherDataException("it is mendatery to fill the above fields")
        q1 = "update teacher set first_name  = %s,last_name  = %s,email = %s where teacher_id  = %s"
        q2 = (first_name, last_name, email, teacher_id)
        cur.execute(q1, q2)
        connection.commit()
    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def DisplayTeacherInfo():
    try:
        cur.execute("select * from teacher\n\n")
        val = cur.fetchall()
        for i in val:
            print(f"\n\n teacher_id : {i[0]}")
            print(f" first_name : {i[1]}")
            print(f" last_name : {i[2]}")
            print(f" email : {i[3]}\n\n")
    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()


def GetAssignedCourses():
    global j
    try:
        q1 = "select * from courses;"
        cur.execute(q1)
        courses_info = cur.fetchall()
        q2 = "select * from teacher;"
        cur.execute(q2)
        teacher_info = cur.fetchall()
        print("\n\nlist  of teacher associated with courses : \n\n")
        for i in courses_info:
            flag = False
            for j in teacher_info:
                if i[3] == j[0]:
                    flag = True
                    break
            if flag:
                print(f"course name  : {i[1]} teacher name : {j[1]} {j[2]}")
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()


def GetStudent():
    global j
    try:
        q1 = "select * from students;"
        cur.execute(q1)
        student_info = cur.fetchall()
        q2 = "select * from payments;"
        cur.execute(q2)
        payment_info = cur.fetchall()
        print("\n\nlist  of teacher associated with courses : \n\n")
        for i in student_info:
            flag = False
            for j in payment_info:
                if i[0] == j[1]:
                    flag = True
                    break
            if flag:
                print(f"student name  : {i[1]} {i[2]} payment amount : {j[2]}  payment date : {j[3]}")
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()


def GetPaymentAmount():
    try:
        cur.execute("select amount from payments ;")
        val = cur.fetchall()
        for i in val:
            print(i[0])
    except Exception as e:
        print(f"Exception details   : {e}")
    finally:
        connection.close()


def GetPaymentDate():
    try:
        sum_value = 0
        cur.execute("select payment_date from payments ;")
        val = cur.fetchall()
        for i in val:
            print(i[0])
    except Exception as e:
        print(f"Exception details  : {e}")
    finally:
        connection.close()

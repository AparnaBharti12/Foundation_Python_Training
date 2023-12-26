import SISDBMethod


def menu():
    print("WELCOME ")
    print("PRESS NUMBER 1 TO  5 ")
    print("PRESS 1 TO ENROLL A STUDENT IN THE COURSE ")
    print("PRESS 2 TO UPDATE STUDENT INFORMATION")
    print("PRESS 3 TO MAKE PAYMENTS")
    print("PRESS 4 TO  DISPLAY STUDENT INFORMATION")
    print("PRESS 5 TO  DISPLAY LIST OF COURSES IN WHICH STUDENTS ARE ENROLLED ")
    print("PRESS 6 TO GET PAYMENT HISTORY")
    print("PRESS 7  ASSIGN TEACHER TO THE COURSE ")
    print("PRESS 8 UPDATE COURSE INFORMATION ")
    print("PRESS 9 DISPLAY DETAILED INFORMATION ABOUT THE COURSE ")
    print("PRESS 10  TO DISPLAY LIST OF STUDENT ENROLLMENTS BASED ON THE COURSES")
    print("PRESS 11 TO DISPLAY LIST OF ASSIGNED TEACHERS IN COURSES")
    print("PRESS 12 TO  DISPLAY COURSES ASSOCIATED WITH ENROLLMENT ")
    print("PRESS 13 TO UPDATE TEACHER INFORMATION")
    print("PRESS 14 TO DISPLAY TEACHER INFORMATION ")
    print("PRESS 15 TO DISPLAY LIST OF COURSES ASSIGNED TO TEACHERS")
    print("PRESS 16 TO DISPLAY STUDENT ASSOCIATED WITH THE PAYMENT ")
    print("PRESS 17 TO DISPLAY PAYMENT AMOUNT")
    print("PRESS 18 TO DISPLAY PAYMENT DATE")
    print("PRESS 19 TO  EXIT ")
    ch = int(input("enter your choice here  :  "))
    if ch == 1:
        SISDBMethod.enrollment_course()
    elif ch == 2:
        SISDBMethod.updateStudentInfo()
    elif ch == 3:
        SISDBMethod.MakePayment()
    elif ch == 4:
        SISDBMethod.DisplayStudentInfo()
    elif ch == 5:
        SISDBMethod.GetEnrolledCourses()
    elif ch == 6:
        SISDBMethod.GetPaymentHistory()
    elif ch == 7:
        SISDBMethod.AssignTeacher()
    elif ch == 8:
        SISDBMethod.UpdateCourseInfo()
    elif ch == 9:
        SISDBMethod.DisplayCourseInfo()
    elif ch == 10:
        SISDBMethod.GetEnrollments()
    elif ch == 11:
        SISDBMethod.GetTeacher()
    elif ch == 12:
        SISDBMethod.GetCourses()
    elif ch == 13:
        SISDBMethod.UpdateTeacherInfo()
    elif ch == 14:
        SISDBMethod.DisplayTeacherInfo()
    elif ch == 15:
        SISDBMethod.GetAssignedCourses()
    elif ch == 16:
        SISDBMethod.GetStudent()
    elif ch == 17:
        SISDBMethod.GetPaymentAmount()
    elif ch == 18:
        SISDBMethod.GetPaymentDate()


menu()

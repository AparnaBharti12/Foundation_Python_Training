from DatabaseConnection import create_connection
from ICourierAdminService import ICourierAdminService
from CMSException import InvalidEmployeeIdException


class Employee(ICourierAdminService):
    def __init__(self, EmployeeID, Name, Email, ContactNumber, Role, Salary):
        self.EmployeeID = EmployeeID
        self.Name = Name
        self.Email = Email
        self.ContactNumber = ContactNumber
        self.Role = Role
        self.Salary = Salary

    def addCourierStaff(self):
        try:
            connection = create_connection()
            cur = connection.cursor(buffered=True)
            cur.execute("select  EmployeeID from Employee")
            var = cur.fetchall()
            if self.EmployeeID in var:
                raise InvalidEmployeeIdException("Duplicate Employee !!  ")
            q1 = "insert into employee( EmployeeID,Name,Email,ContactNumber,Role,Salary) values(%s,%s,%s,%s,%s,%s)"
            q2 = (self.EmployeeID, self.Name, self.Email, self.ContactNumber, self.Role, self.Salary)
            cur.execute(q1, q2)
        except Exception as e:
            print(f"Exception Details  : {e}")

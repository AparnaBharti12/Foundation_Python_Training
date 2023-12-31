from util.db_connection import get_connection


# -- User Table
class User:
    def __init__(self, UserID, Username, Password, Email, First_Name, Last_Name, Date_of_Birth, Profile_Picture):
        self.connection = get_connection()
        self.__UserID = UserID
        self.__Username = Username
        self.__Password = Password
        self.__Email = Email
        self.__First_Name = First_Name
        self.__Last_Name = Last_Name
        self.__Date_of_Birth = Date_of_Birth
        self.__Profile_Picture = Profile_Picture

    @property
    def UserID(self):
        return self.__UserID

    @UserID.setter
    def UserID(self, UserID):
        self.__UserID = UserID

    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password):
        self.__Password = Password

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, Email):
        self.__Email = Email

    @property
    def First_Name(self):
        return self.__First_Name

    @First_Name.setter
    def First_Name(self, First_Name):
        self.__First_Name = First_Name

    @property
    def Last_Name(self):
        return self.__Last_Name

    @Last_Name.setter
    def Last_Name(self, Last_Name):
        self.__Last_Name = Last_Name

    @property
    def Date_of_Birth(self):
        return self.__Date_of_Birth

    @Date_of_Birth.setter
    def Date_of_Birth(self, Date_of_Birth):
        self.__Date_of_Birth = Date_of_Birth

    @property
    def Profile_Picture(self):
        return self.__Profile_Picture

    @Profile_Picture.setter
    def Profile_Picture(self, Profile_Picture):
        self.__Profile_Picture = Profile_Picture

    def __str__(self):
        return f"USER ID  :  {self.UserID}\n"\
               f"USERNAME  : {self.Username}\n"\
               f"PASSWORD  :  {self.Password}\n"\
               f"EMAIL  :  {self.Email}\n"\
               f"FIRST NAME  : {self.First_Name}\n"\
               f"LAST NAME  :  {self.Last_Name}\n" \
               f"DATE OF BIRTH  : {self.Date_of_Birth}\n"\
               f"PROFILE PICTURE :  {self.Profile_Picture}"



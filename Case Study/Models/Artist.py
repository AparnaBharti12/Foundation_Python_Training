from util.db_connection import get_connection


# -- Artist Table
class Artist:
    def __init__(self, ArtistID, Name, Biography, BirthDate, Nationality, Website, Contact_Information):
        self.connection = get_connection()
        self.__ArtistID = ArtistID
        self.__Name = Name
        self.__Biography = Biography
        self.__BirthDate = BirthDate
        self.__Nationality = Nationality
        self.__Website = Website
        self.__Contact_Information = Contact_Information

    @property
    def ArtistID(self):
        return self.__ArtistID

    @ArtistID.setter
    def ArtistID(self, ArtistID):
        self.__ArtistID = ArtistID

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        self.__Name = Name

    @property
    def Biography(self):
        return self.__Biography

    @Biography.setter
    def Biography(self, Biography):
        self.__Biography = Biography

    @property
    def BirthDate(self):
        return self.__BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self.__BirthDate = BirthDate

    @property
    def Nationality(self):
        return self.__Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self.__Nationality = Nationality

    @property
    def Website(self):
        return self.__Website

    @Website.setter
    def Website(self, Website):
        self.__Website = Website

    @property
    def Contact_Information(self):
        return self.__Contact_Information

    @Contact_Information.setter
    def Contact_Information(self, Contact_Information):
        self.__Contact_Information = Contact_Information

    def __str__(self):
        return f" ARTIST ID    :  {self.__ArtistID}\n"\
               f" NAME         :  {self.__Name}\n"\
               f" BIOGRAPHY    :  {self.__Biography}\n"\
               f" BIRTHDATE    :  {self.__BirthDate}\n"\
               f" NATIONALITY  :  {self.__Nationality}\n"\
               f" WEBSITE      :  {self.__Website}\n"\
               f" PHONE        :  {self.__Contact_Information}"

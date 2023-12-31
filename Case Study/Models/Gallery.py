from util.db_connection import get_connection


# -- Gallery Table
class Gallery:
    def __init__(self, GalleryID, Name, Description, Location, Curator, OpeningHours):
        self.connection = get_connection()
        self.__GalleryID = GalleryID
        self.__Name = Name
        self.__Description = Description
        self.__Location = Location
        self.__Curator = Curator
        self.__OpeningHours = OpeningHours

    @property
    def GalleryID(self):
        return self.__GalleryID

    @GalleryID.setter
    def GalleryID(self, GalleryID):
        self.__GalleryID = GalleryID

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, Description):
        self.__Description = Description

    def __str__(self):
        return f" GALLERY ID       :  {self.__GalleryID}\n" \
               f" NAME             :  {self.__Name}\n" \
               f" DESCRIPTION      :  {self.__Description}\n" \
               f" LOCATION         :  {self.__Location}\n" \
               f" CURATOR          :  {self.__Curator}\n" \
               f" OPENING HOURS    :  {self.__OpeningHours} "

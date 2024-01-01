from util.db_connection import get_connection


# -- Artwork Table
class Artwork:
    def __init__(self, ArtworkID, Title, Description, CreationDate, Medium, ImageURL, ArtistID):
        self.connection = get_connection()
        self.__ArtworkID = ArtworkID
        self.__Title = Title
        self.__Description = Description
        self.__CreationDate = CreationDate
        self.__Medium = Medium
        self.__ImageURL = ImageURL
        self.__ArtistID = ArtistID

    @property
    def ArtworkID(self):
        return self.__ArtworkID

    @ArtworkID.setter
    def ArtworkID(self, ArtworkID):
        self.__ArtworkID = ArtworkID

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, Title):
        self.__Title = Title

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, Description):
        self.__Description = Description

    @property
    def CreationDate(self):
        return self.__CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self.__CreationDate = CreationDate

    @property
    def Medium(self):
        return self.__Medium

    @Medium.setter
    def Medium(self, Medium):
        self.__Medium = Medium

    @property
    def ImageURL(self):
        return self.__ImageURL

    @ImageURL.setter
    def ImageURL(self, ImageURL):
        self.__ImageURL = ImageURL

    @property
    def ArtistID(self):
        return self.__ArtistID

    @ArtistID.setter
    def ArtistID(self, ArtistID):
        self.__ArtistID = ArtistID

    def __str__(self):
        return f"\n\nARTWORK ID        :  {self.__ArtworkID}\n" \
               f" TITLE            :  {self.__Title}\n" \
               f" DESCRIPTION      :  {self.__Description}\n" \
               f" CREATION DATE    :  {self.__CreationDate}\n" \
               f" MEDIUM           :  {self.__Medium}\n" \
               f" IMAGE URL        :  {self.__ImageURL}\n" \
               f" ARTIST ID        :  {self.__ArtistID}\n\n"

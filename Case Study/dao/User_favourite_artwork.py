from util.db_connection import get_connection


# Junction class
# -- User_Favorite_Artwork Table (Sample favorites for users)
class user_favourite_artwork:

    def __init__(self, userID=None, ArtworkID=None):
        self.connection = get_connection()
        self.__userID = userID
        self.__ArtworkID = ArtworkID

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID):
        self.__userID = userID

    @property
    def ArtworkID(self):
        return self.ArtworkID

    @ArtworkID.setter
    def ArtworkID(self, ArtworkID):
        self.__ArtworkID = ArtworkID

    def __str__(self):
        return f" USER  ID       :  {self.__userID}\n" \
               f" ARTWORK ID     :  {self.__ArtworkID}\n"

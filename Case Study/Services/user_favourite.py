from dao.User_favourite_artwork import user_favourite_artwork
from util.db_connection import get_connection
from  myexceptions.exception import UserNotFoundException,ArtWorkNotFoundException

class user_favourite(user_favourite_artwork):
    def __init__(self, userID=None, ArtworkID=None):
        super().__init__(userID, ArtworkID)
        self.connection = get_connection()

    def check_artworkID_in_artwork(self, ArtworkID):
        cur = self.connection.cursor()
        cur.execute("SELECT ArtworkID FROM ARTWORK")
        values = cur.fetchall()
        if (ArtworkID,) not in values:
            return False
        return True

    def check_userID_in_user(self, UserID):
        cur = self.connection.cursor()
        cur.execute("SELECT UserID FROM USER")
        values = cur.fetchall()
        if (UserID,) not in values:
            return False
        return True

    def addArtworkToFavorite(self, ArtworkID, UserID):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("INVALID ARTWORK ID ")
            if not self.check_userID_in_user(UserID):
                raise UserNotFoundException("INVALID USER ID ")
            query = """
              INSERT INTO  USER_FAVOURITE_ARTWORK(UserID,ArtworkID) VALUES(%s,%s)
            """
            val = (UserID, ArtworkID)
            cur.execute(query, val)
            self.connection.commit()
            self.__init__(UserID, ArtworkID)
            print(str(self))
            print("\n\n\n\t\t\tADDED ARTWORK INTO USER FAVOURITE TABLE ")
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.commit()

    def removeArtworkFromFavorite(self, ArtworkID = None, UserID = None):
        try:
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("INVALID ARTWORK ID ")
            if not self.check_userID_in_user(UserID):
                raise UserNotFoundException("INVALID USER ID ")
            cur = self.connection.cursor()
            if ArtworkID:
                cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE ArtworkID = %s", (ArtworkID,))
            if UserID:
                cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE UserID = %s", (UserID,))
            print("\n\n\t\t\tARTWORK DELETED FROM USER FAVOURITE ARTWORK ")
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.commit()

    def getUserFavoriteArtworks(self, UserID):
        try:
            if not self.check_userID_in_user(UserID):
                raise UserNotFoundException("INVALID USER ID ")
            cur = self.connection.cursor()
            if UserID:
                query = """SELECT u.UserID,a.Title,a.Description,a.medium ,a.imageURL 
                FROM artwork a inner join user_favourite_artwork u 
                WHERE u.ArtworkID = a.ArtworkID and u.UserID = %s"""
                value = (UserID,)
                cur.execute(query, value)
                val = cur.fetchall()
                print("\n\n\t\tUSER FAVOURITE ARTWORK DETAILS\n\n")
                for info in val:
                    print(f"\t\tUSER ID       :   {info[0]}")
                    print(f"\t\tTITLE         :   {info[1]}")
                    print(f"\t\tDESCRIPTION   :   {info[2]}")
                    print(f"\t\tMEDIUM        :   {info[3]}")
                    print(f"\t\tIMAGE URL     :   {info[4]}")
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.commit()




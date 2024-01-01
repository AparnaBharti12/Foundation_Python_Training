from dao.User_favourite_artwork import user_favourite_artwork
from util.db_connection import get_connection
from myexceptions.exception import UserNotFoundException, ArtWorkNotFoundException


class user_favourite(user_favourite_artwork):
    def __init__(self, userID=None, ArtworkID=None):
        super().__init__(userID, ArtworkID)
        self.connection = get_connection()

    # Check whether ArtworkID is present in Artwork table or not
    def check_artworkID_in_artwork(self, ArtworkID) -> bool:
        cur = self.connection.cursor()
        cur.execute("SELECT ArtworkID FROM ARTWORK")
        values = cur.fetchall()
        if (ArtworkID,) not in values:
            return False
        return True

    # Check whether UserID is present in User table or not
    def check_userID_in_user(self, UserID) -> bool:
        cur = self.connection.cursor()
        cur.execute("SELECT UserID FROM USER")
        values = cur.fetchall()
        if (UserID,) not in values:
            return False
        return True

    # Add Artwork to User favourite table
    def addArtworkToFavorite(self, ArtworkID, UserID):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("ARTWORK NOT FOUND ")
            if not self.check_userID_in_user(UserID):
                raise UserNotFoundException("USER NOT FOUND  ")
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

    # Remove artwork from User Favourite table
    def removeArtworkFromFavorite(self, ArtworkID=None, UserID=None):
        try:
            cur = self.connection.cursor()
            if ArtworkID:
                if not self.check_artworkID_in_artwork(ArtworkID):
                    raise ArtWorkNotFoundException("INVALID ARTWORK ID ")
                cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE ArtworkID = %s", (ArtworkID,))
            if UserID:
                if not self.check_userID_in_user(UserID):
                    raise UserNotFoundException("INVALID USER ID ")
                cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE UserID = %s", (UserID,))
            print("\n\n\t\t\tARTWORK DELETED FROM USER FAVOURITE ARTWORK ")
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.commit()

    # Get User Favourite Artwork from User favourite table
    def getUserFavoriteArtworks(self, UserID):
        try:
            if not self.check_userID_in_user(UserID):
                raise UserNotFoundException("USER NOT FOUND")
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

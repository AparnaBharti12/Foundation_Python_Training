from util.db_connection import get_connection
from dao.Artwork import Artwork
from myexceptions.exception import ArtWorkNotFoundException, UserNotFoundException


class Artwork_management(Artwork):
    artwork_id = 131

    def __init__(self, Title=None, Description=None, CreationDate=None, Medium=None, ImageURL=None, ArtistID=None):
        Artwork.__init__(self, Artwork_management.artwork_id, Title, Description, CreationDate, Medium, ImageURL,
                         ArtistID)
        self.connection = get_connection()
        Artwork_management.artwork_id += 1

    # Add artwork in the Artwork table
    def addArtwork(self):
        try:
            cur = self.connection.cursor()
            query = """INSERT INTO ARTWORK(ArtworkID,Title,Description,CreationDate,Medium,ImageURL,ArtistID) values(%s,
          %s,%s,%s,%s,%s,%s)"""
            val = (
                self.ArtworkID, self.Title, self.Description, self.CreationDate, self.Medium,
                self.ImageURL, self.ArtistID)
            cur.execute(query, val)
            self.connection.commit()
            print(" \n\nARTWORK ADDED  SUCCESSFULLY ")
            return True

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
            return False
        finally:
            self.connection.close()

    # Check whether ArtworkID is present in the Artwork table
    def check_artworkID_in_artwork(self, ArtworkID) -> bool:
        cur = self.connection.cursor()
        cur.execute("SELECT artworkID FROM ARTWORK")
        values = cur.fetchall()
        if (ArtworkID,) not in values:
            return False
        return True

    # Update artwork based on ArtworkID  passed
    def updateArtwork(self, ArtworkID=None, ArtistID=None, Title=None, Description=None, CreationDate=None, Medium=None,
                      ImageURL=None):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("ARTWORK NOT FOUND ")
            if ArtworkID:
                if Title:
                    query = "UPDATE ARTWORK SET Title = %s WHERE ArtworkID = %s"
                    value = (Title, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif Description:
                    query = "UPDATE ARTWORK SET Description = %s WHERE ArtworkID = %s"
                    value = (Description, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif Medium:
                    query = "UPDATE ARTWORK SERT Medium = %s WHERE ArtworkID = %s"
                    value = (Medium, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif CreationDate:
                    query = "UPDATE ARTWORK SET CreationDate = %s WHERE ArtworkID = %s"
                    value = (CreationDate, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif ImageURL:
                    query = "UPDATE ARTWORK SET ImageURL = %s WHERE ArtworkID = %s"
                    value = (ImageURL, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

            elif ArtistID:
                if Title:
                    query = "UPDATE ARTWORK SET Title = %s WHERE ArtistID = %s"
                    value = (Title, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif Description:
                    query = "UPDATE ARTWORK SET Description = %s WHERE ArtistID = %s"
                    value = (Description, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif Medium:
                    query = "UPDATE ARTWORK SET Medium = %s WHERE ArtistID = %s"
                    value = (Medium, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif CreationDate:
                    query = "UPDATE ARTWORK SET CreationDate = %s WHERE ArtistID = %s"
                    value = (CreationDate, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

                elif ImageURL:
                    query = "UPDATE ARTWORK SET ImageURL = %s WHERE ArtistID = %s"
                    value = (ImageURL, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()
                    print("\n\n\t\t\t\tARTWORK UPDATED SUCCESSFULLY  ")
                    return True

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
            return False
        finally:
            self.connection.close()

    # Remove artwork from Artwork_gallery,user_favourite,Artwork table
    def removeArtwork(self, ArtworkID=None):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("ARTWORK NOT FOUND  ")
            cur.execute("DELETE FROM ARTWORK_GALLERY WHERE ArtworkID = %s", (ArtworkID,))
            cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE ArtworkID = %s", (ArtworkID,))
            cur.execute("DELETE FROM ARTWORK WHERE artworkID = %s", (ArtworkID,))
            print("\n\n\t\tARTWORK DELETED SUCCESSFULLY ")
            self.connection.commit()
            return True
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
            return False
        finally:
            self.connection.close()

    # Retrieve Artwork information based on ArtworkID passed
    def getArtworkById(self, ArtworkID):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("ARTWORK NOT FOUND ")
            query = """
                  SELECT * FROM ARTWORK WHERE artworkID = %s
            """
            value = (ArtworkID,)
            cur.execute(query, value)
            det = cur.fetchone()
            print("\n\n\t\tARTWORK DETAILS  \n\n\t\t")
            print('=' * 236)
            print(str(Artwork(det[0], det[1], det[2], det[3], det[4], det[5], det[6])))
            print('=' * 236)
            return det[0]
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
            return None
        finally:
            self.connection.close()

    # Search Artwork with any Keyword
    def searchArtworks(self, Title=None, Description=None, Medium=None):
        try:
            if Title:
                cur = self.connection.cursor()
                query = """
                    select * from artwork where Title like %s;
              """
                value = ('%' + Title + '%',)
                cur.execute(query, value)
                det = cur.fetchall()
                if len(det) == 0:
                    raise ArtWorkNotFoundException("ARTWORK NOT FOUND ")
                print("\n\n\t\t\t\t\t\t\t\tARTWORK DETAILS  \t\t\t\t\t\t\t\t")
                for info in det:
                    print('=' * 236)
                    print(str(Artwork(info[0], info[1], info[2], info[3], info[4], info[5], info[6])))
                print('=' * 236)

            if Description:
                cur = self.connection.cursor()
                query = """
                    select * from artwork where Description like %s;
              """
                value = ('%' + Description + '%',)
                cur.execute(query, value)
                det = cur.fetchall()
                if len(det) == 0:
                    raise ArtWorkNotFoundException("ARTWORK NOT  FOUND ")
                print("\n\n\t\t\t\t\t\tARTWORK DETAILS  \n\n\t\t")
                for info in det:
                    print(str(Artwork(info[0], info[1], info[2], info[3], info[4], info[5], info[6])))

            if Medium:
                cur = self.connection.cursor()
                query = """
                    select * from artwork where Medium like %s;
              """
                value = ('%' + Medium + '%',)
                cur.execute(query, value)
                det = cur.fetchall()
                if len(det) == 0:
                    raise ArtWorkNotFoundException("ARTWORK NOT  FOUND ")
                print("\n\n\t\t\t\t\t\tARTWORK DETAILS  \n\n\t\t")
                for info in det:
                    print(str(Artwork(info[0], info[1], info[2], info[3], info[4], info[5], info[6])))

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()


# a = Artwork_management("Three dynasty", "exceptional", "2011-02-20", "oil  on canvas",
#                        "https://www.geeksforgeeks.org/getter-and-setter-in-python", 213)
# value = a.addArtwork()
# print(value)

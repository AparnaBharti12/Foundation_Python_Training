from util.db_connection import get_connection
from dao.Artwork import Artwork
from myexceptions.exception import ArtWorkNotFoundException, UserNotFoundException


class Artwork_management(Artwork):
    artwork_id = 114

    def __init__(self, Title=None, Description=None, CreationDate=None, Medium=None, ImageURL=None, ArtistID=None):
        Artwork.__init__(self, Artwork_management.artwork_id, Title, Description, CreationDate, Medium, ImageURL,
                         ArtistID)
        self.connection = get_connection()
        Artwork_management.artwork_id += 1

    def addArtwork(self):
        try:
            cur = self.connection.cursor()
            query = """INSERT INTO ARTWORK(ArtworkID,Title,Description,CreationDate,Medium,ImageURL,ArtistID) values(%s,
          %s,%s,%s,%s,%s,%s)"""
            value = (
                Artwork_management.artwork_id, self.Title, self.Description, self.CreationDate, self.Medium,
                self.ImageURL, self.ArtistID)
            cur.execute(query, value)
            self.connection.commit()
            print(" \n\nARTWORK ADDED  SUCCESSFULLY ")
            print("\n\n\t\t ARTWORK DETAILS  \n\n\t\t")

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()

    def updateArtwork(self, ArtworkID=None, ArtistID=None, Title=None, Description=None, CreationDate=None, Medium=None,
                      ImageURL=None):
        try:
            cur = self.connection.cursor()
            if ArtworkID:
                if Title:
                    query = "UPDATE ARTWORK SET Title = %s WHERE ArtworkID = %s"
                    value = (Title, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif Description:
                    query = "UPDATE ARTWORK SET Description = %s WHERE ArtworkID = %s"
                    value = (Description, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif Medium:
                    query = "UPDATE ARTWORK SERT Medium = %s WHERE ArtworkID = %s"
                    value = (Medium, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif CreationDate:
                    query = "UPDATE ARTWORK SET CreationDate = %s WHERE ArtworkID = %s"
                    value = (CreationDate, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif ImageURL:
                    query = "UPDATE ARTWORK SET ImageURL = %s WHERE ArtworkID = %s"
                    value = (ImageURL, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

            elif ArtistID:
                if Title:
                    query = "UPDATE ARTWORK SET Title = %s WHERE ArtistID = %s"
                    value = (Title, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif Description:
                    query = "UPDATE ARTWORK SET Description = %s WHERE ArtistID = %s"
                    value = (Description, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif Medium:
                    query = "UPDATE ARTWORK SET Medium = %s WHERE ArtistID = %s"
                    value = (Medium, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif CreationDate:
                    query = "UPDATE ARTWORK SET CreationDate = %s WHERE ArtistID = %s"
                    value = (CreationDate, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

                elif ImageURL:
                    query = "UPDATE ARTWORK SET ImageURL = %s WHERE ArtistID = %s"
                    value = (ImageURL, ArtworkID)
                    cur.execute(query, value)
                    self.connection.commit()

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()

    def check_artworkID_in_artwork(self, ArtworkID):
        cur = self.connection.cursor()
        cur.execute("SELECT artworkID FROM ARTWORK")
        values = cur.fetchall()
        if (ArtworkID,) not in values:
            return False
        return True

    def removeArtwork(self, ArtworkID=None):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("INVALID ARTWORK ID ")
            cur.execute("DELETE FROM ARTWORK_GALLERY WHERE ArtworkID = %s", (ArtworkID,))
            cur.execute("DELETE FROM USER_FAVOURITE_ARTWORK WHERE ArtworkID = %s", (ArtworkID,))
            cur.execute("DELETE FROM ARTWORK WHERE artworkID = %s", (ArtworkID,))
            print("\n\n\t\tARTWORK DELETED SUCCESSFULLY ")

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()

    def getArtworkById(self, ArtworkID):
        try:
            cur = self.connection.cursor()
            if not self.check_artworkID_in_artwork(ArtworkID):
                raise ArtWorkNotFoundException("INVALID ARTWORK ID ")
            query = """
                  SELECT * FROM ARTWORK WHERE artworkID = %s
            """
            value = (ArtworkID,)
            cur.execute(query, value)
            det = cur.fetchone()
            print("\n\n\t\tARTWORK DETAILS  \n\n\t\t")
            print(str(Artwork(det[0], det[1], det[2], det[3], det[4], det[5], det[6])))
        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()

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
                print("\n\n\t\tARTWORK DETAILS  \n\n\t\t")
                for info in det:
                    print(str(Artwork(info[0], info[1], info[2], info[3], info[4], info[5], info[6])))

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
                print("\n\n\t\tARTWORK DETAILS  \n\n\t\t")
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
                print("\n\n\t\tARTWORK DETAILS  \n\n\t\t")
                for info in det:
                    print(str(Artwork(info[0], info[1], info[2], info[3], info[4], info[5], info[6])))

        except Exception as e:
            print(f"EXCEPTION DETAILS  :  {e}")
        finally:
            self.connection.close()

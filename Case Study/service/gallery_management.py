from dao.Gallery import Gallery
from util.db_connection import get_connection


class Gallery_management(Gallery):
    gallery_id = 411

    def __init__(self, Name=None, description=None, location=None, curator=None, openingHours=None):
        Gallery.__init__(self, Gallery_management.gallery_id, Name, description, location, curator, openingHours)
        self.connection = get_connection()
        Gallery_management.gallery_id = Gallery_management.gallery_id + 1

    def create_new_gallery(self):
        try:
            cur = self.connection.cursor()
            query = ("INSERT INTO GALLERY(GalleryID,Name,Description,Location,Curator,OpeningHours) VALUES(%s,%s,%s,"
                     "%s,%s,%s)")
            val = (Gallery_management.gallery_id, self.Name, self.Description, self.Location, self.Curator,
                   self.OpeningHours)
            cur.execute(query,val)
            self.connection.commit()
            print("NEW GALLERY SUCCESSFULLY CREATED")
            return True
        except Exception as e:
            print(f"EXCEPTION DETAILS  : {e}")
            return False
        finally:
            self.connection.close()

    def check_galleryID(self, galleryID) -> bool:
        cur = self.connection.cursor()
        cur.execute("SELECT galleryID FROM GALLERY")
        values = cur.fetchall()
        if (galleryID,) not in values:
            return False
        return True

    def update_gallery_information(self, GalleryID, Name, Description, Location, Curator, OpeningHours):
        try:
            cur = self.connection.cursor()
            if not self.check_galleryID(GalleryID):
                raise Exception("GALLERY NOT FOUND ")
            elif Name:
                cur.execute("UPDATE GALLERY SET Name = %s WHERE GalleryID = %s", (Name, GalleryID))
                print("GALLERY NAME UPDATED SUCCESSFULLY ")
            elif Description:
                cur.execute("UPDATE GALLERY SET Description = %s WHERE GalleryID = %s", (Description, GalleryID))
                print("GALLERY DESCRIPTION UPDATED SUCCESSFULLY ")
            elif Location:
                cur.execute("UPDATE GALLERY SET Location = %s WHERE GalleryID = %s", (Location, GalleryID))
                print("GALLERY LOCATION UPDATED SUCCESSFULLY ")
            elif Curator:
                cur.execute("UPDATE GALLERY SET Curator = %s WHERE GalleryID = %s", (Curator, GalleryID))
                print("GALLERY CURATOR UPDATED SUCCESSFULLY ")
            elif OpeningHours:
                cur.execute("UPDATE OpeningHours SET Name = %s WHERE GalleryID = %s", (OpeningHours, GalleryID))
                print("GALLERY OPENING HOURS UPDATED SUCCESSFULLY ")
        except Exception as e:
            print(f"EXCEPTION DETAILS  : {e}")
        finally:
            self.connection.close()

    def remove_gallery(self, GalleryID):
        try:
            cur = self.connection.cursor()
            if not self.check_galleryID(GalleryID):
                raise Exception("GALLERY NOT FOUND ")
            cur.execute("DELETE FROM ARTWORK_GALLERY WHERE GalleryID = %s", (GalleryID,))
            cur.execute("DELETE FROM GALLERY WHERE GalleryID  = %s", (GalleryID,))
            print("GALLERY SUCCESSFULLY REMOVED ")
            return True
        except Exception as e:
            print(f"EXCEPTION DETAILS  : {e}")
            return False
        finally:
            self.connection.close()

    def search_gallery(self, GalleryID):
        try:
            cur = self.connection.cursor()
            if not self.check_galleryID(GalleryID):
                raise Exception("GALLERY NOT FOUND ")
            cur.execute("SELECT * FROM GALLERY WHERE GalleryID = %s", (GalleryID,))
            info = cur.fetchone()
            print(f"GALLERY ID     :  {info[0]}")
            print(f"NAME           :  {info[1]}")
            print(f"DESCRIPTION    :  {info[2]}")
            print(f"LOCATION       :  {info[3]}")
            print(f"CURATOR        :  {info[4]}")
            print(f"OPENING HOURS  :  {info[5]}")
            return info[0]
        except Exception as e:
            print(f"EXCEPTION DETAILS  : {e}")
            return False
        finally:
            self.connection.close()




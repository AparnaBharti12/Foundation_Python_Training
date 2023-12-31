from util.db_connection import get_connection


# Junction table
# -- Artwork_Gallery Table (Sample artwork displayed in galleries)
class artwork_gallery:
    def __init__(self, ArtworkID, GalleryID):
        self.ArtworkID = ArtworkID
        self.GalleryID = GalleryID

    @property
    def ArtworkID(self):
        return self.ArtworkID

    @ArtworkID.setter
    def ArtworkID(self, ArtworkID):
        self.ArtworkID = ArtworkID

    @property
    def GalleryID(self):
        return self.GalleryID

    @GalleryID.setter
    def GalleryID(self, GalleryID):
        self.GalleryID = GalleryID

    def __str__(self):
        return f"ARTWORK ID   :  {self.ArtworkID}\n"\
               f"GALLERY ID   :  {self.GalleryID}"

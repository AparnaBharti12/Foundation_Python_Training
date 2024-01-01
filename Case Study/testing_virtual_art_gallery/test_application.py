from service.Artwork_management import Artwork_management
from service.gallery_management import Gallery_management
import unittest


class TestVirtualArtGallery(unittest.TestCase):
    def setUp(self):
        self.art = Artwork_management()
        self.gallery = Gallery_management()

    @unittest.SkipTest
    def test_add_artwork(self):
        self.artwork = Artwork_management("Girl before a Mirror", "women standing in front of a mirror looking at her "
                                                                  "reflection", "1932-12-12", "oil on canvas",
                                          "https://en.wikipedia.org/wiki/Girl_before_a_Mirror#/media/File"
                                          ":GirlBeforeAMirror.jpg", 213)
        added_artwork = self.artwork.addArtwork()
        self.assertTrue(added_artwork)

    def test_update_artwork_details(self):
        update_artwork = self.art.updateArtwork(ArtworkID=116, Title="self portrait by Vincent van Gogh ")
        self.assertTrue(update_artwork)

    @unittest.SkipTest
    def test_remove_artwork(self):
        remove_artwork = self.art.removeArtwork(115)
        self.assertTrue(remove_artwork)

    def test_search_artwork(self):
        search_artwork = self.art.getArtworkById(111)
        self.assertEqual(search_artwork, 111)

    @unittest.SkipTest
    def test_add_gallery(self):
        self.artwork_gallery = Gallery_management(" Louvre Museum", "World's largest art museum and historic monument",
                                                  "paris,France", 202, "10AM - 6PM")
        add_gallery = self.artwork_gallery.create_new_gallery()
        self.assertTrue(add_gallery)

    @unittest.SkipTest
    def test_remove_gallery(self):
        remove_gallery = self.gallery.remove_gallery(412)
        self.assertTrue(remove_gallery)

    def test_search_gallery(self):
        search_gallery = self.gallery.search_gallery(402)
        self.assertEqual(search_gallery, 402)


if __name__ == "__main__":
    unittest.main()

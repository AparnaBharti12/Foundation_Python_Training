from service.Artwork_management import Artwork_management
from service.user_favourite import user_favourite


class MainModule:
    def main(self):
        print("\n\n\t\t\t\t\t\t\t\t__________________.WELCOME TO VIRTUAL ART GALLERY.___________________________")
        print("\n\t\t\t\t\t\tPRESS 1 :  LOGIN AS ADMIN ")
        print("\n\t\t\t\t\t\tPRESS 2 :  LOGIN AS USER ")
        option = int(input("\n\n\t\t\t\t\tenter your choice here "))
        if option == 1:
            print("\n\t\t\t\t\t\tPRESS 1 :  ADD ARTWORK ")
            print("\n\t\t\t\t\t\tPRESS 2 :  DISPLAY ARTWORK ")
            print("\n\t\t\t\t\t\tPRESS 3 :  UPDATE ARTWORK ")
            print("\n\t\t\t\t\t\tPRESS 4 :  DISPLAY ARTWORKS BY ANY KEYWORD ")

            print("\n\t\t\t\t\t\tPRESS ANY NUMBER BETWEEN (1-5)")

            ch = int(input("\n\t\t\t\t\t\tenter your choice here  :  "))
            if ch == 1:
                Title = input("\n\n\tENTER ARTWORK TITLE  :  ")
                Description = input("\n\n\tENTER ARTWORK DESCRIPTION  :  ")
                CreationDate = input("\n\n\tENTER ARTWORK CREATION DATE  :  ")
                Medium = input("\n\n\tENTER ARTWORK  MEDIUM  :  ")
                ImageURL = input("\n\n\tENTER ARTWORK  IMAGE URL  :  ")
                ArtistID = input("\n\n\tENTER ARTWORK  ARTIST ID  :  ")
                a = Artwork_management(Title, Description, CreationDate, Medium, ImageURL, ArtistID)
                a.addArtwork()
                print(str(a))
            elif ch == 2:
                a = Artwork_management()
                ID = int(input(" \n\n\t\t ENTER ARTWORK ID "))
                a.getArtworkById(ID)
            elif ch == 3:
                a = Artwork_management()
                Artwork_ID = int(input(" \n\n\t\t ENTER ARTWORK ID "))
                print("\n\n\n\tPRESS 1     :   ENTER TITLE  ")
                print("\n\tPRESS 2     :   ENTER DESCRIPTION ")
                print("\n\tPRESS 3     :   ENTER MEDIUM  ")
                print("\n\tPRESS 4     :   CREATION DATE ")
                print("\n\tPRESS 5     :   IMAGE URL  ")

                op = int(input("\n\n\t\tenter your choice here  :  "))
                if op == 1:
                    val = input("\n\n\t\tENTER  TITLE  :  ")
                    a.updateArtwork(ArtworkID=Artwork_ID, Title=val)
                elif op == 2:
                    val = input("\n\n\t\tENTER DESCRIPTION  :  ")
                    a.updateArtwork(ArtworkID=Artwork_ID, Description=val)
                elif op == 3:
                    val = input("\n\n\t\tENTER  MEDIUM  :  ")
                    a.updateArtwork(ArtworkID=Artwork_ID, Medium=val)
                elif op == 4:
                    val = input("\n\n\t\tENTER CREATION DATE  :  ")
                    a.updateArtwork(ArtworkID=Artwork_ID, CreationDate=val)
                elif op == 5:
                    val = input("\n\n\t\tENTER  IMAGE URL  :  ")
                    a.updateArtwork(ArtworkID=Artwork_ID, ImageURL=val)
                else:
                    print("\n\n\t\t\tINVALID CHOICE INSERTED ")

            elif ch == 4:
                a = Artwork_management()
                print("\n\n\n\tPRESS 1     :   ENTER TITLE  ")
                print("\n\tPRESS 2     :   ENTER DESCRIPTION  ")
                print("\n\tPRESS 3     :   ENTER MEDIUM  ")

                op = int(input("\n\n\t\tenter your choice here  :  "))
                if op == 1:
                    val = input("\n\n\t\tENTER ANY KEYWORD OF TITLE  :  ")
                    a.searchArtworks(Title=val)
                elif op == 2:
                    val = input("\n\n\t\tENTER ANY KEYWORD OF DESCRIPTION  :  ")
                    a.searchArtworks(Description=val)
                elif op == 3:
                    val = input("\n\n\t\tENTER ANY KEYWORD OF MEDIUM  :  ")
                    a.searchArtworks(Medium=val)
                else:
                    print("\n\n\t\t\tINVALID CHOICE INSERTED ")
            else:
                print("\n\n\t\t\tINVALID CHOICE INSERTED ")
        elif option == 2:
            print("\n\t\t\t\t\t\tPRESS 1 :  ADD ARTWORK IN  YOUR FAVOURITE ")
            print("\n\t\t\t\t\t\tPRESS 2 :  REMOVE ARTWORK FROM YOUR FAVOURITE")
            print("\n\t\t\t\t\t\tPRESS 3 :  GET YOUR  FAVOURITE ARTWORK ")

            choice = int(input("\n\n\t\tenter your choice here "))

            if choice == 1:
                u = user_favourite()
                Artwork_id = int(input("\n\n\t\t  ENTER ARTWORK ID  : "))
                user_id = int(input("\n\n\t\t  ENTER USER ID  : "))
                u.addArtworkToFavorite(Artwork_id, user_id)
            if choice == 2:
                u = user_favourite()
                print("\n\t\t\t\t\t\tPRESS 1 :  ENTER ARTWORK ID ")
                print("\n\t\t\t\t\t\tPRESS 2 :  ENTER USER ID")
                ch = int(input("\n\n\t\tenter your choice here  : "))
                if ch == 1:
                    Artwork_id = int(input("\n\n\t\tENTER ARTWORK ID  : "))
                    u.removeArtworkFromFavorite(ArtworkID=Artwork_id)
                if ch == 2:
                    User_id = int(input("\n\n\t\tENTER USER ID  : "))
                    u.removeArtworkFromFavorite(UserID=User_id)
                else:
                    print("\n\n\t\tINVALID CHOICE ")
            if choice == 3:
                u = user_favourite()
                User_id = int(input("\n\n\t\tENTER USER ID  : "))
                u.getUserFavoriteArtworks(User_id)
            else:
                print("\n\n\t\tINVALID CHOICE INSERTED ")


m = MainModule()

m.main()

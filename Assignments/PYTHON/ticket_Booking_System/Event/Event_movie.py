from TicketEvent import Event
from DatabaseConnection import create_connection


class Movie(Event):
    def __init__(self, genre, ActorName, ActressName):
        self.genre = genre
        self.Actorname = ActorName
        self.ActressName = ActressName

    @property
    def genre(self):
        return self.genre

    @genre.setter
    def genre(self, genre):
        self.genre = genre

    @property
    def ActorName(self):
        return self.Actorname

    @ActorName.setter
    def ActorName(self, ActorName):
        self.ActorName = ActorName

    @property
    def ActressName(self):
        return self.ActressName

    @ActressName.setter
    def ActressName(self, ActressName):
        self.ActressName = ActressName

    def display_even_details(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select  * from movie")
        var = cur.fetchall()
        for i in var:
            print(f"GENRE :  {i[0]}")
            print(f"ACTOR NAME :  {i[1]}")
            print(f"ACTRESS  NAME :  {i[2]}")

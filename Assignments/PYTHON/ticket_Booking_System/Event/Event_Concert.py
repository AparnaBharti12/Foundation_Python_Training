from TicketEvent import Event
from DatabaseConnection import create_connection


class Concert(Event):
    def __init__(self, artist, Type):
        self.artist = artist
        self.Type = type

    @property
    def artist(self):
        return self.artist

    @artist.setter
    def artist(self, artist):
        self.artist = artist

    @property
    def Type(self):
        return self.Type

    @Type.setter
    def Type(self, Type):
        self.Type = Type

    def display_concert_details(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from concert")
        var = cur.fetchall()
        for i in var:
            print(f"Artist name : {i[0]}")
            print(f" Type : {i[1]}")

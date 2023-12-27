from DatabaseConnection import create_connection


class Venue:
    def __init__(self, venue_id, venue_name, address):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.address = address

    def get_venue_id(self):
        return self.venue_id

    def get_venue_name(self):
        return self.venue_name

    def get_address(self):
        return self.address

    def display_venue_details(self,venue_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from venu where venue_id = %s",(venue_id,))
        val = cur.fetchall()
        for i in val:
            print(f"\n\nVENUE ID  : {i[0]}")
            print(f"VENUE  NAME  : {i[1]}")
            print(f"VENUE  ADDRESS : {i[2]}")

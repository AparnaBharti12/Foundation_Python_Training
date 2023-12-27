from datetime import date, datetime

from DatabaseConnection import create_connection


class Event:
    def __init__(self, event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats,
                 ticket_price, event_type, booking_id):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.booking_id = booking_id

    def get_event_id(self):
        return self.event_id

    def get_event_name(self):
        return self.event_name

    def get_event_date(self):
        return self.event_date

    def get_event_time(self):
        return self.event_time

    def get_venue_id(self):
        return self.venue_id

    def get_total_seats(self):
        return self.total_seats

    def get_available_seats(self):
        return self.available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def get_event_type(self):
        return self.event_type

    def get_booking_id(self):
        return self.booking_id

    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def calculate_total_revenue(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        q1 = """
        select e.event_id,e.ticket_price*b.num_tickets from event e 
        inner join booking b on e.event_id  = b.event_id;
        """
        cur.execute(q1)
        val = cur.fetchall()
        for i in val:
            print(f"for event Id {i[0]}  total revenue is {i[1]}")

    def getBookedNoOfTickets(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select booking_id,num_tickets from booking ")
        val = cur.fetchall()
        for i in val:
            print(f"No of booked tickets for Booking ID {i[0]} are {i[1]}")

    def book_ticket(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        try:
            booking_date = datetime.now().strftime("%Y-%m-%d")
            cur.execute("select ticket_price from event where event_id = %s", (self.event_id,))
            val = cur.fetchone()
            q1 = """
                      insert into booking(
                      booking_id,customer_id,event_id,num_tickets,total_cost,booking_date) values(%s,%s,%s,%s,%s,%s)
                    """
            q2 = (
            self.booking_id, self.customer_id, self.event_id, self.num_tickets, self.num_tickets * val[0], booking_date)
            cur.execute(q1, q2)
            connection.commit()
        except Exception as e:
            print(f"Exception details : {e}")
        finally:
            print("TICKED BOOKED SUCCESSFULLY !!! ")
            connection.close()

    def cancel_booking(self, num_tickets, booking_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select num_tickets  from booking where booking_id = %s", (booking_id,))
        val = cur.fetchone()
        if num_tickets < val[0]:
            ticket = num_tickets - val[0]
            cur.execute("update booking set num_tickets = %s where booking_id = %s", (ticket, booking_id))
            cur.execute("update event set  available_seats =  available_seats+%s", (val[0],))
            connection.commit()
            print("BOOKING DELETED SUCCESSFULLY !!!")

    def display_event_details(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from event")
        val = cur.fetchall()
        for i in val:
            print(f"\n\nEVENT ID  : {i[0]}")
            print(f"EVENT TIME  : {i[1]}")
            print(f"VENUE ID  : {i[2]}")
            print(f"TOTAL SEATS BOOKED  : {i[3]}")
            print(f"AVAILABLE  SEAT  : {i[4]}")
            print(f"TICKET PRICE   : {i[5]}")
            print(f"EVENT TYPE  : {i[6]}")
            print(f"BOOKING ID  : {i[7]}")
            print(f"EVENT  DATE  : {i[8]}")


e = Event(211, "Concert Extravaganza", "2023-12-12", "10:00  AM", 111, 120, 100,
          450, "Concert", 11)
# e.calculate_total_revenue()
# e.getBookedNoOfTickets()

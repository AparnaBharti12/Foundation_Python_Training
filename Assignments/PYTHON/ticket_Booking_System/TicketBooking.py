from datetime import datetime

from DatabaseConnection import *
from TicketEvent import Event
class Booking:
    def __init__(self, booking_id, customer_id, event_id, num_tickets):
        self.connection = create_connection()
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.event_id = event_id
        self.num_tickets = num_tickets

    def get_booking_id(self):
        return self.booking_id

    def get_customer_id(self):
        return self.customer_id

    def get_event_id(self):
        return self.event_id

    def get_num_tickets(self):
        return self.num_tickets

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
            q2 = (self.booking_id, self.customer_id, self.event_id, self.num_tickets, self.num_tickets * val[0],booking_date)
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
            cur.execute("update booking set num_tickets = %s where booking_id = %s",(ticket,booking_id))
            cur.execute("update event set  available_seats =  available_seats+%s",(val[0],))
            connection.commit()
            print("BOOKING DELETED SUCCESSFULLY !!!")

    def getAvailableNoOfTickets(self,event_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select  available_seats from event where event_id = %s",(event_id,))
        val = cur.fetchone()
        print(f"AVAIBALE SEATS FOR EVENT {event_id} ARE {val[0]}")
    def getEventDetails(self,booking_id):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from event where booking_id  = %s",(booking_id,))
        i = cur.fetchone()

        print(f"\n\nEVENT ID  : {i[0]}")
        print(f"EVENT TIME  : {i[1]}")
        print(f"VENUE ID  : {i[2]}")
        print(f"TOTAL SEATS BOOKED  : {i[3]}")
        print(f"AVAILABLE  SEAT  : {i[4]}")
        print(f"TICKET PRICE   : {i[5]}")
        print(f"EVENT TYPE  : {i[6]}")
        print(f"BOOKING ID  : {i[7]}")
        print(f"EVENT  DATE  : {i[8]}")


# b = Booking(14, 309, 204,12)
# b.book_ticket()
# b.getEventDetails()
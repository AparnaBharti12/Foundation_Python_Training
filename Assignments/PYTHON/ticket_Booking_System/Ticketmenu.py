from TicketEvent import Event
from TicketBooking import Booking
from TicketVenue import Venue
from TicketCustomer import Customer

print("\n\n\t\t\t__________________.WELCOME TO THE MAIN MENU.___________________")
print("\n\n PRESS 1 TO BOOK TICKET ")
print(" PRESS 2 TO CANCEL TICKET ")
print(" PRESS 3 TO DISPLAY NO OF TICKETS AVAILABLE FOR AN EVENT ")
print(" PRESS 4 TO DISPLAY EVENT DETAILS ")
print(" PRESS 5 TO DISPLAY USER DISPLAY ")
print(" PRESS 6 TO DISPLAY VENUE DISPLAY ")
ch = int(input("\n\n\n\t\tEnter your choice here  :  "))
alt = Booking(15, 302, 202, 2)
if ch == 1:
    print("\n\t\t\tENTER DETAILS  ")
    booking_id = int(input("\nENTER BOOKING ID  :  "))
    customer_id = int(input("\nENTER CUSTOMER ID  :  "))
    event_id = int(input("\nENTER EVENT ID  :  "))
    num_tickets = int(input("\nENTER NUMBER OF TICKETS  :  "))
    b = Booking(booking_id, customer_id, event_id, num_tickets)
    b.book_ticket()
if ch == 2:
    print("\n\t\t\tENTER DETAILS  ")
    booking_id = int(input("\nENTER BOOKING ID  :  "))
    ticket = int(input("\nENTER NO  OF TICKETS TO CANCEL  :  "))
    alt.cancel_booking(booking_id,ticket)
if  ch==3:
    print("\n\t\t\tENTER DETAILS  ")
    event_id = int(input("\nENTER EVENT ID  :  "))
    alt.getAvailableNoOfTickets(event_id)
if  ch==4:
    print("\n\t\t\tENTER DETAILS  ")
    booking_id = int(input("\nENTER BOOKING ID  :  "))
    alt.getEventDetails(booking_id)
if ch==5:
    print("\n\t\t\tENTER DETAILS  ")
    customer_id = int(input("\nENTER CUSTOMER ID  :  "))
    c = Customer(311,"Shreya Mittal","shreya@example.com","90987654321",11)
    c.display_customer_details(customer_id)
if ch==6:
    print("\n\t\t\tENTER DETAILS  ")
    venue_id = int(input("\nENTER VENUE ID  :  "))
    # (self, venue_id, venue_name, address):
    v  = Venue(111,"Gujarat Pavilion","100 Ahmedabad Street, Gandhinagar")
    v.display_venue_details(venue_id)
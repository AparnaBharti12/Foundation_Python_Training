from CMSCourier import Courier
from CMSLocation import Location


class payment(Courier, Location):
    def __init__(self, PaymentID, CourierID, LocationID, Amount, PaymentDate):
        self.PaymentID = PaymentID
        self.CourierID = CourierID
        self.LocationID = LocationID
        self.Amount = Amount
        self.PaymentDate = PaymentDate

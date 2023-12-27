from CMSCourier import Courier
from DatabaseConnection import create_connection


class CourierServices:
    def __init__(self, ServiceID, ServiceName, Cost):
        self.ServiceID = ServiceID
        self.ServiceName = ServiceName
        self.Cost = Cost



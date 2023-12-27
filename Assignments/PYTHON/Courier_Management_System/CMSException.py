class  TrackingNumberNotFoundException(Exception):
    def __init__(self, message=" Tracking Number  Not Found "):
        self.message = message
        super().__init__(self.message)


class  InvalidEmployeeIdException(Exception):
    def __init__(self, message=" Invalid Employee  Id"):
        self.message = message
        super().__init__(self.message)
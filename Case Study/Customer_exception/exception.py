class ArtWorkNotFoundException(Exception):
    def __init__(self, message=" Art Work Not Found"):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self, message=" User Not Found"):
        self.message = message
        super().__init__(self.message)

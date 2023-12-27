from DatabaseConnection import create_connection
from TicketEvent import Event


class sports(Event):
    def __init__(self, sportsName, teamName):
        self.sportsName = sportsName
        self.teamName = teamName

    @property
    def sportsName(self):
        return self.sportsName

    @sportsName.setter
    def sportsName(self, sportsName):
        self.sportsName = sportsName

    @property
    def teamName(self):
        return self.teamName

    @teamName.setter
    def teamName(self, teamName):
        self.teamName = teamName
    def  display_sports_details(self):
        connection = create_connection()
        cur = connection.cursor(buffered=True)
        cur.execute("select * from sports")
        var = cur.fetchall()
        for i in var:
            print(f"Sports name : {i[0]}")
            print(f" team name  : {i[1]}")


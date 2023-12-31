from util.db_connection import get_connection


class CrimeAnalysisServiceImpl:
    def __init__(self):
        self.connection = get_connection()

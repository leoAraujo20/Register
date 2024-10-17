import datetime

class DataBase:

    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = with open(sel.filename, 'r') as file:

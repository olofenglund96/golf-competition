import pymongo
from pymongo import MongoClient
from pprint import pprint

class MongoDB:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client['golf-league']

        serverStatusResult = self.db.command("serverStatus")
        pprint(serverStatusResult)
    

    def get_players(self):
        players = list(self.db.players.find().sort('score', direction=pymongo.DESCENDING))

        return players

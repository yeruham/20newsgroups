from pymongo import MongoClient


class DAL_mongo:

    def __init__(self, host, database, collection, user= None, password= None):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None


    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb://{self.user}:{self.password}@{self.host}::27017"
        else:
            URI = f"mongodb://{self.host}:27017"

        return URI


    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            self.client.admin.command("ping")
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def get_all(self):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            data = collection.find({}, {"_id": 0})
            return list(data)


    def insert_one(self, data):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            results = collection.insert_one(data)
            return results

    def delete_all(self):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            results =collection.delete_many({})
            return results


    def close_connection(self):
        if self.client:
            self.client.close()

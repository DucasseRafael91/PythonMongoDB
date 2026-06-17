from app import db
from bson import ObjectId

class ClientDAO:

    @staticmethod
    def find_clients():
        return list(db["clients"].find())

    @staticmethod
    def find_client_by_id(client_id):
        return db["clients"].find_one({"_id": client_id})

    @staticmethod
    def find_clients_by_first_name(first_name):
        return list(db["clients"].find({"first_name": first_name}))

    @staticmethod
    def create_client(last_name, first_name):
        return db["clients"].insert_one({"last_name": last_name,"first_name": first_name })

    @staticmethod
    def delete_client(client_id):
        return db["clients"].delete_one({"_id": ObjectId(client_id)})


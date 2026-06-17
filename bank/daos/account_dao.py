from app import db
from bson import ObjectId

class AccountDAO:

    @staticmethod
    def find_accounts():
        return list(db["accounts"].find())

    @staticmethod
    def find_client_by_id(client_id):
        return db["clients"].find_one({"_id": ObjectId(client_id)})

    @staticmethod
    def find_clients_by_first_name(first_name):
        return list(db["clients"].find({"first_name": first_name}))

    @staticmethod
    def create_account(client_id, solde):
        return db["accounts"].insert_one({"client_id": ObjectId(client_id), "solde": solde})

    @staticmethod
    def update_client(client_id, updated_client):
        return db["clients"].update_one({"_id": ObjectId(client_id)}, {"$set": updated_client})

    @staticmethod
    def delete_client(client_id):
        return db["clients"].delete_one({"_id": ObjectId(client_id)})


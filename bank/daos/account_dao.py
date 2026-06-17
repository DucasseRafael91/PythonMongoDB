from app import db
from bson import ObjectId

class AccountDAO:

    @staticmethod
    def find_accounts():
        return list(db["accounts"].find())

    @staticmethod
    def find_account_by_id(account_id):
        return db["accounts"].find_one({"_id": ObjectId(account_id)})

    @staticmethod
    def find_accounts_by_client_id(id):
        return list(db["accounts"].find({"client_id": ObjectId(id)}))

    @staticmethod
    def create_account(client_id, solde):
        return db["accounts"].insert_one({"client_id": ObjectId(client_id), "solde": solde})

    @staticmethod
    def update_account(account_id, updated_account):
        return db["accounts"].update_one({"_id": ObjectId(account_id)}, {"$set": updated_account})

    @staticmethod
    def delete_account(account_id):
        return db["accounts"].delete_one({"_id": ObjectId(account_id)})


from app import db
from bson import ObjectId

class OperationDAO:

    @staticmethod
    def create_operation_depot(account_id, type, montant):
        return db["operations"].insert_one({"compteId": ObjectId(account_id), "montant": montant, "type": type})

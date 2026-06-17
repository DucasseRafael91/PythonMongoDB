import sys
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["bank"]
    client.server_info()
except Exception as e:
    print(f"Erreur de connexion à la base de données : {e}")
    sys.exit(1)
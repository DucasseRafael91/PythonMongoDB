#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une sélection du prix Goncourt
"""
import app

from business.goncourt import Goncourt
from daos.client_dao import ClientDAO

def main() -> None:
    """Programme principal."""
    end_program = False
    while not end_program:
        print("\nVeuillez choisir une option :")
        print("1 - Créer un client")
        print("2 - Rechercher un client par prénom")
        print("3 - Modifier un client A FAIRE")
        print("4 - Suppprimer un client A FAIRE")
        print("5 - Liste des clients")

        choice = input("Tapez 1, 2, 3, 4 ou 5 : ")

        if choice == "1":
            last_name = input("Entrez le nom du client : ")
            first_name = input("Entrez le prénom du client : ")
            ClientDAO.create_client(last_name, first_name)
        elif choice == "2":
            print("Rechercher un prénom de client :")
            first_name = input("Entrez le prénom du client : ")
            clients = ClientDAO.find_clients_by_first_name(first_name)
            if not clients:
                print(f"Aucun client trouvé avec le prénom '{first_name}'.")
            else:
                print("Clients trouvés :")
                for i, client in enumerate(clients, start=1):
                    print(f"{i}. {client['first_name']} {client['last_name']}")
        elif choice == "5":
            clients = ClientDAO.find_clients()
            for client in clients:
                print(f"{client['first_name']} {client['last_name']}")
            end_program = True
        else:
            print("Choix invalide, veuillez taper 1, 2 ou 3.")

if __name__ == '__main__':
    main()

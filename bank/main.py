#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une sélection du prix Goncourt
"""
import app
from daos.client_dao import ClientDAO
from daos.account_dao import AccountDAO

def main() -> None:
    """Programme principal."""
    end_program = False
    while not end_program:
        print("\nVeuillez choisir une option :")
        print("1 - Créer un client")
        print("2 - Rechercher un client par prénom")
        print("3 - Modifier un client")
        print("4 - Suppprimer un client")
        print("5 - Liste des clients")
        print("6 - Créer un compte pour un client")
        print("7 - Consulter les comptes d'un client")
        print("8 - Modifier un compte d'un client")
        print("9 - Suppprimer un compte d'un client")
        print("10 - Liste des comptes d'un client")

        choice = input("Tapez 1, 2, 3, 4 ou 5 : ")

        if choice == "1":
            choice_1()
        elif choice == "2":
            choice_2()
        elif choice == "3":
            choice_3()
        elif choice == "4":
            choice_4()
        elif choice == "5":
            choice_5()
        elif choice == "6":
            solde = float(input("Entrez le solde initial du compte : "))
            client_id = input("Entrez l'ID du client pour lequel créer le compte : ")
            AccountDAO.create_account(client_id, solde)
        else:
            print("Choix invalide, veuillez taper 1, 2 ou 3.")

def choice_1():
    last_name = input("Entrez le nom du client : ")
    first_name = input("Entrez le prénom du client : ")
    ClientDAO.create_client(last_name, first_name)

def choice_2():
    print("Rechercher un prénom de client :")
    first_name = input("Entrez le prénom du client : ")
    clients = ClientDAO.find_clients_by_first_name(first_name)
    if not clients:
        print(f"Aucun client trouvé avec le prénom '{first_name}'.")
    else:
        print("Clients trouvés :")
        for i, client in enumerate(clients, start=1):
            print(f"{i}. {client['first_name']} {client['last_name']}")

def choice_3():
    clients = ClientDAO.find_clients()
    for client in clients:
        print(f"{client['_id']} {client['first_name']} {client['last_name']}")
    chosen_client_id = input("Entrez l'ID du client à modifier : ")
    client = ClientDAO.find_client_by_id(chosen_client_id)
    if client:
        new_first_name = input(f"Entrez le nouveau prénom pour {client['first_name']} : ")
        new_last_name = input(f"Entrez le nouveau nom pour {client['last_name']} : ")
        if new_first_name:
            client['first_name'] = new_first_name
        if new_last_name:
            client['last_name'] = new_last_name
        ClientDAO.update_client(chosen_client_id, client)
    else:
        print("Client non trouvé.")

def choice_4():
    client_id = input("Entrez l'ID du client à supprimer : ")
    ClientDAO.delete_client(client_id)

def choice_5():
    clients = ClientDAO.find_clients()
    for client in clients:
        print(f"{client['first_name']} {client['last_name']}")


if __name__ == '__main__':
    main()

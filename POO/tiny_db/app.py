# Activer l'env virtuel:
# 1- Installer tinydb:
#     pip install tinydb
# 2 - Creation de la base de donne
#
#
#
#


# 2-
from tinydb import TinyDB, Query, where

# from tinydb.storages import MemoryStorage


# 2- Permet de creer la base de donnee si elle n'existe
db = TinyDB("data.json", indent=4)
# db = TinyDB(storage=MemoryStorage)
#
#
# INSERT=======================================
# # - Inserer une ligne
# db.insert({"name": "Chri Chri", "age": 20, "deleted": False})
# # - Inserer plusieurs lignes:
# db.insert_multiple(
#     [
#         {"name": "DiagneShu", "age": 20, "deleted": False},
#         {"name": "FabiShu", "age": 19, "deleted": False},
#     ]
# )
#
#
# RECHERCHE=====================================
# Creer un objet Query qui nous permet de faire
user = Query()

# # Afficher tous les utilisateurs qui sont majeurs
# majeurs = db.search(user.age >= 18)
# print(majeurs)
# # OU BIEN
# majeurs = db.search(where("age") < 18)
# print(majeurs)
#
# # Afficher les user qui se nomme Toto:
# totos = db.search(user.name == "Toto")

# print(totos)
#
# # Afficher les user qui se nomme Breukh:
# breukhs = db.search(user.name == "Breukh")
# print(breukhs)

# # Afficher le premier user qui se nomme Breukh:
# breukh = db.get(user.name == "Breukh")
# print(breukh)

# # afficher les user qui ont un "Shu" dans leur nom:❌ => verifier si dans la base il y a un user dont le nom est Shu
# #
# shu_in_name = db.contains(user.name == "Breukh")
# print(shu_in_name)

# # UPDATE===================================
# #Modifier une valeur
# db.update({"age": 21}, where("name") == "Martinique")
#
# # Ajouter des attribute
# db.update({"bios": ["Flutter Dev", "Magician"]}, where("name") == "Martinique")
# print(len(db))
#
#
# # LA MEHODE UPSERT:
# db.upsert({"name": "FantiShu", "age": 23, "deleted": True}, where("name") == "Fanta")
#
#
# # SUPPRIMER=============
# #
# db.remove(where("age") == 16)
# #
#
#
# AJOUT DE NOUVELLE TABLE==================
# -ajouter une table produit
# #
# produit = db.table("Produit")
# produit.insert({"libelle": "Tapis-souris", "prix": 1500, "quantite": 122})
# produit.insert({"libelle": "Souris sans fil", "prix": 4500, "quantite": 15})
# produit.insert({"libelle": "Clavier", "prix": 2500, "quantite": 300})


categ = db.table("Categorie")
categ.insert({"lebelle": "Informatique"})
categ.insert({"lebelle": "Produit chimique"})

#
#
#
#
#
#
#
#
#
#

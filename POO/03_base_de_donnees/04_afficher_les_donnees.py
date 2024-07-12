import sqlite3

conn = sqlite3.connect("./database.db")

c = conn.cursor()

# Prendre des donnees de la base une par une
c.execute("SELECT * FROM produit")
data = c.fetchone()
print(data)
print("==========================")
data = c.fetchone()
print(data)
print("==========================")
# =========================================
# Prendre les donnees de la base
#
c.execute("SELECT libelle, prix FROM produit")

datas = c.fetchall()  # Impossible d'executer cette requetes deux fois de suite
print(datas)
print("-----------------------")
datas = c.fetchall()
print(datas)


# Afficher les produit en rupture de stock
c.execute("SELECT * FROM produit WHERE quantite = 0")

ruptures = c.fetchall()
print("=======================PRODUITS EN RUPTURE=============")
print(ruptures)

# Afficher le nombre de produits en rupture de stock
print("=======================LE NOMBRE DE PRODUITS EN RUPTURE=============")
print(len(ruptures))

conn.close()

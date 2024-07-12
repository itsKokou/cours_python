# 1 - Creation de table ou tableau
    # -> Recperer le cursor (Permet d'ecrire dans le fichier), on execute 
    #     les requetes avec ce cursor
    # -> Eecuter une requete avec la methode execute() du cursor 
    # -> Appliquer la requete au niveau de la base de donnees avec la methode 
    # commit() de la connexion

import sqlite3

conn = sqlite3.connect("./database.db")

# Recup du corsor:
c = conn.cursor()
# Execution d'une requete:
c.execute("CREATE TABLE IF NOT EXISTS produit(id number, libelle text, prix number, quantite number)")
# Appliquer la requete dans la base
conn.commit()
conn.close()


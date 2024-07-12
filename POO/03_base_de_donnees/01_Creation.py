# sqlite3 est un module qui est fourni par defaut
import sqlite3



# Cree une connexion : si le fichier de la base de donnees n'existe il le cree
conn = sqlite3.connect("./database.sqlite3")

# .... 

# Fermer la base de donnees 
conn.close()


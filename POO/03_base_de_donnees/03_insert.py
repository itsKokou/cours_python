import sqlite3

conn = sqlite3.connect("./database.db")

# Recup du corsor:
c = conn.cursor()
# Execution d'une requete:
# c.execute("""
#     INSERT INTO produit(id,libelle,prix,quantite)
#     VALUES(1,'Sucre',100,23)
# """)
#
# c.execute(
#     """
#     INSERT INTO produit(id,libelle,prix,quantite)
#     VALUES(:id,:libelle,:prix,:quantite)
# """,
#     {"id": 2, "libelle": "Banane", "prix": 150, "quantite": 100},
# )
#

param = {"i": 3, "l": "Sel", "p": 500, "q": 25}
c.execute(
    """
    INSERT INTO produit(id,libelle,prix,quantite)
    VALUES(:i,:l,:p,:q)
""",
    param,
)

# Appliquer la requete dans la base
conn.commit()
conn.close()

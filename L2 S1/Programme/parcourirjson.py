import json 
with open('essai.json',"r") as fichier:
    affiche=json.load(fichier)
print(affiche[0]["name"])
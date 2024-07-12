import json

with open('kokou.json') as mon_fichier:
    data = json.load(mon_fichier)
    
print(data)
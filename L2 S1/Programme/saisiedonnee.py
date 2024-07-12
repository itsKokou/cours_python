#Soit la constante suivante : “Je m’appelle … et j’étudie à l’école … mon langage préféré est …”.
#Écrire un programme qui affiche la constante avec vos données personnelles saisi au clavier
char ="""Je m’appelle … et j’étudie à l’école … mon langage préféré est …"""
nom = input("Entrez votre nom :")
ecole =input("Quel est le nom de votre école :")
lang = input("Quel est votre langage préféré ?")
list = char.split("…")
list[0]+=nom
list[1]+=ecole
list[2]+=lang
char = ''.join(list)
print(char)
#Écrire un programme qui permet de remplir une liste d’entier puis de saisir un entier N, 
# Le programme supprime toutes les occurrences de N de la liste.
nbre=input("Entrez une suite d'entiers : \n")
n= input("Veuillez saisir l'entier à supprimer : \n")
list = nbre.split(' ')
for i in range(len(list)-2):
    if (n==list[i]):
        del list[i]
print(list)
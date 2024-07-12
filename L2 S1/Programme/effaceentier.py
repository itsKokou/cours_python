#Écrire un programme qui permet de remplir une liste d’entiers.
# Le programme supprime les entiers dupliqués de la liste
n=0
list=[]
while(n<=0):
    n=int(input("Combien d'entier voulez-vous saisir ?\n"))
for i in range(0,n):
    x=int(input("Entrez un entier :\n"))
    list.append(x)
list =set(list)
print(list)
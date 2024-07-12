#Écrire un programme qui permet de remplir une liste de phrases puis de saisir un mot M, 
# Le programme supprime toutes les phrases contenant le mot de M de la liste.
n=0
list=[]
while(n<=0):
    n=int(input("Combien de phrase voulez-vous saisir ?\n"))
for i in range(0,n):
    x=input("Entrez une phrase :\n")
    list.append(x)
m=input("Entrez le mot :\n")
i=0
while (i<n):
    if (m in list[i]):
        del list[i]
        n=len(list)
    else :
        i=i+1 
print(list)
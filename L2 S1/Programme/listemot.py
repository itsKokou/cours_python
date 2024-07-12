#Écrire un programme qui permet de saisir une chaine de caractères CH et qui crée une liste 
#des mots contenant au moins un chiffre et une majuscule.
CH=str(input("Entrez une chaine de caractères : "))
list=CH.split(' ')
i=0
liste=[]
while (i<len(list)): 
    x=list[i]
    y=len(x)
    if (x.istitle() and x[y-1].isdigit()):
        liste.append(x)
    i=i+1
print(liste)

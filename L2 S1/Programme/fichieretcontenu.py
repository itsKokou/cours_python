#Ecrire un programme qui permet de creer un fichier texte avec du contenu 
#Le nom du fichier et son contenu sont saisis au clavier et affiche le nombre de caracteres saisis 
nom=input("Entrez le nom du fichier : \n")
contenu=input("Entrez le contenu du fichier :\n")
nomfichier=nom+".txt"
with open(nomfichier,"w",encoding='utf-8') as f:
    nbre=f.write(contenu)
    print("{} caracteres ont été saisis".format(nbre))
#with open(nomfichier,"r",encoding='utf-8') as f:
#    affiche = f.read()
#    print(affiche)
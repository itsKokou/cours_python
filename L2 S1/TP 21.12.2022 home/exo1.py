from genericpath import exists
invalide=True
while invalide==True :
    invalide=False
    nomFichier=input("Entrez le nom du fichier à créer : ").strip()
    for i in range(10):
        if str(i) in nomFichier or len(nomFichier)==0:
            invalide=True
    rep="OUI"
    if (invalide==False):
        nomFichier=f"{nomFichier}.txt"
        if exists(nomFichier):
            rep=input("Voulez-vous écraser le fichier existant ? [OUI/NON] : ").upper()
            while rep!="OUI" and rep!="NON":
                rep=input("Veillez repondre par OUI ou NON : ").upper()
        if (rep=="OUI"):
            with open(nomFichier,'w') as f:
                contenu=input("Entrez le contenu du fichier : ")
                contenuSansEspace=contenu.replace(' ','')
                #print(contenuSansEspace)
                while contenuSansEspace.isalnum()==False:    #isalnum(): teste s'il n'y'a que des alphanumériques
                    contenu=input("Entrez le contenu du fichier : ")
                    contenuSansEspace=contenu.replace(' ','')
                if (len(contenu)>100):
                    contenu=f"{contenu[:100]}..."
                f.write(contenu)
        else:
            invalide=True
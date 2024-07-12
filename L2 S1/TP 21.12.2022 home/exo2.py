messi={
    "nom":"MESSI",
    "age":35,
    "matchs":[
        {"date":"23/06/2021","buts":2},
        {"date":"25/08/2021","buts":3},
        {"date":"05/01/2022","buts":1},
        {"date":"03/07/2022","buts":3}
    ]
}
mbappe={
    "nom":"Kylian",
    "age":24,
    "matchs":[
        {"date":"23/06/2021","buts":0},
        {"date":"25/08/2021","buts":2},
        {"date":"05/01/2022","buts":1},
        {"date":"03/07/2022","buts":3}
    ]
}

def get_but(joueur:dict):
    nbreBut=0
    for m in joueur.get("matchs"):
        nbreBut+=m.get('buts')
    return nbreBut

def meilleur_buteur(joueur1:dict,joueur2:dict):
    nbreBut1=get_but(joueur1)
    nbreBut2=get_but(joueur2)
    if(nbreBut1>nbreBut2):
        return (joueur1.get('nom'),nbreBut1)
    return (joueur2.get('nom'),nbreBut2)
    
#print(meilleur_buteur(messi,mbappe))

def afficher_joueur(joueur:dict):
    print(f"Nom : {joueur.get('nom')}")
    print(f"Age : {joueur.get('age')}")
    print("Les matchs :")
    for m in joueur.get("matchs"):
        print(f"-> {m.get('date')} : {m.get('buts')} but(s)")

#afficher_joueur(messi)

def ecrire_fichier(joueur:dict):
    nomFichier=f"{joueur.get('nom')}.txt"
    with open(nomFichier,"w") as f:
        f.write(f"Nom : {joueur.get('nom')}\n")
        f.write(f"Age : {joueur.get('age')}\n")
        f.write("Les matchs : \n")
        for m in joueur.get("matchs"):
            f.write(f"-> {m.get('date')} : {m.get('buts')} but(s) \n")

ecrire_fichier(messi)
ecrire_fichier(mbappe)
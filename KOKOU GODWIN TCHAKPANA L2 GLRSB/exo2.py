Kone={
    "nom": "MOUSSA",
    "prenom":"Kone",
    "datenaiss":"01/01/2003",
    "classe": "L2 GLRSB",
    "semestre": 1,
    "annee":"2021-2022",
    "matieres":{
        "Sport":{"devoir":15,"examen":18,"coef":2},
        "Langage C":{"devoir":18.5,"examen":18,"coef":2},
        "Python":{"devoir":12,"examen":19,"coef":3},
        "Algo":{"devoir":14,"examen":16,"coef":4},
        "Photoshop":{"devoir":18,"examen":18,"coef":2},
        "Statistique":{"devoir":19,"examen":16,"coef":3},
    },
}

def create_bulletin(etudiant:dict):
    nomFichier=f"{etudiant.get('prenom')}.txt"
    TAILLE=105
    somMoy=0
    somCoef=0
    somPoints=0
    somDev=0
    somEXa=0
    n=0
    print(nomFichier)
    with open(nomFichier,"w",encoding='UTF-8') as f:
        f.write(f"""{'*'*TAILLE}\n""")
        msg=f""" ** BULLETIN DU SEMESTRE {etudiant.get('semestre')} ** """
        f.write(f"""{msg:^{TAILLE}} \n""")
        f.write(f"""{'*'*TAILLE}\n""")
        f.write(f"Nom : {etudiant.get('nom')}")
        an=f"Année Académique : {etudiant.get('annee')}"
        f.write(f"{an:>{TAILLE-13}}\n")
        f.write(f"Prenom : {etudiant.get('prenom')}\n")
        f.write(f"Date de naissance : {etudiant.get('datenaiss')}\n")
        f.write(f"Classe : {etudiant.get('classe')}\n\n")
        f.write(f"""{'-'*TAILLE}\n""")
        f.write(f"""| {"MODULES":<20} """)
        f.write(f"""| {"DEVOIR":<15} """)
        f.write(f"""| {"EXAMEN":<15} """)
        f.write(f"""| {"MOYENNE":<15} """)
        f.write(f"""| {"COEF":<15} """)
        f.write(f"""| {"POINTS ":<20} \n""")
        f.write(f"""{'-'*TAILLE}\n""")
        for key,val in etudiant.get('matieres').items():
            n+=1
            moy=(val.get("devoir") + 2*val.get("examen"))/3
            somMoy+=moy
            point=moy*val.get("coef")
            somPoints+=point
            somDev+=val.get("devoir")
            somEXa+=val.get("examen")
            somCoef+=val.get("coef")
            f.write(f"""| {key:<20} """)
            f.write(f"""| {str(val.get("devoir")):<15} """)
            f.write(f"""| {str(val.get("examen")):<15} """)
            f.write(f"""| {str(moy)[:5]:<15} """)
            f.write(f"""| {str(val.get("coef")):<15} """)
            f.write(f"""| {str(point)[:5]:<20} \n""")
            f.write(f"""{'-'*TAILLE}\n""")
        f.write(f"""| {"TOTAL":<20} """)
        f.write(f"""| {str(somDev):<15} """)
        f.write(f"""| {str(somEXa):<15} """)
        f.write(f"""| {str(somMoy)[:5]:<15} """)
        f.write(f"""| {str(somCoef):<15} """)
        f.write(f"""| {str(somPoints)[:5]:<20} \n""")
        f.write(f"""{'-'*TAILLE}\n""")
        f.write(f"""| Moyenne du semestre :  {str(somMoy/n)[:5]}\n""")
        f.write(f"""{'*'*TAILLE}\n""")


create_bulletin(Kone)
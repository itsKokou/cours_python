mamadou={
    "nom": "Fall",
    "prenom":"Mamadou",
    "datenaiss":"01/06/2023",
    "classe": "L2 GLRSB",
    "matieres":{
        "Sport":{"devoir":15,"examen":18},
        "Langage C":{"devoir":18.5,"examen":18},
        "Python":{"devoir":12,"examen":19},
        "Algo":{"devoir":14,"examen":16},
        "Photoshop":{"devoir":18,"examen":18},
        "Statistique":{"devoir":19,"examen":16},
    },
    "moyenne":17.62
}

def bulletin(etudiant:dict):
    nomFichier=f"{etudiant.get('nom')}.txt"
    print(nomFichier)
    with open(nomFichier,"w") as f:
        f.write(f"""{'*'*70}\n""")
        f.write(f"{'** BULLETIN DU 1er SEMESTRE **':^70} \n")
        f.write(f"""{'*'*70}\n""")
        f.write(f"Nom : {etudiant.get('nom')}\n")
        f.write(f"Prenom : {etudiant.get('prenom')}\n")
        f.write(f"Date de naissance : {etudiant.get('datenaiss')}\n")
        f.write(f"Classe : {etudiant.get('classe')}\n\n")
        f.write(f"""{'-'*70}\n""")
        f.write(f""" {"MATIERES":<25} """)
        f.write(f""" {"DEVOIR":<20} """)
        f.write(f""" {"EXAMEN":<25} \n""")
        f.write(f"""{'-'*70}\n""")
        for key,val in etudiant.get('matieres').items():
            f.write(f""" {key:<25} """)
            f.write(f""" {str(val.get("devoir")):<20} """)
            f.write(f""" {str(val.get("examen")):<25} \n""")
            f.write(f"""{'-'*70}\n""")
        f.write(f"""Moyenne du semestre:  {etudiant.get('moyenne')}\n""")
        f.write(f"""{'*'*70}\n""")


bulletin(mamadou)
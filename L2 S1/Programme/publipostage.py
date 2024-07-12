ENTETE="OSC 2022"
OBJET="Stage"
TEXTE="Bonjour {name},\nSuite à votre candidature à OSC, vous avez été sélectionné pour faire les tests.\nVotre login est : {email} et votre mot de passe est {passw}.\nMerci"
etudiants=[
    ["Toto","Sy","toto@exemple.com"],
    ["Tata","Sow","tata@exemple.com"],
    ["Momo","Sambou","momo@exemple.com"],
    ["Mount","Goat","mount@exemple.com"]
]
def mdp(nom,pnom):
    """Cette fonction permet de générer le mot de passe d'un étudiant (en majuscule), à partir de son nom et prenom passés en paramètre"""
    l=pnom.split() # argument par defaut de .split() => espace
    motdepasse=""
    for p in l:
        motdepasse+=p[0]
    motdepasse+=nom
    return motdepasse.upper()
def afficheLettre(e):
    """Cette fonction permet d'afficher la lettre d'un étudiant passé en paramètre""" #documentation
    print(ENTETE)
    print(f"Objet : {OBJET}")
    nomcomplet=e[0]+" "+e[1]
    password= mdp(e[1],e[0])
    print(TEXTE.format(name=nomcomplet,email=e[2],passw=password))
def genererLettre(e):
    """Cette fonction permet de générer un fichier texte contenant la lettre de l'etudiant"""
    with open(f"{e[2]}.txt","w",encoding='utf-8') as fichier :
        fichier.write(f"{ENTETE}\n\n\n")
        fichier.write(f"Objet : {OBJET}\n\n")
        nomcomplet=e[0]+" "+e[1]
        password= mdp(e[1],e[0])
        fichier.write(TEXTE.format(name=nomcomplet,email=e[2],passw=password))

for e in etudiants:
    afficheLettre(e)
    genererLettre(e)
    print("-----------------------------------------------------")

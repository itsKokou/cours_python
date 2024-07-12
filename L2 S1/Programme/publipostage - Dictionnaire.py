ENTETE="OSC 2022"
OBJET="Stage"
TEXTE="Bonjour {name},\nSuite à votre candidature à OSC, vous avez été sélectionné pour faire les tests.\nVotre login est : {email} et votre mot de passe est {passw}.\nMerci"
etudiants=[
    {"prenom":"Toto","nom":"Sy","email":"toto@exemple.com"},
    {"prenom":"Tata","nom":"Sow","email":"tata@exemple.com"},
    {"prenom":"Momo","nom":"Sambou","email":"momo@exemple.com"},
    {"prenom":"Mount","nom":"Goat","email":"mount@exemple.com"}
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
    #nomcomplet=e["prenom"]+" "+e["nom"]
    nomcomplet=e.get("prenom")+" "+e.get("nom")
    password= mdp(e.get("nom"),e.get("prenom"))
    print(TEXTE.format(name=nomcomplet,email=e.get("email"),passw=password))
def genererLettre(e):
    """Cette fonction permet de générer un fichier texte contenant la lettre de l'etudiant"""
    with open(f"{e.get('email')}.txt","w",encoding='utf-8') as fichier :
        fichier.write(f"{ENTETE}\n\n\n")
        fichier.write(f"Objet : {OBJET}\n\n")
        nomcomplet=e.get("prenom")+" "+e.get("nom")
        password= mdp(e.get("prenom"),e.get("nom"))
        fichier.write(TEXTE.format(name=nomcomplet,email=e.get("email"),passw=password))

for e in etudiants:
    afficheLettre(e)
    genererLettre(e)
    print("-----------------------------------------------------")

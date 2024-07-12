# 1. Creation de la methode __init__ :
#     Cette methode est appelee a chaque fois qu'on creer une instance d'une classe

# REMARQUE:
#   le mot clef SELF est requis si on veut avoir des attributs d'objet a initialiser


class Montre:
    # Attribut de classe:
    nbreMontre = 0

    # 1_ Attribut d'objet
    def __init__(self, marque, style, bracelet):
        Montre.nbreMontre += 1
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        # print("Appel de la methode init ...")


print(Montre.nbreMontre)

m1 = Montre("TAG Heuer", "Aiguille", "Cuivre")
m2 = Montre("Rolex", "Aiguille", "Cuir")
print(Montre.nbreMontre)
m3 = Montre("Casio", "Electronique", "Metal")


print(f"{m1.marque} - {m1.style} - {m1.bracelet}")
print(f"{m2.marque} - {m2.style} - {m2.bracelet}")
print(f"{m3.marque} - {m3.style} - {m3.bracelet}")


print(Montre.nbreMontre)
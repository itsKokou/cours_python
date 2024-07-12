# Ajouter une methode a la classe Montre (afficher heure) : sans le mot cle SELF
# Creer un objet puis appeler la methode (afficher heure)
#
#
#


class Montre:
    def __init__(self, marque, style, bracelet):
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        # print("Appel de la methode init ...")

    def printHour(self):
        print("10:20:20")


m1 = Montre("TAG Heuer", "Aiguille", "Cuivre")

# m1.printHour()

Montre.printHour(m1)

# Comment faire pour afficher les information d'un objet si on print l'objet
#
# SOLUTION :
# La methode __str__ :
#   Elle permet de representer l'objet par une chaine de caractere


class Montre:
    nbreMontre = 0

    def __init__(self, marque, style, bracelet):
        Montre.nbreMontre += 1
        self.marque = marque
        self.style = style
        self.bracelet = bracelet

    @classmethod
    def creerRolex(clss):
        return clss("Rolex", "Aiguille", "Cuir")

    @classmethod
    def creerTagHeuer(clss):
        return clss("TAG Heuer", "Electronique", "Metal")

    @staticmethod
    def afficherNombre():
        print(f"Le nombre de montre est : {Montre.nbreMontre}")

    @staticmethod
    def printHour():
        from datetime import datetime

        date = datetime.now()
        print(date.strftime("%H:%M:%S"))

    def __str__(self):
        return f"<Objet : {self.marque} - {self.style} {self.bracelet}>"


mr1 = Montre("Rolex", "Aiguille", "Cuir")
mr2 = Montre("Rodslkfjdslklex", "Aildskfjguille", "Cldksjfuir")

print(mr1)
print(mr2)

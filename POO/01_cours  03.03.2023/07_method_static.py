# 1) Creer une methode qui permet d'afficher les detail
# sur le nombre de montre cree :
#       le nombre de montre cree est : ...

# SOLUTION:
#     les methodes statique:
#     Methode qui n'a pas besoin de paramtre : ni de self ni class
#     Ce sont les méthodes statiques, qui ne prennent
#     pas d’instance d’objet (self) ou de classe (clss),
#     ce qui signifie qu’elles ne peuvent pas accéder à leurs états.
#     Mais elles sont liées à la classe.
#         des methodes avec le decorateur : @staticmethod


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


# mr1 = Montre("Rolex", "Aiguille", "Cuir")
# mr1 = Montre.creerRolex()


Montre.printHour()

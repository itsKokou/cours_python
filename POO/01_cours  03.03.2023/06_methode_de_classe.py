# 1. On suppose que l'entreprise vend le plus souvent des :
#   - Rolex a aiguille en cuir
#   - TAG Heuer Electonique en metal.
#   Proposer une solution rapide pour creer ces type de montre
#
#   SOLUTION :
#       Les methodes de classe:
#           des methodes avec le decorateur : @classmethod


class Montre:
    def __init__(self, marque, style, bracelet):
        self.marque = marque
        self.style = style
        self.bracelet = bracelet

    @classmethod
    def creerRolex(clss):
        return clss("Rolex", "Aiguille", "Cuir")

    @classmethod
    def creerTagHeuer(clss):
        return clss("TAG Heuer", "Electronique", "Metal")


# mr1 = Montre("Rolex", "Aiguille", "Cuir")
mr1 = Montre.creerRolex()
mr2 = Montre.creerTagHeuer()
mr3 = Montre("Casion", "Aiguille", "Cuir")

print(f"{mr1.marque} - {mr1.style} - {mr1.bracelet}")
print(f"{mr2.marque} - {mr2.style} - {mr2.bracelet}")

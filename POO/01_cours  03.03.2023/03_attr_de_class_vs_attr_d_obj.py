# 1. Creer deux instances de la classe Montre
# 2. Modifier la marque de la classe a partir de la classe Montre
# 3. Modifier la marque de la classe a partir de l'instance

# REMARQUE:
#   Le changement de valeur d'un attribut d'une classe affecte toutes instances de cette classe


class Montre:
    marque = "Hublot"
    style = "Aiguille"
    bracelet = "Metalique"


# 1_
m1 = Montre()
m2 = Montre()
print(m1.marque)
print(m2.marque)
print("---------------------")
# 2_
Montre.marque = "TAG Heuer"
print(Montre.marque)
print(m1.marque)
print(m2.marque)
print("---------------------")
# 3_
m1.marque = "Rolex"
print(Montre.marque)
print(m1.marque)
print(m2.marque)
print("---------------------")

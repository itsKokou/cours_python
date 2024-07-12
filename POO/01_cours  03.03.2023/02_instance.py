# 1. Creer une instance de la classe Montre
# 2. Afficher l'instance ????????
# 3. Afficher la marque de l'instance
# 4. Creer une seconde instance de la classe Montre


# REMARQUE :
#   les instances de la classe Montre ont les memes valeurs des attributs
#
class Montre:
    marque = "Hublot"
    style = "Aiguille"
    bracelet = "Metalique"


# 1_
m1 = Montre()
# 2_
print(m1)
print("----------------------")
# 3_
print(m1.marque)
# 4_
m2 = Montre()
print("----------------------")
print(m1)
print(m2)
print(m2.marque)

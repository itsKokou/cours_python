# l = list()
# l.append(4)
# l.extend([2, 3, 4, 5])
# print(l)
# l.remove(2)

# print(l)
#
#
#


class BreukhListe(list):
    def ajouter(self, element):
        super().append(element)

    def etendre(self, l):
        super().extend(l)


l = BreukhListe()
l.ajouter(4)
l.etendre([2, 3, 4, 5])
print(l)
l.remove(2)

print(l)

# l.ajouter(4)
# l.etendre([2, 3, 4, 5])
# l.supprimer(2)

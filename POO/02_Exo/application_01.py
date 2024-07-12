

from email.errors import MalformedHeaderDefect
from typing import List

class Animal:
    nom = '???'
    def crier(self):
        return "???"

class Mouton(Animal):
    nom  = 'Monton'
    def beler(self):
        return 'MBééééééééééé...'

    def crier(self):
        return super().crier() +' '+ self.beler()

class Coq(Animal):
    nom  = 'Coq'
    def chanter(self):
        return "Cocoricoooooo..."


a = Animal()
print(a.crier())
print(a.nom)

m = Mouton()
print(m.crier())
print(m.nom)
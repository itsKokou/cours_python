#        DEVOIR 
# Un produit est caracterisé :
#     - id
#     - libelle
#     - prix
#     - quantite
#     - categorie
#     - date de peremption

# Une categorie est caracterisée par :
#     - libelle
#     - id

# Un catalogue est caracterisé  par:
#     - son nom
#     - ses produits
# Un produit peut etre dans plusieurs categories
# Dans une categorie on peut avoir plusieurs produits
# Un produit peut ne pas avoir de date de peremption

# QUESTIONS :
#     proposer les fonctionnalites suivantes:
#     - Ajout de nouveau produit au catalogue
#     - Afficher le catalogue
#     - Trier les produit par categorie
#     - Afficher les produit d'une categorie donné
#     - Mettre a jour un produit.

#                  RESOLUTION

class Categorie : 
    def __init__(self,id:int, libelle:str):
        self.id = id 
        self.libelle = libelle

class Produit : 
    def __init__(self,id:int, libelle:str, prix:float, quantite:int, categorie : list, dateDePeremption=None):
        self.id = id 
        self.libelle = libelle
        self.prix = prix
        self.quantite = quantite
        self.categorie = categorie
        self.dateDePeremption = dateDePeremption

    def affiche (self):
        print(f"Nom : {self.libelle}")
        print(f"Prix : {self.prix}")
        print(f"Quantité : {self.quantite}")
        if self.dateDePeremption != None :
            print(f"Date de Péremption : {self.dateDePeremption}")

    def TrierProduit (self, categorie : Categorie):
        if categorie in self.categorie : 
            self.affiche()  

    def update(self,prix:float,quantite:int,dateDePeremption:str) :
        self.prix = prix
        self.quantite = quantite
        self.dateDePeremption = dateDePeremption
        

class Catalogue : 
    def __init__(self,nom:str, produits:list):
        self.nom = nom
        self.produits = produits

    def addProduct (self, produit : Produit )-> bool:
        if not isinstance(produit, Produit):
            raise ValueError(f"Attention : il faut entrer un produit !!!")

        if produit in self.produits:
            print("Ce produit existe deja.")
            return False

        self.produits.append(produit)
        return True
    
    def afficheCatalogue (self):
        print(f"Nom : {self.nom}")
        print(f"Les produits : ")
        print("-----------------------------")
        for prod in self.produits :
            prod.affiche() 
            print("-----------------------------")
    
    def afficherProduitByCategorie(self,categorie: Categorie):
        print(f"Les produits de la categorie {categorie.libelle} : ")
        for prod in self.produits :
          prod.TrierProduit(categorie)
          print("-----------------------------")  

     


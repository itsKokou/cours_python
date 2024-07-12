from datetime import datetime
import sqlite3
from config import DB_DIR


class CompteBancaire :
    numeroCompte = 0
    nom = ""
    prenom = ""
    adresse =""
    email =""
    telephone =""
    solde = 0
    date = datetime.now().strftime("%d/%m/%Y")
    heure = datetime.now().strftime("%H:%M:%S")

    def __init__(self,nom :str,prenom : str,email: str,tel: str):
        CompteBancaire.numeroCompte += 1
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.email = email
        self.telephone = tel

    def getNumeroCompte(self)-> int:
        return self.numeroCompte
    
    def getNom(self)-> str:
        return self.nom
    
    def getPrenom(self)-> str:
        return self.prenom
    
    def getTelephone(self)-> str:
        return self.telephone
    
    def getSolde(self)-> int:
        return self.solde
    
    def getAdresse(self)-> str:
        return self.adresse
    
    def getEmail(self)-> str:
        return self.email
    
    def getDate(self)-> str:
        return self.date
    
    def getHeure(self)-> str:
        return self.heure
    
    def setAdresse(self,adr : str):
        if isinstance(adr,str):
            self.adresse = adr
            return True
        else :
            print("L'adresse doit être une chaine")
            return False

    def Versement(self, montant : float) :
        if montant <=0 :
            print("Entrez un montant supérieur à zéro")
            return False
        else :
            self.solde += montant
            print(f"Vous venez d'effectuer un versement de {montant} Francs. A Bientôt !")
            return True
   
    def Retrait(self, montant : float) :
        if montant <=0 :
            print("Entrez un montant supérieur à zéro")
            return False
        elif montant >= self.solde :
            print("Vous n'avez pas suffisamment de fond pour effectuer cette opération.")
            return False
        else :
            self.solde -= montant
            print(f"Vous venez d'effectuer un retrait de {montant} Francs. A Bientôt !")
            return True

    def Taxe(self):
        print(f"Votre taxe à payer est de {self.solde*0.02} Francs.")

    def afficher(self):
        print(f"Numéro de Compte : {self.numeroCompte}")
        print(f"Solde du Compte : {self.solde}")
        print(f"Date de création du Compte : {self.date}")
        print(f"Heure de création du Compte : {self.heure}")
        print(f"Propriétaire du Compte : {self.nom} {self.prenom}")
        print(f"Adresse du propriétaire : {self.adresse}")
        print(f"Téléphone du propriétaire : {self.telephone}")
        print(f"Email du propriétaire : {self.email}")

    def save(self):
        conn = sqlite3.connect(f"{DB_DIR}base.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS compte(numero number, nom text, prenom text, adresse text, email text, telephone text, solde real, date text, heure text)")
        data = {"a":self.numeroCompte,"b":self.nom,"c":self.prenom,"d":self.adresse,"e":self.email,"f":self.telephone,"g":self.solde,"h":self.date,"i":self.heure}
        c.execute("""
            INSERT INTO compte(numero,nom,prenom,adresse,email,telephone,solde,date,heure)
            VALUES(:a,:b,:c,:d,:e,:f,:g,:h,:i)
        """, data)
        conn.commit()
        conn.close()

    def setAdresseDB(self,adresse):
        if self.setAdresse(adresse) == True :
            conn = sqlite3.connect(f"{DB_DIR}base.db")
            c = conn.cursor()
            c.execute(f""" UPDATE compte SET adresse = "{adresse}"  WHERE compte.numero = {self.numeroCompte}""")
            conn.commit()
            conn.close()

    def VersementDB(self,montant):
        if self.Versement(montant)== True :
            conn = sqlite3.connect(f"{DB_DIR}base.db")
            c = conn.cursor()
            c.execute(f""" UPDATE compte SET solde = {self.solde}  WHERE compte.numero = {self.numeroCompte}""")
            conn.commit()
            conn.close()

    def RetraitDB(self,montant):
        if self.Retrait(montant)== True :
            conn = sqlite3.connect(f"{DB_DIR}base.db")
            c = conn.cursor()
            c.execute(f""" UPDATE compte SET solde ={self.solde}  WHERE compte.numero = {self.numeroCompte}""")
            conn.commit()
            conn.close()
    
    @staticmethod
    def liste():
        conn = sqlite3.connect(f"{DB_DIR}base.db")
        c = conn.cursor()
        c.execute("SELECT * FROM compte")
        data = c.fetchall()
        print(data)
        conn.close()
  
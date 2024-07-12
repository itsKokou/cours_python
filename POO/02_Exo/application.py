import os
from config import DB_DIR, CURRENT_DIR
import json

from json import JSONEncoder


class Contact:
    #
    def __init__(self, name: str, phoneNumbers: list):
        self.name = name
        self.phoneNumbers = phoneNumbers

    def details(self):
        print(f"NOM : {self.name}")
        print("Telephone(s) : ")
        print("---------------")
        for phone in self.phoneNumbers:
            print(f"- {phone}")

    def addNew(self, phoneNumber: str) -> bool:
        if not isinstance(phoneNumber, str):
            # print(f"Attention : '{phoneNumber}' doit etre une chaine!!!")
            # return False
            raise ValueError(f"Attention : '{phoneNumber}' doit etre une chaine!!!")

        if phoneNumber in self.phoneNumbers:
            print(f"{phoneNumber} existe deja.")
            return False

        self.phoneNumbers.append(phoneNumber)
        return True

    def removePhoneNumber(self, phoneNumberToRemove: str) -> bool:
        if phoneNumberToRemove in self.phoneNumbers:
            self.phoneNumbers.remove(phoneNumberToRemove)
            return True
        return False


class Repertoire(list):
    def __init__(self, name):
        self.name = name

    #
    def addContact(self, contactToAdd: Contact) -> bool:
        if not isinstance(contactToAdd, Contact):
            raise ValueError("Vous devez ajouter un contact pas autre chose!!!")
        for c in self:
            if c.name == contactToAdd.name:
                print(f"Ce contact existe deja!!!")
                return False
        self.append(contactToAdd)
        return True

    def printRepertoire(self):
        print(f"LES CONTACTS ({self.name}) : ")
        print("------------------------------")
        for c in self:
            conc = Contact(c["name"], c["phoneNumbers"])
            line = f"{conc.name}          {conc.phoneNumbers[0]}"
            if len(conc.phoneNumbers) > 1:
                line = line + "..."
            # c.details()
            print(line)
            print("-----------------------------------------")

    def removeContact(self, contactName: str) -> bool:
        pass

    def save(self):
        dbPath = os.path.join(DB_DIR, f"Contacts_{self.name}.json")

        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)

        #
        with open(dbPath, "w") as f:
            f.write(
                json.dumps(self, default=lambda c: c.__dict__),
            )
            print(f"Tous les contacts du repertoire '{self.name}' sont enregistres.")
            return True
        return False

    def fetchAll(self):
        dbPath = os.path.join(DB_DIR, f"Contacts_{self.name}.json")
        with open(dbPath, "r") as f:
            db_contacts = json.loads(f.readline())
            self.extend(db_contacts)


# c = Contact("Toto", ["77 145 45 45"])
# c1 = Contact("Tata", ["77 145 45 00", "77 876 65 54"])

r1 = Repertoire("Busness")
#
# r1.addContact(c)
# r1.addContact(c1)
# r1.printRepertoire()

# r1.save()
r1.fetchAll()
r1.printRepertoire()

###

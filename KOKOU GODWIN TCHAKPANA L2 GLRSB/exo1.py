montant=300000
achat=0
poidsT=0
achatT=0
age=input("Veillez saisir l'âge du cheval : ")
while age.isdigit()==False or int(age)<5 or int(age)>10 :
    age=input("Saisissez un entier positif entre 5 et 10 : ")
age=int(age)
if(age>=5 and age<7):
    capacite=100-15
else:
    capacite=200-15
ferrailles=[]
invalide=True
while invalide==True:
    type=input("Entrez le type du ferraille à ajouter dans la charette :").lower()
    while  ( type not in ["or","fer","bronze","cuivre"]):
        type=input("Choisissez entre: Or, Fer, Bronze et Cuivre : ").lower()
    if(type=="or"):
        prix=150000
    elif(type=="fer"):
        prix=75
    elif(type=="bronze"):
        prix=100
    elif(type=="cuivre"):
        prix=500
    cpt=True
    poids=input(f"Veillez entrer le kilo de {type} à acheter :")
    while cpt==True:
        cpt=False
        if(poids.replace(',','').replace('.','').isdigit()==False):
            poids=input("Saisissez une valeur entière ou décimal :")
        else:
            achat=prix*float(poids)
            if(achat>montant or float(poids) >capacite or achatT>montant or poidsT >capacite):
                poids=input("Entrez plus petit poids :")
                cpt= True
    poidsT+=float(poids)
    achatT+=prix*float(poids)
    list.append(ferrailles,{"type":type,"poids":float(poids),"prix": prix})
    if(achat>montant or poidsT>capacite):
        invalide=False
    else:
        invalide=True

with open("modou.txt",'w',encoding='UTF-8') as f:
    totaux=0
    f.write(f"""{'*'*50}\n""")
    f.write(f"""{'RECU':^50}\n""")
    f.write(f"""{'*'*50}\n\n""")
    f.write(f""" {"FERRAILLES":<15} """)
    f.write(f""" {"POIDS":<10} """)
    f.write(f""" {"PRIX U ":<10} """)
    f.write(f"""| {"PRIX TOTAL":<15} \n""")
    for i in range (len(ferrailles)):
        f.write(f""" {str(ferrailles[i].get('type')):<15} """)
        f.write(f""" {str(ferrailles[i].get('poids')):<10} """)
        f.write(f""" {str(ferrailles[i].get('prix')):<10} """)
        total=ferrailles[i].get('prix')*ferrailles[i].get('poids')
        totaux+=total
        f.write(f""" {str(total):<15} \n\n""")
    f.write(f"""{'*'*50}\n""")
    f.write(f""" NET A PAYER : {totaux} \n""")
    f.write(f"""{'*'*50}\n""")
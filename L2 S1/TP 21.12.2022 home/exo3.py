import json

liste=["suuuu",15,True,False,"Okay",12.5,False,18,13.8,18.9]

def ma_fonction(maliste:list):
    if type(maliste)!=list :
        return None
    chaine=""
    entier=0
    somReel=0
    nbreReel=0
    nbreTrue=0
    nbreFalse=0
    for i in maliste:
        if type(i)==str:
            chaine+=i
        if type(i)==int:
            entier+=i
        if type(i)==float:
            somReel+=i
            nbreReel+=1
        if type(i)==bool:
            if(i==True):
                nbreTrue+=1
            else:
                nbreFalse+=1
    reel=somReel/nbreReel
    booleen= (nbreTrue>nbreFalse)# condition si l'expression est vrai alors 
                                 #booleen prend la valeur True sinon False
    contenu={
        "chaine":chaine,
        "entier":entier,
        "reel":reel,
        "bool":booleen
    }
    with open("monjson.json","w") as f:
       json.dump(contenu,f,indent=4) 

ma_fonction(liste)
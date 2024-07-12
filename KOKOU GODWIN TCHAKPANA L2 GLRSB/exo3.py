l=['1','2','1','3','4','1','10','5','7','8','9','10']

def recherche_val(l:list,n:str):
    for i in range(len(l)):
        if (l[i]==n):
            return True
    return False

def nombre_valeur(maListe:list): 
    nbreUnique=0
    nbreRepete=0
    cpt=[]
    for i in maListe:
        if list.count(maListe,i)==1:
            nbreUnique+=1
        else : #list.count(maListe,i)>=2:
            if recherche_val(cpt,i)==False:
                nbreRepete+=1
                cpt.append(i)
    return (nbreUnique,nbreRepete,cpt)

print(nombre_valeur(l))

#print(recherche_val(['2','1','3'],'5'))
#Ecrire un programme qui permet de copier un fichier
#Le nom du fichier source est saisi au clavier mais le nom du fichier 
#destinataire est sous le format : nomfichiersource copie.ext
#la casse du contenu du fichier destinataire est inversée
from genericpath import isfile


nomfichiersource=input("Entrez le nom du fichier a copier : \n")
if (isfile(nomfichiersource)):
    if (nomfichiersource.find(".")!=-1):
        list=nomfichiersource.split('.')
        with open(nomfichiersource,"r",encoding='utf-8') as f:
            data=f.read()
        i=1
        n=len(list)
        nomfichiercopie=list[0]
        while(i<n-1):
            nomfichiercopie+="."+list[i]
            i+=1
        nomfichiercopie+=list[-1]
        with open(nomfichiercopie,'w',encoding="utf-8") as d:
            d.write(data)
else:
    print(f""""Le fichier "{nomfichiersource}"n'existe pas! """)
          
           
        
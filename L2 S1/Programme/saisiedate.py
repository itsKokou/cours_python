# Écrire un programme qui permet de saisie une date au format JJ/MM/AAAA. Le programme 
#affiche la date au format JJ-MM-AAAA.
#NB : chaque partie de la date doit être valide.

i=0
while (i==0):
    date=input("Entrez une date au format JJ/MM/AAAA :")
    x= date.split("/")
    mois=int(x[1])
    if(mois>=1 and mois<=12):
         if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
             nbre =31
         elif (mois==4 or mois==6 or mois==9 or mois==11):
             nbre=30
         else :
            if(mois%4==0 and mois%100!=0 or mois%400==0):
                nbre=29
            else:
                nbre =28
         j=int(x[0])
         an=int(x[2])
         if ((j>0 and j<=nbre) and an>0 ):
             print('-'.join(x))
             i=1
         else:
             print('date invalide !')
    else :
         print('date invalide !')
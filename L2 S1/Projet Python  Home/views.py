
from fonctions import clear_screen, connexion_json,load_users,save_users,update_users,load_films,update_films,save_films,date
from fonctions import find_all_client,find_client_by_id,reservations_encours,find_cinema_by_id,find_film_by_id,update_reservations,save_reservations
from fonctions import reservations_terminees_by_id_client,reservations_by_id_client,reservations_encours_by_id_client,load_reservations
import os
from constantes import TAILLE
import sys

def milieu(msg,motif='+',taille=100):
    reste=taille - len(msg)
    nbrech1=reste//2
    if(reste%2 == 1):
        nbrech2=nbrech1+1
    else:
        nbrech2=nbrech1
    print(f"{motif*taille}")
    print(f"{motif*nbrech1}{msg}{motif*nbrech2}")
    print(f"{motif*taille}")

def title(msg:str,taille=100,motif='+'):
    print(taille*motif)
    print(f"{msg:^{taille}}")#ecrire sur 70 char: > signifie en commençant à droite, < gauche et ^ au centre
    print(taille*motif)

def enter_login():
    login=input("LOGIN : ").strip()
    while login.isalnum() == False :
        login= input("LOGIN : ").strip()
    return login

def login_page():
    clear_screen()
    title('CONNEXION')
    print("Taper 0 pour créer un compte")
    login=enter_login()
    if(login=="0"):
        clear_screen()
        create_account(3)
        clear_screen()
        login_page()
    else:
        password=input("PASSWORD : ").strip()
        while connexion_json(login,password)==None :
            clear_screen()
            title('CONNEXION')
            print("Login ou mot de passe incorrect")
            login=enter_login()
            password=input("PASSWORD : ").strip()
    return connexion_json(login,password)

def enter_name( msg):
    nom = input(f"Entrez {msg}").strip()
    while nom.isalpha()==False or len(nom)<2 :
        nom = input(f"Entrez {msg}").strip()
    return nom 

def verify_login():
    users=load_users()
    cpt=0
    while cpt==0 :
        cpt=1
        login= input("Entrez votre login : ").strip()
        if(login.isalpha()==False):
            cpt=0
        else:
            for user in users:
                if(user.get("login")==login):
                    cpt=0
                    break 
    return login

def  verify_password():
    password = input("Entrez votre mot de passe : ").strip()
    while password.isspace() == True or len(password)<5 :
        password = input("Entrez votre mot de passe : ").strip()
    return password 

def create_account(role:int,msg=""):
    title(f"CREATION DE COMPTE {msg}")
    user={}
    users= load_users()
    user["id"]=users[-1].get('id')+1
    user["nom"]= enter_name("votre nom : ")
    user["prenom"]= enter_name("votre prenom : ")
    user["login"]= verify_login()
    user["password"]= verify_password()
    mdp=input("Confirmer votre mot de passe : ")
    while mdp!=user["password"] :
        print("Les mots de passe ne correspondent pas !!! ")
        mdp=input("Confirmer votre mot de passe : ")
    user["role"]=role
    user["etat"]=1
    validation=input("\nVoulez-vous confirmer la création du compte ?[ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    if(validation=='1'):
        save_users(user)
        print("\n\n       **** COMPTE CRÉE AVEC SUCCÈS !!! **** \n\n")
    else:
        print("\n\n       **** CREATION DE COMPTE ANNULÉE !!! **** \n\n")
    os.system('pause')

def entete(user:dict,motif:str,taille=100):
    clear_screen()
    print(motif*taille)
    if (user.get('role') == 1):
        tail = 100 -(7*2+len(user["login"])+5)
        print(f"{motif*3}  {user['login']}  {motif*tail}  ADMIN  {motif*3}")
    elif (user.get('role') == 2):
        tail = 100 -(7*2+len(user["login"])+8)
        print(f"{motif*3}  {user['login']}  {motif*tail}  CAISSIER  {motif*3}")
    else:
        tail = 100 -(7*2+len(user["login"])+6)
        print(f"{motif*3}  {user['login']}  {motif*tail}  CLIENT  {motif*3}")
    print(motif*taille)
    



####################################################### ADMINISTRATEUR ########################################################################


def menu_admin():
    print("1........................CREER UN COMPTE")
    print("2........................AJOUTER UN FILM")
    print("3........................AJOUTER DES CINEMAS")
    print("4........................MODIFIER DES CINEMAS")
    print("5........................VOIR LA LISTE DES FILMS")
    print("6........................VOIR LA LISTE DES CLIENTS")
    print("7........................BLOQUER OU DEBLOQUER UN UTILISATEUR")
    print("8........................QUITTER \n")
    choix = input("Faites votre choix : \n")
    while choix.isdigit()==False or int(choix)>7 or int(choix) <1:
        choix = input("Faites votre choix : \n")
    return int(choix)


#================== USERS =============

def afficher_client():
    usersClient=find_all_client()
    print('-'*TAILLE)
    print(f"""{'POSITION':<15}{'PRENOM(S)':<30}{'NOM':<20}{'LOGIN':<20}{'ETAT':<15}""")
    print('-'*TAILLE)
    n=len(usersClient)
    for i in range(n):
        if (usersClient[i].get("etat")==1):
            etat="Actif"
        else :
            etat="Suspendu"
        print(f"""{i:<15}{usersClient[i].get('prenom'):<30}{usersClient[i].get('nom'):<20}{usersClient[i].get('login'):<20}{etat:<15}""")
        print('-'*TAILLE)

def afficher_user(users:list):
    print('-'*TAILLE)
    print(f"""{'POSITION':<10}{'ID':<10}{'PRENOM(S)':<20}{'NOM':<15}{'LOGIN':<15}{'ROLE':<15}{'ETAT':<15}""")
    print('-'*TAILLE)
    n=len(users)
    for i in range(n):
        if (users[i].get("etat")==1):
            etat="ACTIF"
        else :
            etat="SUSPENDU"
        if (users[i].get("role")==1):
            role="ADMIN"
        elif (users[i].get("role")==2) :
            role="CAISSIER"
        else:
            role="CLIENT"
        print(f"""{i:<10}{users[i].get('id'):<10}{users[i].get('prenom'):<20}{users[i].get('nom'):<15}{users[i].get('login'):<15}{role:<15}{etat:<15}""")
        print('-'*TAILLE)

def details_user(usersList:list,p):
    clear_screen()
    msg="Details de l'utilisateur:"
    print(f"""{msg}{'-'*(TAILLE-len(msg))}""")
    print(f"""{f"PRENOM : {usersList[p].get('prenom')}":^{TAILLE}}""")
    print(f"""{f"NOM : {usersList[p].get('nom')}":^{TAILLE}}""")
    print(f"""{f"LOGIN : {usersList[p].get('login')}":^{TAILLE}}""")
    if (usersList[p].get("etat")==1):
        etat="ACTIF"
    else :
        etat="SUSPENDU"
    if (usersList[p].get("role")==1):
        role="ADMIN"
    elif (usersList[p].get("role")==2) :
        role="CAISSIER"
    else:
        role="CLIENT"
    print(f"""{f"ROLE : {role}":^{TAILLE}}""")
    print(f"""{f"ETAT : {etat}":^{TAILLE}}""")
    print('-'*TAILLE)
    

def bloquer_user(usersList:list):
    n=len(usersList)
    p='-1'
    while (p.isdigit()==False or (int(p)<0 or int(p)>=n)):
        p=input("Entrez la POSITION de l'utilisateur à SUSPENDRE : \n")
    if (usersList[int(p)].get('etat')==0):
        clear_screen()
        print("\n\n     CET UTILISATEUR EST DÉJÀ SUSPENDU !!!\n\n")
    else:
        details_user(usersList,int(p))
        choix="2"
        while (choix.isdigit()==False or (int(choix)!=0 and int(choix)!=1)):
            choix=input("Confirmer la suspension ? [1 => OUI / 0 => NON] \n")
        if (choix=='1'):
            usersList[int(p)]['etat']=0
            update_users(usersList)
            clear_screen()
            print("\n\n     UTILISATEUR BLOQUÉ AVEC SUCCÈS !!!\n\n")
        else:
            print("\n\n      SUSPENSION D'UTILISATEUR ANNULÉE !!!\n\n")


def debloquer_user(usersList:list):
    n=len(usersList)
    p='-1'
    while (p.isdigit()==False or (int(p)<0 or int(p)>=n)):
        p=input("Entrez la POSITION de l'utilisateur à RESTITUER : \n")
    if (usersList[int(p)].get('etat')==1):
        clear_screen()
        print("\n\n     CET UTILISATEUR EST DÉJÀ ACTIF !!!\n\n")
    else:
        details_user(usersList,int(p))
        choix="2"
        while (choix.isdigit()==False or (int(choix)!=0 and int(choix)!=1)):
            choix=input("Confirmer la restitution ? [1 => OUI / 0 => NON] \n")
        if (choix=='1'):
            usersList[int(p)]['etat']=1
            update_users(usersList)
            clear_screen()
            print("\n\n     UTILISATEUR RESTITUÉ AVEC SUCCÈS !!!\n\n")
        else:
            print("\n\n      RESTITUTION D'UTILISATEUR ANNULÉE !!!\n\n")


#===============   FILMS ===================

def afficher_film(films:list):
    print('-'*TAILLE)
    print(f"""{'POSITION':<10}{'TITRE':<20}{'GENRE':<20}{'DUREE':<15}{'ANNEE DE PROD':<20}{'DATE DE SORTIE':<15}""")
    print('-'*TAILLE)
    n=len(films)
    for i in range(n):
        print(f"""{i:<10}{films[i].get('titre'):<20}{films[i].get('genre'):<20}{films[i].get('duree'):<15}{films[i].get('annee_de_production'):<20}{films[i].get('date_de_sortie'):<15}""")
        print('-'*TAILLE)

def recherche_film(titre:str):
    films=load_films()
    for film in films :
        if (film.get("titre")==titre):
            return film
    return False

def saisir_titre():
    cpt=0
    while cpt==0 :
        cpt=1
        titre= input("Entrez le titre du film : \n").strip()
        titreList=titre.split(" ")
        for i in titreList:
            if(i.isalpha()==False):
                cpt=0
                break
        if (recherche_film(titre.upper())!=False):
            cpt=0       
    return titre

def saisir_date_de_sortie(annee:str):
    cpt=0
    while cpt== 0 :
        cpt=1
        date=input("Entrez la date de sortie du film sous format [JJ/MM/AAAAA] : \n").strip()
        dd=date.split('/')
        for i in dd :
            if i.isdigit()==False or len(dd[0])!=2 or len(dd[1])!=2 or len(dd[2])!=4 :
                cpt=0
                break
            elif int(dd[2]) < int(annee):
                print("L'année de sortie ne peut être antérieure à l'année de production !")
                cpt=0
                break
            elif int(dd[0])<=0 or int(dd[0])>31 or int(dd[1])<=0 or int(dd[1])>12 :
                print("La date saisie n'est pas correcte !!!")
                cpt=0
                break
    return date 


def saisir_duree():
    cpt=0
    while cpt== 0 :
        cpt=1
        duree=input("Entrez la durée du film en minutes : \n").strip()
        if(duree.isdigit()==False):
            cpt=0
            break
        elif int(duree)>=240:
            cpt=0
            break
        else:
            n=int(duree)
            x=0
            while n>=60 :
                x=x+1
                n=n-60
            return f"{x}h {n}min"


def ajouter_film():
    title("AJOUT DE FILM")
    films= load_films()
    film={}
    film["id"]=films[-1].get('id')+1
    film["titre"]=saisir_titre()
    film["synopsis"]=input("Entrez le synopsis du film :\n").strip()
    film["genre"]= enter_name("le genre du film :\n")
    film["annee_de_production"]=input("Entrez l'année de production du film :\n").strip()
    while (film["annee_de_production"].isdigit()==False or int(film["annee_de_production"])>2023 or int(film["annee_de_production"])<1950):
        film["annee_de_production"]=input("Entrez l'année de production du film :\n").strip()

    film["date_de_sortie"]= saisir_date_de_sortie(film["annee_de_production"])
    film["duree"]=saisir_duree()
    film["cinemas"]=[]
    validation=input("\nVoulez-vous confirmer l'ajout du film ?[ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    if(validation=='1'):
        save_films(film)
        print("\n\n       **** FILM AJOUTÉ AVEC SUCCÈS !!! **** \n\n")
    else:
        print("\n\n       **** AJOUT DE FILM ANNULÉ !!! **** \n\n")
    os.system('pause')


def details_films(films:list,p):
    clear_screen()
    msg="Details du film:"
    print(f"""{msg}{'-'*(TAILLE-len(msg))}""")
    print(f"""{"TITRE : ":>50}{films[p].get('titre')}""")
    print(f"""{"GENRE : ":>50}{films[p].get('genre')}""")
    print(f"""{"DURÉE : ":>50}{films[p].get('duree')}""")
    print(f"""{"ANNÉE DE PRODUCTION : ":>50}{films[p].get('annee_de_production')}""")
    print(f"""{"DATE DE SORTIE : ":>50}{films[p].get('date_de_sortie')}""")
    print(f"""{"SYNOPSIS : ":>50}""")
    n=len(films[p].get('synopsis'))
    i=0
    while i<n:
        print(f"""{"":>42}{films[p].get('synopsis')[i:i+55]:}""")
        i=i+55
    print(f"""\n{"CINEMAS : ":>50}""")
    if (films[p].get('cinemas')==[]):
        print(f"""{"":>50}{"AUCUN PROGRAMME DE DIFFUSION"}""")
    else :
        for cine in films[p].get('cinemas'):
            print(f"""{"NOM : ":>60}{cine.get('nom')}""")
            print(f"""{"SALLE : ":>60}{cine.get('salle')}""")
            print(f"""{"PRIX : ":>60}{cine.get('prix')}""")
            print(f"""{"DATE : ":>60}{cine.get('horaire').get('jour')}""")
            print(f"""{"HORAIRE : ":>60}{cine.get('horaire').get('temps')}""")
            print(f"""{"PLACES RESTANT : ":>60}{cine.get('nbreplace')}\n""")
    print('-'*TAILLE)
    

#============= Cinema ==============

def saisir_nom_cine(msg=""):
    cpt=0
    while cpt==0 :
        cpt=1
        nom= input(f"Entrez le nom du Cinéma {msg}: \n").strip()
        nomList=nom.split(" ")
        for i in nomList:
            if(i.isalpha()==False):
                cpt=0
                break
    return nom

def saisir_int(msg:str,fin:int,debut=0):
    n=input(f"{msg}\n")
    while (n.isdigit()==False or int(n)<=debut or int(n)>fin):
        n=input(f"{msg}\n")
    return int(n)

def saisir_date():
    cpt=0
    while cpt== 0 :
        cpt=1
        date=input("Entrez la date de projection du film [JJ/MM] : \n").strip()
        dd=date.split('/')
        for i in dd :
            if i.isdigit()==False or len(dd[0])!=2 or len(dd[1])!=2 :
                cpt=0
                break
            elif int(dd[0])==0 or int(dd[0])>31 or int(dd[1])==0 or int(dd[1])>12 :
                print("La date saisie n'est pas correcte !!!")
                cpt=0
                break
    return f"{date}/2023" 

def calcul_temps(film:dict):
    cpt=0
    while cpt==0:
        cpt=1
        debut=input("Entrez l'heure de début de la projection sous format [00h 00]: \n")
        dd=debut.replace("h","").split(" ")
        if (dd[0].isdigit==False or dd[1].isdigit==False or len(dd[0])!=2 or len(dd[1])!=2):
            cpt=0
        elif(int(dd[0])>=24 or int(dd[1])>=60):
            cpt=0
        else:
            hh=film["duree"].replace("min","").split("h ")
            heure=int(dd[0])*60+int(dd[1])+ int(hh[0])*60+int(hh[1])
            div=heure//60
            rest=heure%60
            if(div>=24):
                div=div-24
    return f"{debut} - {str(div).zfill(2)}h {str(rest).zfill(2)}"

def details_cinema(cinema):
    clear_screen()
    msg="Details du cinema:"
    print(f"""{msg}{'-'*(TAILLE-len(msg))}""")
    print(f"""{"NOM : ":>60}{cinema.get('nom')}""")
    print(f"""{"SALLE : ":>60}{cinema.get('salle')}""")
    print(f"""{"PRIX : ":>60}{cinema.get('prix')}""")
    print(f"""{"DATE : ":>60}{cinema.get('horaire').get('jour')}""")
    print(f"""{"HORAIRE : ":>60}{cinema.get('horaire').get('temps')}""")
    print(f"""{"PLACES RESTANT : ":>60}{cinema.get('nbreplace')}\n""")
    print('-'*TAILLE)


def modifier_cinema(films):
    choix='-1'
    while ((choix.isdigit()==False) or ((int(choix)<0 or int(choix)>=len(films)))) :
        print("Pour quel film souhaitez-vous modifier le cinéma ?")
        choix=input("Entrez la POSITION : \n")
    p=int(choix)
    details_films(films,p)
    if(len(films[p].get("cinemas"))==1):
        cine=films[p].get("cinemas")[0]
    else:
        cpt=0
        while cpt==0 :
            cpt=1
            cineNom=saisir_nom_cine("choisi ").lower()
            for cinema in films[p].get("cinemas"):
                if(cinema.get("nom").lower() == cineNom):
                    cine=cinema
                    break
                else: 
                    cpt=0
    details_cinema(cine)
    cinema={}
    cinema["id"]= cine.get('id')
    cinema["nom"]=cine.get('nom')
    cinema["salle"]=saisir_int("Entrez le numéro de la nouvelle Salle : ",10)
    cinema["nbreplace"]=saisir_int("Entrez le nombre de place de la salle : ",500)
    cinema["prix"]=saisir_int("Entrez le prix unitaire d'une place : ",13000,2499)
    cinema["horaire"]={}
    cinema["horaire"]["jour"]= saisir_date()
    cinema["horaire"]["temps"]=calcul_temps(films[p])
    
    validation=input("\nVoulez-vous confirmer la modification du cinema ?[ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    if(validation=='1'):
        for c in films[p].get("cinemas"):
            if (c.get("id")==cine.get('id')):
                if(c == cinema):
                    print("\n\n           *** VOUS N'AVEZ FAIT AUCUNE MODIFICATION !!! ***\n\n ")
                    break
                else:
                    films[p]["cinemas"][cine.get('id')-1] = cinema
                    update_films(films)
                    print("\n\n       **** CINÉMA MODIFIÉ AVEC SUCCÈS !!! **** \n\n")
                    break
    else:
        print("\n\n       **** MODIFICATION DE CINÉMA ANNULÉ !!! **** \n\n")
    os.system('pause')

def ajouter_cinema():
    films=load_films()
    cinema={}
    choix='-1'
    while ((choix.isdigit()==False) or ((int(choix)<0 or int(choix)>=len(films)))) :
        print("À Quel film souhaitez-vous ajouter de cinéma ?")
        choix=input("Entrez la POSITION : \n")
    p=int(choix)
    details_films(films,p)
    cinema["id_cine"]=len(films[p]["cinemas"])+1
    cinema["nom"]=saisir_nom_cine()
    cinema["salle"]=saisir_int("Entrez le numéro de Salle : ",10)
    cinema["nbreplace"]=saisir_int("Entrez le nombre de place de la salle : ",400)
    cinema["prix"]=saisir_int("Entrez le prix unitaire d'une place : ",13000,2499)
    cinema["horaire"]={}
    cinema["horaire"]["jour"]= saisir_date()
    cinema["horaire"]["temps"]=calcul_temps(films[p])
    validation=input("\nVoulez-vous confirmer l'ajout du cinema ?[ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    cpt=1
    if(validation=='1'):
        for c in films[p].get("cinemas"):
            if (c.get("nom").lower() == cinema.get("nom").lower() and c.get("salle") == cinema.get("salle") and c.get("nbreplace") == cinema.get("nbreplace") and c.get("prix") == cinema.get("prix") and c.get("horaire") == cinema.get("horaire")):
                cpt=0
                print("\n\n           *** CE CINÉMA EXISTE DÉJÀ !!! ***\n\n ")
                break
        if(cpt==1):
            films[p]["cinemas"].append(cinema)
            update_films(films)
            print("\n\n       **** CINÉMA AJOUTÉ AVEC SUCCÈS !!! **** \n\n")
    else:
        print("\n\n       **** AJOUT DE CINÉMA ANNULÉ !!! **** \n\n")
    os.system('pause')
   


def fonction_admin(user:dict):
    clear_screen()
    entete(user,'*') 
    print(f"{'-'*TAILLE}")
    milieu("MENU GENERAL")
    print("\n")
    choice = menu_admin()
    match choice :
        case 1:
            choix=input("Quel type de compte souhaitez-vous créer ? [1 => ADMIN / 2 => CAISSIER]\n")
            while choix.isdigit()==False or int(choix)>2 or int(choix) <1:
                choix = input("Faites votre choix : [ 1 => ADMIN / 2 => CAISSIER ] \n")
            clear_screen()
            entete(user,'*') 
            print(f"{'-'*TAILLE}")
            if(choix=='1'):
                msg="ADMIN"
            else:
                msg="CAISSIER"
            create_account(int(choix),msg); #pause est dedans
            fonction_admin(user)
        case 2:
            clear_screen()
            ajouter_film()
            fonction_admin(user)
        case 3:
            clear_screen()
            entete(user,'*')
            films=load_films() 
            afficher_film(films)
            milieu("AJOUT DE CINEMA")
            print("")
            ajouter_cinema()
            fonction_admin(user)
        case 4:
            clear_screen()
            entete(user,'*')
            films=load_films()
            afficher_film(films)
            milieu("MODIFICATION DE CINEMA")
            print("")
            modifier_cinema(films)
            fonction_admin(user)
        case 5:
            clear_screen()
            entete(user,'*') 
            films=load_films()
            afficher_film(films)
            milieu("LISTE DES FILMS")
            print("")
            n=len(films)
            cpt=0
            while cpt==0 :
                choix=input("Entrez la POSITION d'un film pour voir les details [ -1 pour quitter ] :\n")
                cpt=1
                if(choix=="-1"):
                    pass
                elif choix.isdigit()==False or int(choix)>=n:
                    cpt=0
            if(choix=="-1"):
               pass
            else :
                details_films(films,int(choix))
            print()
            os.system('pause')
            fonction_admin(user)
        case 6:
            clear_screen()
            entete(user,'*') 
            afficher_client()
            milieu("LISTE DES CLIENTS")
            print("\n")
            os.system('pause')
            fonction_admin(user)
        case 7:
            clear_screen()
            entete(user,'*')
            users=load_users() # liste est là
            afficher_user(users)
            milieu("LISTE DES UTILISATEURS")
            print("\n")
            choix='0'
            while (choix.isdigit()==False or (int(choix)!=1 and int(choix)!=2)) :
                choix=input("Que voulez-vous faire ?[ 1 => BLOQUER / 2 => DEBLOQUER ] \n")
            if(choix=='1'):
                bloquer_user(users)
            else:
                debloquer_user(users)
            os.system('pause')
            fonction_admin(user)
        case other:
            print("\nFermeture...")
            os.system('pause')
            sys.exit("Bye !")
    


##################################################### FIN ADMINISTRATEUR ################################################################



####################################################### CAISSIER ########################################################################


def menu_caissier():
    print("1........................VALIDER UNE RESERVATION CLIENT")
    print("2........................GENERER UN TICKET D'UN CLIENT")
    print("3........................QUITTER \n")
    choix = input("Faites votre choix : \n")
    while choix.isdigit()==False or int(choix)>3 or int(choix) <1:
        choix = input("Faites votre choix : \n")
    return int(choix)

def etat_de_reservation(etat:int):
    if (etat==0):
        msg="EN COURS"
    elif (etat==1):
        msg="TERMINÉE"
    else:
        msg="ANNULÉE"
    return msg

def afficher_reservations(reservations:list):
    print('-'*TAILLE)
    print(f"""{'POSITION':<10}{'FILM':<17}{'CLIENT':<15}{'CINEMA':<20}{'SALLE':<8}{'PLACES':<8}{'DATE':<12}{'STATUT':<10}""")
    print('-'*TAILLE)
    n=len(reservations)
    for i in range(n):
        film=find_film_by_id(reservations[i].get('film_id'))
        client=find_client_by_id(reservations[i].get('client_id'))
        cine=find_cinema_by_id(film.get("cinemas"),reservations[i].get("cine_id"))
        nom=f"""{client.get("nom")} {client.get("prenom")}"""
        etat=etat_de_reservation(reservations[i].get('etat'))
        print(f"""{i:<10}{film.get("titre"):<17}{ nom:<15}{cine.get("nom"):<20}{cine.get("salle"):<8}{reservations[i].get('nbre_place_reserve'):<8}{reservations[i].get('date'):<12}{etat:<10}""")
        print('-'*TAILLE)

def afficher_reservations_terminees(reservations:list):
    print('-'*TAILLE)
    print(f"""{'POSITION':<10}{'FILM':<20}{'CINEMA':<20}{'SALLE':<8}{'PLACES':<8}{'MONTANT':<12}{'DATE':<12}{'STATUT':<10}""")
    print('-'*TAILLE)
    n=len(reservations)
    for i in range(n):
        film=find_film_by_id(reservations[i].get('film_id'))
        cine=find_cinema_by_id(film.get("cinemas"),reservations[i].get("cine_id"))
        etat=etat_de_reservation(reservations[i].get('etat'))
        print(f"""{i:<10}{film.get("titre"):<20}{cine.get("nom"):<20}{cine.get("salle"):<8}{reservations[i].get('nbre_place_reserve'):<8}{reservations[i].get('montant'):<12}{reservations[i].get('date'):<12}{etat:<10}""")
        print('-'*TAILLE)



def details_reservation(reservations:list,p:int):
    clear_screen()
    msg="Details de la reservation:"
    print(f"""{msg}{'-'*(TAILLE-len(msg))}""")

    film=find_film_by_id(reservations[p].get('film_id'))
    client=find_client_by_id(reservations[p].get('client_id'))
    cine=find_cinema_by_id(film.get("cinemas"),reservations[p].get("cine_id"))
    nom=f"""{client.get("nom")} {client.get("prenom")}"""

    print(f"""{"CLIENT : ":>50}{nom}""")
    print(f"""{"CINEMA : ":>50}{cine.get('nom')}""")
    print(f"""{"SALLE : ":>50}{cine.get('salle')}""")
    print(f"""{"HORAIRE : ":>50}{cine.get('horaire').get("temps")}""")
    print(f"""{"DATE DE DIFFUSION : ":>50}{cine.get('horaire').get("jour")}""")
    print(f"""{"PLACES RÉSERVÉES : ":>50}{reservations[p].get('nbre_place_reserve')}""")
    print(f"""{"DATE DE RÉSERVATION : ":>50}{reservations[p].get('date')}""")
    print(f"""{"STATUT DE RÉSERVATION : ":>50}{etat_de_reservation(reservations[p].get('etat'))}""")
    print(f"""{"MONTANT DE RÉSERVATION : ":>50}{reservations[p].get('montant')}""")
    print(f"""\n{"------------ Informations du film ------------ ":^100}\n""")

    print(f"""{"TITRE : ":>50}{film.get('titre')}""")
    print(f"""{"GENRE : ":>50}{film.get('genre')}""")
    print(f"""{"DURÉE : ":>50}{film.get('duree')}""")
    print(f"""{"ANNÉE DE PRODUCTION : ":>50}{film.get('annee_de_production')}""")
    print(f"""{"DATE DE SORTIE : ":>50}{film.get('date_de_sortie')}""")
    print(f"""{"SYNOPSIS : ":>50}""")
    n=len(film.get('synopsis'))
    i=0
    while i<n:
        print(f"""{"":>42}{film.get('synopsis')[i:i+55]:}""")
        i=i+55
    print('-'*TAILLE)


def valider_reservations(reservations:list):
    n=len(reservations)
    films=load_films()
    clients = find_all_client()
    p='-1'
    while (p.isdigit()==False or (int(p)<0 or int(p)>=n)):
        p=input("Entrez la POSITION de la reservation à VALIDER : \n")
    details_reservation(reservations,int(p))
    validation=input("\nVoulez-vous confirmer la Validation  ? [ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    if(validation=='1'):
        i=reservations[int(p)].get("film_id")
        id_cine=reservations[int(p)].get("cine_id")
        if(films[i-1]["cinemas"][id_cine-1]["nbreplace"] >= reservations[int(p)].get("nbre_place_reserve")):
            reservations[int(p)]["etat"]=1
            films[i-1]["cinemas"][id_cine-1]["nbreplace"] -= reservations[int(p)].get("nbre_place_reserve")
            update_films(films)
            update_reservations(reservations)
            print("\n\n       **** RÉSERVATION VALIDÉE AVEC SUCCÈS !!! **** \n\n")
            for client in clients:
                if (client.get("id")==reservations[int(p)].get("client_id")):
                    create_ticket(client,reservations,int(p))
                    break
        else :
            print("\n\n       **** LA VALIDATION NE PEUT ABOUTIR !!! **** \n\n")
    else:
        print("\n\n       **** VALIDATION ANNULÉE !!! **** \n\n")
    os.system('pause')

def create_ticket(client:dict,reservations:list,p:int):
    nomFichier=f"""TICKET_{reservations[p].get('id')}_{reservations[p].get('date').replace("/","")}_{client.get('nom')}_{client.get('prenom')}.txt"""
    film=find_film_by_id(reservations[p].get('film_id'))
    cine=find_cinema_by_id(film.get("cinemas"),reservations[p].get("cine_id"))
    with open(nomFichier,"w",encoding='UTF-8') as f:
        f.write(f"""{'*'*70}\n""")
        f.write(f"{'** TICKET DE RÉSERVATION **':^70} \n")
        f.write(f"""{'*'*70}\n""")
        f.write(f"Nom : {client.get('nom')}\n")
        f.write(f"Prenom : {client.get('prenom')}\n")
        f.write(f"Login : {client.get('login')}\n")
        f.write(f"Date de Réservation : {reservations[p].get('date')}\n")
        f.write(f"""Ticket n° : TICKET_{reservations[p].get('id')}_{reservations[p].get('date').replace("/","")}\n\n""")
        f.write(f"""{'-'*70}\n""")
        f.write(f"{'AU PROGRAMME':^70} \n")
        f.write(f"""{'-'*70}\n""")
        f.write(f"FILM : {film.get('titre')}\n")
        f.write(f"""GENRE : {film.get('genre')}\n""")
        f.write(f"""DURÉE : {film.get('duree')}\n""")
        f.write(f"""ANNÉE DE PRODUCTION : {film.get('annee_de_production')}\n""")
        f.write(f"""DATE DE SORTIE : {film.get('date_de_sortie')}\n\n""")
        f.write(f"""{'-'*70}\n""")
        f.write(f"{'LE CINÉMA':^70} \n")
        f.write(f"""{'-'*70}\n""")
        f.write(f"""NOM : {cine.get('nom')}\n""")
        f.write(f"""SALLE : {cine.get('salle')}\n""")
        f.write(f"""HORAIRE : {cine.get('horaire').get("temps")}\n""")
        f.write(f"""DATE DE DIFFUSION : {cine.get('horaire').get("jour")}\n""")
        f.write(f"""PLACES RÉSERVÉES : {reservations[p].get('nbre_place_reserve')}\n\n""")
        f.write(f"""{'-'*70}\n""")
        f.write(f"""{f"MONTANT TOTAL : {reservations[p].get('montant')} CFA ":>70} \n""")
        f.write(f"""{'-'*70}\n""")
        f.write(f"""{'*'*70}\n""")
        f.write(f"{'BON VISIONNAGE':^70} \n")
        f.write(f"""{'*'*(70-len(" MERCI ET À BIENTOT :):)"))} MERCI ET À BIENTOT :)\n""")

        



def generer_ticket(user:dict):
    clients=find_all_client()
    n=len(clients)
    cpt=0
    while cpt==0 :
        p=input("Entrez la POSITION du Client pour GÉNÉRER SON TICKET [ -1 pour quitter ] :\n")
        cpt=1
        if(p=="-1"):
            break
        elif p.isdigit()==False or int(p)>=n:
            cpt=0
    if(p=="-1"):
        print()
    else :
        clear_screen()
        if(clients[int(p)].get("etat")==0):
            print("\n\n       **** CE CLIENT EST SUSPENDU. PAS DE TICKET POUR LUI !!! **** \n\n")
        else:
            reservations = reservations_terminees_by_id_client(clients[int(p)].get("id"))
            if(reservations==[]):
                print("\n\n       **** AUCUNE RESERVATION TROUVÉE POUR CE CLIENT !!! **** \n\n")
            else:
                entete(user,"*")
                afficher_reservations_terminees(reservations)
                title(f"""LISTE DES RESERVATIONS DE {clients[int(p)].get("prenom").upper()} {clients[int(p)].get("nom").upper()}""")
                print()
                c='-1'
                while (c.isdigit()==False or (int(c)<0 or int(c)>=n)):
                    c=input("Entrez la POSITION de la RÉSERVATION pour GÉNÉRER SON TICKET  : \n")
                details_reservation(reservations,int(c))
                validation=input("\nVoulez-vous confirmer la création du Ticket ? [ 0 => ANNULER / 1 => CONFIRMER ] \n")
                while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
                    validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
                clear_screen()
                if(validation=='1'):
                    create_ticket(clients[int(p)],reservations,int(c))
                    print("\n\n       **** TICKET GÉNÉRÉ AVEC SUCCÈS !!! **** \n\n")
                else:
                    print("\n\n       **** GÉNÉRATION DE TICKET ANNULÉE !!! **** \n\n")

    

def fonction_caissier(user:dict):
    clear_screen()
    entete(user,'*') 
    print(f"{'-'*TAILLE}")
    milieu("MENU GENERAL")
    print("\n")
    reservations=reservations_encours()
    choice = menu_caissier()
    match choice :
        case 1:
            clear_screen()
            entete(user,'*')
            afficher_reservations(reservations)
            milieu("LISTE DES RESERVATIONS EN ATTENTE")
            print()
            valider_reservations(reservations)
            fonction_caissier(user)
        case 2:
            clear_screen()
            entete(user,'*')
            afficher_client()
            milieu("LISTE DES CLIENTS");
            print()
            generer_ticket(user)
            os.system('pause')
            fonction_caissier(user)
        case other:
            print("\nFermeture...")
            os.system('pause')
            sys.exit("Bye !")

########################################################## FIN CAISSIER ################################################################


####################################################### CLIENT ########################################################################

def menu_client():
    print("1........................RECHERCHER UN FILM POUR VOIR SES DETAILS")
    print("2........................VOIR LES FILMS DE LA SEMAINE")
    print("3........................FAIRE UNE RESERVATION")
    print("4........................VOIR MES RESERVATIONS")
    print("5........................ANNULER UNE RESERVATION")
    print("6........................QUITTER \n")
    choix = input("Faites votre choix : \n")
    while choix.isdigit()==False or int(choix)>7 or int(choix) <1:
        choix = input("Faites votre choix : \n")
    return int(choix)

def entrer_titre():
    cpt=0
    while cpt==0 :
        cpt=1
        titre= input("Entrez le titre du film : \n").strip()
        titreList=titre.replace(":","")
        titreList=titreList.split()
        for i in titreList:
            if(i.strip().isalnum()==False):
                cpt=0
                break      
    return titre.upper()

def faire_reservation(reservations:list,films:list,user:dict):
    reservation={}
    n=len(films)
    c='-1'
    while (c.isdigit()==False or (int(c)<0 or int(c)>=n)):
        c=input("Entrez la POSITION du film pour réserver  : \n")
    details_films(films,int(c))

    if (films[int(c)].get("cinema")==[]):
        print("\n\n        AUCUN PROGRAMME DE DIFFUSION POUR CE FILM !!! ")
    else:
        reservation["id"]=reservations[-1].get("id")+1
        reservation["client_id"]=user.get("id")
        reservation["film_id"]=films[int(c)].get("id")
        if(len(films[int(c)].get("cinemas"))==1):
            sauveCine=films[int(c)].get("cinemas")[0]
        else:
            cpt=0
            while cpt==0 :
                cpt=1
                cine=saisir_nom_cine("choisi ").lower()
                for cinema in films[int(c)].get("cinemas"):
                    if(cinema.get("nom").lower()==cine):
                        sauveCine=cinema
                        break
                    else: 
                        cpt=0
        reservation["cine_id"]=sauveCine.get("id")
        nbreplace = input("Combien de places souhaitez-vous réserver ? \n")
        while (nbreplace.isdigit()==False or int(nbreplace)>sauveCine.get("nbreplace")):
            nbreplace = input("Combien de places souhaitez-vous réserver ? \n")
        reservation["nbre_place_reserve"]=int(nbreplace)
        reservation["montant"]=int(nbreplace)*sauveCine.get("prix")
        reservation["date"]=date()
        reservation["etat"]=0
        liste=[]
        liste.append(reservation)
        details_reservation(liste,0)
        validation=input("\nVoulez-vous confirmer la Réservation ? [ 0 => ANNULER / 1 => CONFIRMER ] \n")
        while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
            validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
        clear_screen()
        if(validation=='1'):
            save_reservations(reservation)
            print("\n\n       **** RESERVATION EFFECTUÉE AVEC SUCCÈS !!! **** \n\n")
        else:
            print("\n\n       **** RESERVATION ANNULÉE !!! **** \n\n")

def annuler_reservation(reservations:list):
    n=len(reservations)
    c='-1'
    while (c.isdigit()==False or (int(c)<0 or int(c)>=n)):
        c=input("Entrez la POSITION de la RÉSERVATION pour l'ANNULER  : \n")
    details_reservation(reservations,int(c))
    validation=input("\nVoulez-vous confirmer l'Annulation  ? [ 0 => ANNULER / 1 => CONFIRMER ] \n")
    while validation.isdigit()==False or int(validation)>1 or int(validation) <0:
        validation = input("[ 0 => ANNULER / 1 => CONFIRMER ] : \n")
    clear_screen()
    if(validation=='1'):
        touteReserves= load_reservations()
        for r in touteReserves:
            if(reservations[int(c)].get("id")==r.get("id")):
                r["etat"]=2
                break
        update_reservations(touteReserves)
        print("\n\n       **** RESERVATION ANNULÉE AVEC SUCCÈS !!! **** \n\n")
    else:
        print("\n\n       **** ANNULATION DE RESERVATION REJETÉE !!! **** \n\n")



def fonction_client(user:dict):
    clear_screen()
    entete(user,'*') 
    print(f"{'-'*TAILLE}")
    milieu("MENU GENERAL")
    print("\n")
    choice = menu_client()
    films=load_films()
    match choice :
        case 1:
            clear_screen()
            entete(user,'*')
            print(f"{'-'*TAILLE}")
            title("RECHERCHE DE FILM")
            print()
            titre=entrer_titre()
            film=recherche_film(titre)
            if(film==False):
                print("\n\n       **** AUCUN RESULTAT TROUVÉ !!! **** \n\n")
            else:
                details_films(films,film["id"]-1)
            os.system('pause')
            fonction_client(user)
        case 2:
            clear_screen()
            entete(user,'*')
            films=load_films() 
            afficher_film(films)
            milieu("LISTE DES FILMS DE LA SEMAINE");
            print("")
            n=len(films)
            cpt=0
            while cpt==0 :
                choix=input("Entrez la POSITION d'un film pour voir les details [ -1 pour quitter ] :\n")
                cpt=1
                if(choix=="-1"):
                    break
                elif choix.isdigit()==False or int(choix)>=n:
                    cpt=0
            if(choix=="-1"):
               print()
            else :
                details_films(films,int(choix))
            os.system('pause')
            fonction_client(user) 
        case 3:
            clear_screen()
            entete(user,'*')
            films=load_films()
            reservations=load_reservations()
            afficher_film(films)
            title("FAIRE UNE RESERVATION")
            print()
            faire_reservation(reservations,films,user)
            os.system('pause')
            fonction_client(user)  
        case 4:
            clear_screen()
            entete(user,'*') 
            reservations = reservations_by_id_client(user.get('id'))
            afficher_reservations_terminees(reservations)
            milieu("LISTE DE MES RÉSERVATIONS")
            print("")
            n=len(reservations)
            cpt=0
            while cpt==0 :
                choix=input("Entrez la POSITION d'une réservation pour voir les details [ -1 pour quitter ] :\n")
                cpt=1
                if(choix=="-1"):
                    break
                elif choix.isdigit()==False or int(choix)>=n:
                    cpt=0
            if(choix=="-1"):
               print()
            else :
                details_reservation(reservations,int(choix))
            os.system('pause')
            fonction_client(user)    
        case 5:
            clear_screen()
            entete(user,'*') 
            reservations = reservations_encours_by_id_client(user.get('id'))
            afficher_reservations_terminees(reservations)
            milieu("LISTE DE MES RÉSERVATIONS EN ATTENTE")
            print()
            annuler_reservation(reservations)
            os.system('pause')
            fonction_client(user)  
        case other:
            print("\nFermeture...")
            os.system('pause')
            sys.exit("Bye !")
########################################################## FIN CLIENT ################################################################
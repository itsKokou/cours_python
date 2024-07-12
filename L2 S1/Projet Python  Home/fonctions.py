from constantes import F_USERS,F_FILMS,F_RESERVATIONS
import json
import os
from datetime import datetime

#================= Système 

def clear_screen():
    if(os.name=="posix"):
        os.system("clear")
    else :
        os.system("cls")

#================== Connexion 

def connexion_json(log,mdp):
    users= load_users()
    for user in users:
        if(user.get("login")==log and user.get("password")==mdp):
            return user
    return None

#================== USERS

def load_users():
    with open(F_USERS,"r",encoding='UTF-8') as f:
        users=json.load(f)
    return users

def update_users(users:list):
    with open(F_USERS,"w",encoding='UTF-8') as f:
        json.dump(users,f,ensure_ascii=False,indent=4)

def save_users(user:dict):
    users=load_users()
    users.append(user)
    update_users(users)

def find_all_client():
    users=load_users()
    usersClient=[]
    for u in users :
        if (u.get('role')==3):
            usersClient.append(u)
    return usersClient

def find_client_by_id(id:int):
    clients=find_all_client()
    for client in clients :
        if (client.get("id")==id):
            return client
    return None

#================== FILMS

def load_films():
    with open(F_FILMS,"r",encoding='UTF-8') as f:
        films=json.load(f)
    return films

def update_films(films:list):
    with open(F_FILMS,"w",encoding='UTF-8') as f:
        json.dump(films,f,ensure_ascii=False,indent=4)

def save_films(film:dict):
    films=load_films()
    films.append(film)
    update_films(films)

def find_film_by_id(id:int):
    films=load_films()
    for film in films :
        if (film.get("id")==id):
            return film
    return None

#=================== CINEMA

def find_cinema_by_id(cinemas:list,id:int):
    for cine in cinemas :
        if (cine.get("id")==id):
            return cine
    return None


#================= RESERVATIONS

def load_reservations():
    with open(F_RESERVATIONS,"r",encoding='UTF-8') as f:
        reservations=json.load(f)
    return reservations

def update_reservations(reservations:list):
    with open(F_RESERVATIONS,"w",encoding='UTF-8') as f:
        json.dump(reservations,f,ensure_ascii=False,indent=4)

def save_reservations(reservation:dict):
    reservations=load_reservations()
    reservations.append(reservation)
    update_reservations(reservations)

def reservations_encours():
    reservations=load_reservations()
    reservationsEnCours=[]
    for reservation in reservations :
        if (reservation.get("etat")==0):
            reservationsEnCours.append(reservation)
    return reservationsEnCours

def reservations_terminees_by_id_client(id:int):
    reservations=load_reservations()
    reservationsTerminees=[]
    for reserve in reservations :
        if (reserve.get('client_id')==id and reserve.get("etat")==1):
            reservationsTerminees.append(reserve)
    return reservationsTerminees

def reservations_by_id_client(id:int):
    reservations=load_reservations()
    reservationsClient=[]
    for reserve in reservations :
        if (reserve.get('client_id')==id):
            reservationsClient.append(reserve)
    return reservationsClient

def reservations_encours_by_id_client(id:int):
    reservations=reservations_encours()
    reservationsClient=[]
    for reserve in reservations :
        if (reserve.get('client_id')==id):
            reservationsClient.append(reserve)
    return reservationsClient
#============== DATE

def date():
    myDatetime = datetime.now()
    myString = myDatetime.strftime('%d/%m/%Y')
    return myString




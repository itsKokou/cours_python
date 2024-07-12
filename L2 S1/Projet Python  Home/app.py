#                     KOKOU GODWIN TCHAKPANA
from views import login_page,fonction_admin,fonction_caissier,fonction_client,clear_screen
from os import system
import sys

system('color 1')
connectedUser=login_page()
if (connectedUser.get('etat')==1):
    if (connectedUser.get('role')==1):
        fonction_admin(connectedUser)
    elif (connectedUser.get('role')==2):
        fonction_caissier(connectedUser)
    else :
        fonction_client(connectedUser)
else:
    clear_screen()
    print("\n\n             VOUS NE POUVEZ ACCÉDER À VOTRE COMPTE.   ")
    print("        VEUILLEZ VOUS RAPPROCHER DE L'ADMINISTRATEUR !!! \n\n")
    system('pause')
    sys.exit("Bye !")
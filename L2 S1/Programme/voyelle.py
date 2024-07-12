#Écrire un programme qui permet de saisir une phrase. Le programme compte le nombre de 
#voyelles de la phrase et pour chaque voyelle, son nombre de présences.
ph =input("Entrez une phrase : \n")
n=0
if ('i' in ph):
    n+=1
    cpt=ph.count('i')
    print(""" 'i' est présent {} fois """.format(cpt))
if ('a' in ph):
    n+=1
    cpt=ph.count('a')
    print(""" 'a' est présent {} fois """.format(cpt))
if ('e' in ph):
    n+=1
    cpt=ph.count('e')
    print(""" 'e' est présent {} fois """.format(cpt))
if ('o' in ph):
    n+=1
    cpt=ph.count('o')
    print(""" 'o' est présent {} fois """.format(cpt))
if ('u' in ph):
    n+=1
    cpt=ph.count('u')
    print(""" 'u' est présent {} fois """.format(cpt))
if ('y' in ph):
    n+=1
    cpt=ph.count('y')
    print(""" 'y' est présent {} fois """.format(cpt))
print ("Au total, il y a {} voyelle(s).".format(n))
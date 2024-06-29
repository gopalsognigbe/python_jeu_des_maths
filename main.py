def afficher_information_personne(nom,age,taille=0):
    print(f"votre nom est {nom}, vous avez {age} ans l'an prochain vous aurez {age + 1} ans")
    if age == 1 or age ==2:
        print('vous etes un bebe')
    elif age < 10 :
        print("vous etes mineur")
    elif age == 17:
        print('Vous etes presque majeur')
    elif age >= 12 and age < 18:
        print('vous etes adolescent')
    elif age == 18:
        print('vous etes tout juste majeur')
    elif age > 60:
        print('vous etes senior')
    elif age > 18:
        print('vous etes majeur')
    # afficher la taille 
    if taille != 0:
        print('votre taille est :'+str(taille)+' m')


def demander_nom ():
    nom= input('entrer le nom: ')
    while nom=='':
        nom= input('entrer le nom: ')
    return nom


def demander_age(nom_personne):
    age_int=0
    while     age_int==0:
        age=input(f'votre age {nom_personne} :')
        try:
            age_int= int(age)
        except:
            print('Erreur:vous devez rentrer un nombre ')
    return age_int
""" 
#demander nom
nom=demander_nom()
nom1=demander_nom()

#demander age
age=demander_age(nom)
age1=demander_age(nom1)

#afficher information
afficher_information_personne(nom,age)1
afficher_information_personne(nom1,age1)
"""
for i in range(0,3):
    nom='personne '+ str(i +1)
    age=demander_age(nom)
    afficher_information_personne(nom,age,)
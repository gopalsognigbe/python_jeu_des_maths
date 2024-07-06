import random
NOMBRE_MIN=1
NOMBRE_MAX=10
NOMBRE_Q=10
nb_point=0

trouve=False


def poser_question():
    a=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    op=random.randint(0,1)
    if op == 1:
        op='+'
        calcul=a+b
    else:
        op='*'
        calcul=a*b
    rep_str=input(f'Calculez {a} {op} {b} =')
    rep_int=int(rep_str)

    if rep_int == calcul:
        print('Bravo reponse correct!!')
        global trouve
        trouve=True

    else :
        print('Dommage')
        trouve=False
    return trouve



for i in range (1,NOMBRE_Q+1):
    print(f"Question {i} sur {NOMBRE_Q}:")
    poser_question()
    if trouve==True:
        nb_point+=1
    print('')
print(f"votre resultat {nb_point}/{NOMBRE_Q}")

if nb_point == 4 :
    print('Vous etes le meilleur!!')
elif nb_point == 0:
    print('Tres null!!')
elif nb_point > int(NOMBRE_Q/2): 
    print('Peu mieux faire')
else : 
    print('revise tes maths ')
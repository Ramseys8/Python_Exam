# Exercice 1: Multiples de 3 et 5


# Création de la fonction qui calcule la somme de tous les multiples de 3 et de 5 inférieurs à Nb_max 
def multiple_3_5(Nb_max):
    # On initialise Nb_multiple qui contiendra le nombre de multiples que l'on cherche
    Nb_multiple = 0
    # On crée une boucle qui parcourt tous les nombres de 0 à Nb_multiple
    for i in range(Nb_max):
        # Si i est un multiple de 3 ou de 5, il est additionné à Nb_multiple
        if i%3 == 0 or i%5 == 0:
            Nb_multiple += i
    # On renvoie Nb_miltiple et donc la somme des multiples de 3 et 5 inférieurs à Nb_max.
    print(Nb_multiple)
    return Nb_multiple
    
    
    
# L'énoncé souhaite que la fonction calcule la somme pour Nb_max = 1000 :
# On crée donc un entier Nb égale à 1000 puis on donne à res la somme de notre fonction avec Nb comme paramètre.

multiple_3_5(1000)

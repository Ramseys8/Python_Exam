# Exercice 2: Comptage de voyelles


# Création de la fonction qui demande à l'utilisateur de saisir une phrase, puis compte le
# nombre de voyelles (a, e, i, o, u) dans la phrase.
def counting_vowel(sentence):
    # On initialise Nb_vowel à 0.
    Nb_vowel = 0
    # On crée une boucle qui parcourt la phrase écrite par l'utilisateur.
    for i in sentence :
        # Si i est une voyelle (majuscule ou minuscule) on incrémente Nb_vowel de 1.
        if i in "aeiouAEIOU" :
            Nb_vowel +=1
    # On renvoie Nb_vowel qui contiendra le nombre de voyelle présentes dans la phrase.
    print(Nb_vowel)
    return(Nb_vowel)


if __name__ == "__main__":
    print("Start \n")    
    # On crée sentence qui prends comme valeur un input, qui demandera à l'utilisateur
    # d'écrire une phrase dont on comptera le nombre de voyelles.
    sentence = input("Veuillez écrire une phrase : \n")
    
    counting_vowel(sentence)

    print("\nEnd")
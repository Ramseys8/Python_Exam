# Exercice 3: Calcul de nombres premiers

def is_prime_number(nb):
    if nb <= 1:
        return False

    for i in range(2, int(nb**0.5)+1):
        if nb%i == 0:
            return False

    return True


if __name__ == "__main__":
    # Vous pouvez appeler des fonctions, créer des objets, etc.
    print("Start \n")
    number = int(input("Veuillez écrire un nombre entier : :\n"))
    if is_prime_number(number):
        print("C'est en effet un nombre premier")
    else:
        print("\nMalheureusement ce n'est pas un nombre premier...")

    print("\nEnd")

def calcul_factorielle_boucle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f'Étape {i}: {resultat}')
    return resultat

def calcul_factorielle_boucle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        print(f'Étape {i}: {resultat}')
        i += 1
    return resultat

def main():
    try:
        n = int(input("Entrez un entier n : "))
        choix_boucle = input("Choisissez la boucle (for/while) : ")

        if choix_boucle.lower() == "for":
            resultat = calcul_factorielle_boucle_for(n)
        elif choix_boucle.lower() == "while":
            resultat = calcul_factorielle_boucle_while(n)
        else:
            print("Choix de boucle invalide. Veuillez choisir 'for' ou 'while'.")

        print(f"\nLa factorielle de {n} est : {resultat}")

    except ValueError:
        print("Veuillez entrer un entier valide.")

if __name__ == "__main__":
    main()

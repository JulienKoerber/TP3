import random
def deviner_nombre():
    nombre= random.randint(0, 100)
    compteur = 0

    print("Devinez le nombre")
    print("Trouver le nombre entre 0 et 100")

    while True:
        try:
            devine = int(input("Votre nombre : "))
        except ValueError:
            print("Le nombre n'est pas valide")
            continue
        compteur += 1
        if devine < nombre:
            print("C'est plus grand")
        elif devine > nombre:
            print("C'est plus petit")
        else:
            print(f"Le nombre à été découvert en {compteur} tours.")
            break

if __name__ == "__main__":
    deviner_nombre()

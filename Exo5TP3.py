def calculer_cout_location(heure_debut, heure_fin):
    if heure_debut < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return

    if heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.\n")
        return

    if heure_debut > heure_fin:
        print("Attention ! L'heure de début de la location est après l'heure de fin.\n")
        return
    if 0 <= heure_debut < 7 or 17 <= heure_debut <= 24:
        tarif = 1
    else:
        tarif = 2

    duree_location = heure_fin - heure_debut
    cout_location = duree_location * tarif
    print(f"Le coût de la location est de {cout_location} euro(s).\n")
if __name__ == "__main__":
    try:
        heure_debut = int(input("Entrez l'heure de début de la location (0-24) : "))
        heure_fin = int(input("Entrez l'heure de fin de la location (0-24) : "))
        calculer_cout_location(heure_debut, heure_fin)
    except ValueError:
        print("Erreur ! Veuillez entrer des entiers pour les heures de début et de fin de location.")

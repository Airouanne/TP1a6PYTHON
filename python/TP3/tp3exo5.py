#EXO5


# Demander à l'utilisateur les heures de début et de fin de location
heure_debut = int(input("Entrez l'heure de début de la location : "))
heure_fin = int(input("Entrez l'heure de fin de la location : "))

# Vérifier la validité des heures
if heure_debut < 0 or heure_fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")
elif heure_debut == heure_fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.\n")
elif heure_debut > heure_fin:
    print("Attention ! Le début de la location est après la fin de la location.\n")
else:
    # Calculer le coût de la location en fonction des tarifs
    if 0 <= heure_debut < 7 or 17 <= heure_debut <= 24:
        tarif = 1
    else:
        tarif = 2

    # Calculer le nombre d'heures de location
    duree_location = heure_fin - heure_debut

    # Calculer le coût total
    cout_location = tarif * duree_location

    # Afficher le résultat
    print(f"Le coût de la location est de {cout_location} euro(s).")

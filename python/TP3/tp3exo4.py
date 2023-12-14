#EXO 4


# Fonction pour calculer la factorielle avec la boucle 'for'
def factorielle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f"Iteration {i}: {resultat}")
    return resultat

# Fonction pour calculer la factorielle avec la boucle 'while'
def factorielle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        print(f"Iteration {i}: {resultat}")
        i += 1
    return resultat

# Demander à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier pour calculer sa factorielle : "))

# Demander à l'utilisateur de choisir la boucle
choix_boucle = input("Choisissez la boucle ('for' ou 'while') : ").lower()

# Vérifier le choix de l'utilisateur et effectuer le calcul
if choix_boucle == 'for':
    resultat_final = factorielle_for(n)
elif choix_boucle == 'while':
    resultat_final = factorielle_while(n)
else:
    print("Choix de boucle non valide. Veuillez entrer 'for' ou 'while'.")

# Afficher le résultat final
print(f"La factorielle de {n} est : {resultat_final}")

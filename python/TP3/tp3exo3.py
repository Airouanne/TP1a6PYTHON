#EXO 3


import random

# Générer une valeur aléatoire entre 0 et 100
nombre_mystere = random.randint(0, 100)

# Initialiser le compteur de tentatives
tentatives = 0

print("Devinez le nombre mystère entre 0 et 100.")

while True:
    # Demander à l'utilisateur de deviner la valeur
    devine = int(input("Votre estimation : "))
    
    # Incrémenter le compteur de tentatives
    tentatives += 1

    # Comparer la valeur devinée avec le nombre mystère
    if devine < nombre_mystere:
        print("Plus grand. Essayez encore.")
    elif devine > nombre_mystere:
        print("Plus petit. Essayez encore.")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère {nombre_mystere} en {tentatives} tentatives.")
        break

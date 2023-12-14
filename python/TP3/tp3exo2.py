#EXO 2

import time

# Demander à l'utilisateur de saisir un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Utiliser la boucle 'for' pour afficher les nombres par ordre décroissant
print("Version avec la boucle 'for':")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)  # Attendre 1 seconde entre chaque nombre

# Réinitialiser le temps d'attente
time.sleep(1)

# Utiliser la boucle 'while' pour afficher les nombres par ordre décroissant
print("\nVersion avec la boucle 'while':")
i = n
while i >= 0:
    print(i)
    time.sleep(1)  # Attendre 1 seconde entre chaque nombre
    i -= 1

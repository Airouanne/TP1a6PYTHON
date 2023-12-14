#EXO 1
A.


# Demander à l'utilisateur de saisir la valeur de N
N = int(input("a) Entrez la valeur de N : "))

# Initialiser la somme à 0
somme = 0

# Calculer la somme des entiers naturels de 0 à N
for i in range(N + 1):
    somme += i

# Afficher le résultat
print(f"La somme des entiers naturels de 0 à {N} est : {somme}")

B.


while True:
    valeur = int(input("b) Entrez une valeur : "))
    if valeur == 100:
        break

C.


# Initialiser les compteurs
inf_10 = 0
sup_eq_10_inf_15 = 0
sup_eq_15 = 0

# Boucle pour lire 10 valeurs réelles
for _ in range(10):
    valeur = float(input("c) Entrez une valeur réelle entre 0 et 20 : "))
    
    # Vérifier l'intervalle et mettre à jour les compteurs
    if 0 <= valeur < 10:
        inf_10 += 1
    elif 10 <= valeur < 15:
        sup_eq_10_inf_15 += 1
    elif valeur >= 15:
        sup_eq_15 += 1

# Afficher les résultats
print(f"Nombre de valeurs inférieures strictement à 10 : {inf_10}")
print(f"Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 : {sup_eq_10_inf_15}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {sup_eq_15}")

D.


# Demander à l'utilisateur de saisir la valeur de X
X = float(input("d) Entrez un nombre supérieur à 1 : "))

# Initialiser la somme à 0 et le nombre N à 0
somme = 0
N = 0

# Calculer le plus grand N tel que la somme reste inférieure à X
while somme <= X:
    N += 1
    somme += N

# Afficher le résultat
print(f"Le plus grand nombre N tel que la somme soit inférieure ou égale à {X} est : {N-1}")






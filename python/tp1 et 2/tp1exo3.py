
jour = int(input("entrez le jour du mois (0-31) : "))
entrez le jour du mois (0-31) : 20
heure = int(input("entrez l'heure(0-23) : "))
entrez l'heure(0-23) : 9
minute = int(input("entrez les minutes(0-59) : "))
entrez les minutes(0-59) : 53
minutes_ecoulees = ( jour - 1 ) * 24 *60 + heure * 60 + minute
print (f"Depuis le debut du mois, il s'est ecoule {minutes_ecoulees} minutes.")


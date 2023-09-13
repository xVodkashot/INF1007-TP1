# Demander à l'utilisateur de choisir le type de conversion
print("Type de conversion : \n"
    "1: Kilometres vers Miles (K vers M)\n"
    "2: Miles vers Kilometres (M vers K)")

choice = int(input("Entrez votre choix (1 ou 2): "))

# Demande de la distance à l'utilisateur
distance = float(input("Entrez la distance a convertir: "))
KmMilesConstant = 0.621371

#Conversion

if choice == 1:
    choixKmEnMiles = distance / KmMilesConstant
    print(distance, "kilometers equivalent a", choixKmEnMiles, "miles.")

else :
    choixMilesEnKm = distance * KmMilesConstant
    print(distance, "miles equivalent a ", choixMilesEnKm, "kilometres.")




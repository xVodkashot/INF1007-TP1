#Question 2

# On demande à l'utilisateur d'entrer la longueur du rectangle en tant que nombre décimal (float).
height = float(input("Entrez la longueur du rectangle: "))

# On demande à l'utilisateur d'entrer la largeur du rectangle en tant que nombre décimal (float).
width = float(input("Entrez la largeur du rectangle: "))

# On calcule le périmètre du rectangle en utilisant la formule : 2 * (longueur + largeur).
perimeter = 2 * (height + width)

# On calcule l'aire du rectangle en utilisant la formule : longueur * largeur.
area = height * width

# On affiche le périmètre du rectangle.
print("Le permietre du rectangle est:", perimeter)

# On affiche l'aire du rectangle.
print("L'aire du rectangle est:", area) 
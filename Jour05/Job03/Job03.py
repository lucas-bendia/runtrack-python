# Définition de la fonction qui affiche le triangle
def afficher_triangle(hauteur):
    # Boucle sur chaque ligne du triangle
    for i in range(hauteur):
        # Calcul du nombre d'espaces nécessaires pour centrer le triangle
        espaces = ' ' * (hauteur - i - 1)
        # Construction de la ligne du triangle avec les caractères '/' et '\'
        slashes = '/' + ' ' * (2 * i) + '\\'
        # Affichage de la ligne du triangle
        print(espaces + slashes)
    # Affichage de la ligne du bas
    print('_' * (2 * hauteur + 1))

# Demande à l'utilisateur d'entrer la hauteur du triangle
hauteur = int(input("Entrez la hauteur du triangle : "))
# Appel de la fonction pour afficher le triangle
afficher_triangle(hauteur)

# Définition de la liste initiale avec des doublons
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


# Définition de la fonction qui supprime les doublons
def list():
    # Création d'une nouvelle liste vide pour stocker les éléments uniques
    liste_sans_doublons = []

    # Parcours de chaque élément de la liste initiale
    for i in ma_liste:
        # Si l'élément n'est pas déjà dans la nouvelle liste, on l'ajoute
        if i not in liste_sans_doublons:
            liste_sans_doublons.append(i)

    return liste_sans_doublons


print(list())


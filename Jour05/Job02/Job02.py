def rectangle(width, height):  # Définition de la fonction rectangle avec deux paramètres : width (largeur) et height (hauteur)
    for i in range(height):  # Boucle for qui s'exécute 'height' fois
        if i == 0 or i == height - 1:  # Si nous sommes sur la première ou la dernière ligne
            print('-' * width)  # On imprime un tiret '-' 'width' fois
        else:
            print('|' + ' ' * (width - 2) + '|')  # On imprime un caractère '|' suivi de 'width' - 2 espaces, puis un autre caractère '|'

rectangle(10, 3)  # Appel de la fonction rectangle avec width = 10 et height = 3

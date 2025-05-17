def func_saisie():
    while True:
        try:
            shape = int(input("Entrez l'ordre de la matrice : "))
            if shape < 5:
                print("Erreur : Les dimensions de la matrice devront être > 5")
            else:
                return shape
        except ValueError:
            print("Erreur : Vous devez saisir un nombre valide.")
    

def generate_matrice(shape):
    matrice = []
    for ligne in range(shape):
        elt_ligne = []
        for colonne in range(shape):
            elt_ligne.append(ligne * shape + colonne + 1)  # Générer des valeurs consécutives
        matrice.append(elt_ligne)
    return matrice

def menu_couleur():
    while True:
        print("--- MENU--COULEUR ---")
        print("1. Cliquer sur 1 pour le Bleu:")
        print("2. Cliquer sur 2 pour le Rouge:")
        print("3. Cliquer sur 0 pour quitter")
        choix = int(input("Veuillez choisir une option : "))
        if choix == 1:
            return "bleu"
        elif choix == 2:
            return "rouge"
        elif choix == 0:
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

def menu_positions():
    while True:
        print("----MENU--POSITION----")
        print("1. Cliquer sur 1 pour la position haute")
        print("2. Cliquer sur 2 pour la position basse")
        print("3. Cliquer sur 0 pour quitter")
        position = int(input("Veuillez choisir une option : "))
        if position == 1:
            return "haute"
        elif position == 2:
            return "basse"
        elif position == 0:
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

def colorizing(matrice, choix, position):
    couleur_ansi = {"bleu": "\033[94m", "rouge": "\033[91m", "reset": "\033[0m"}
    taille = len(matrice)
    for x in range(taille):
        for y in range(taille):
            # Si la position choisie est haute et que x > y, ou si la position est basse et que x < y
            if (position == "haute" and x > y) or (position == "basse" and x < y):
                # Appliquer la couleur à cette cellule
                print(f"{couleur_ansi[choix]}{matrice[x][y]}{couleur_ansi['reset']}", end=" ")
            else:
                # Afficher la valeur sans couleur
                print(f"{matrice[x][y]}", end=" ")
        print()  # Nouvelle ligne après chaque ligne de la matrice

def affichage():
    shape = func_saisie()
    matrice = generate_matrice(shape)
    choix = menu_couleur()
    position = menu_positions()
    matrix=colorizing(matrice, choix, position)
    return matrix

    
# Appel de la fonction
affichage()
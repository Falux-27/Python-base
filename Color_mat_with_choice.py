 # Fonction pour demander la taille de la matrice
def func_saisie():
    while True:
        try:
            ordre = int(input("Donner la dimension de la matrice: "))
            if ordre <= 4:
                print("Erreur ! La taille doit être supérieure à 4.")
            else:
                return ordre
        except ValueError:
            print("Vous devez saisir un nombre valide.")

# Fonction pour créer une matrice vide
def func_matrice(ordre):
    return [[" " for _ in range(ordre)] for _ in range(ordre)]

# Menu des couleurs
def menu_color():
    list_color = ["rouge", "bleu", "violet", "vert", "jaune", "orange"]
    couleur_choisi = []
    print("\n--- MENU-COULEUR ---")
    print("1. Choisir une couleur (1)")
    print("2. Quitter (2)")
    
    while len(couleur_choisi) < len(list_color):
        choix = int(input("Veuillez choisir une option : "))
        if choix == 1:
            # Affichage des couleurs une seule fois
            for indice, element in enumerate(list_color):
                print(f"{indice}: {element}")
            choix_couleur = int(input("Veuillez entrer le numéro de la couleur choisie: "))
            if 0 <= choix_couleur < len(list_color):
                couleur = list_color[choix_couleur]
                if couleur not in couleur_choisi:
                    couleur_choisi.append(couleur)
                    list_color.remove(couleur)
                    print(f"Vous avez choisi la couleur : {couleur}")
                else:
                    print(f"{couleur} est déjà choisie.")
            else:
                print("Numéro invalide.")
        elif choix == 2:
            print("Programme terminé !")
            break
        else:
            print("Option invalide.")
    
    return couleur_choisi

# Menu des positions
def menu_position():
    print("\n--- MENU-POSITION ---")
    print("1. Choisir une position (1)")
    print("2. Quitter (2)")
    liste_position = ["ADDP", "EDDP", "SDP", "ADDS", "EDDS", "SDS"]
    position_choisi = []

    while len(position_choisi) < len(liste_position):  # Tant qu'on n'a pas choisi toutes les positions
        choix = int(input("Veuillez choisir une option : "))
        if choix == 1:
            # Affichage des positions une seule fois
            for indice, element in enumerate(liste_position):
                print(f"{indice}: {element}")
            
            choix_position = int(input("Veuillez entrer le numéro de la position choisie: "))
            if 0 <= choix_position < len(liste_position):
                position = liste_position[choix_position]
                if position not in position_choisi:
                    position_choisi.append(position)
                    print(f"Vous avez choisi la position : {position}")
                else:
                    print(f"La position {position} est déjà choisie.")
            else:
                print("Numéro invalide.")
        elif choix == 2:
            print("Programme terminé !")
            break
        else:
            print("Option invalide.")
    
    return position_choisi

# Fonction de coloriage
def colorizing(matrice, couleur_choisi, position_choisi):
    couleur_ansi = {"rouge": "\033[31m", "bleu": "\033[34m", "violet": "\033[35m", "vert": "\033[32m", "jaune": "\033[33m", "orange": "\033[38;5;214m"}
    reset = "\033[0m"
    taille = len(matrice)
    for i in range(taille):
        for j in range(taille):
            if position_choisi[0] == "ADDP" and i < j:
                print(f"{couleur_ansi[couleur_choisi[0]]}{matrice[i][j]}{reset}", end=" ")
            elif position_choisi[1] == "EDDP" and i > j:
                print(f"{couleur_ansi[couleur_choisi[1]]}{matrice[i][j]}{reset}", end=" ")
            elif position_choisi[2] == "SDP" and i == j:
                print(f"{couleur_ansi[couleur_choisi[2]]}{matrice[i][j]}{reset}", end=" ")
            elif position_choisi[3] == "ADDS" and i + j < taille - 1:
                print(f"{couleur_ansi[couleur_choisi[3]]}{matrice[i][j]}{reset}", end=" ")
            elif position_choisi[4] == "EDDS" and i + j > taille - 1:
                print(f"{couleur_ansi[couleur_choisi[4]]}{matrice[i][j]}{reset}", end=" ")
            elif position_choisi[5] == "SDS" and i + j == taille - 1:
                print(f"{couleur_ansi[couleur_choisi[5]]}{matrice[i][j]}{reset}", end=" ")
            else:
                print(f"{matrice[i][j]}", end=" ")
        print()
    return matrice

# Programme principal
def affichage():
    ordre = func_saisie()
    matrice = func_matrice(ordre)
    couleur_choisi = menu_color()
    position_choisi = menu_position()
    affichage =colorizing(matrice, couleur_choisi, position_choisi)
    return affichage

# Appel de la fonction
affichage()


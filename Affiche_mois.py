def afficher_mois():
    # Tableau  mois
    mois = [
        "Janvier", "Février", "Mars","Avril", "Mai", "Juin","Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    for ligne_index in range(4):
        print(f"{mois[ligne_index]:<10} {mois[ligne_index+4]:<10} {mois[ligne_index+8]:<10}")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Afficher les mois de l'année")
        print("2. Quitter")
        
        choix = input("Veuillez choisir une option : ")

        if choix == "1":
            afficher_mois()
        elif choix == "2":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Lancer le programme
menu()

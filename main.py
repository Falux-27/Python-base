from Exo8 import *

def main():
    liste_etudiant = []
    while True:
        nombre_etudiant = int(input("Entrez le nombre d'étudiants à enregistrer: "))
        if nombre_etudiant > 0:
            break
        else:
           print("Veuillez entrer un nombre valide.")
    print("Saisie des informations de chaque etudiant...")
    for i in range (nombre_etudiant):
        print(f"Entrez les infos de l'etudiant {i+1} :")
        etudiant = saisie_ET_validation()
        moyenne(etudiant)
        liste_etudiant.append(etudiant)
    while True:
        print("==-> Menu-Principal ==->")
        print("1. Afficher tous les étudiants")
        print("2. Trier les étudiants par moyenne")
        print("3. Rechercher un étudiant")
        print("4. Modifier les notes d'un étudiant")
        print("5. Sortir")

        choix = input("Choisissez une option (1-5): ")
        if choix == "1":
            affichage(liste_etudiant)
        elif choix == "2":
            etudiants = func_tri(liste_etudiant)
            affichage(liste_etudiant)
        elif choix == "3":
            func_recherche(liste_etudiant)
        elif choix == "4":
            modif_By_number(liste_etudiant)
        elif choix == "5":
            sortir()
        else:
                print("Option invalide. Veuillez choisir une option entre 1 et 6.")

main()
        


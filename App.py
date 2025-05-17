def func_isdigit (chiffre):
    list_chiffre = "1234567890"
    for element in chiffre:
        if element not in list_chiffre:
            return False
    return True

def simple_valid_number(number):
    number = number.replace(" ", "")
    if len(number) != 9 or not func_isdigit(number):
        return False
    prefixes = ['77', '78', '76', '70', '75']
    return number[:2] in prefixes

def saisie_ET_validation():
    list_keys = ['nom', 'prenom', 'classe', 'note_devoir', 'note_exam', 'note_project', 'telephone']
    infos_etudiant = {}
    liste_numeros = []
    for cle in list_keys[:-4]:
        infos_etudiant[cle] = input(f"Entrez votre {cle}:" )
    while True:
            note_devoir = input("Entrez votre note de devoir:")
            note_exam = input("Entrez votre note d'examen:")
            note_project = input("Entrez votre note de projet:")
            if func_isdigit(note_devoir) and func_isdigit(note_exam) and func_isdigit(note_project):
                note_devoir = int(note_devoir)  
                note_exam = int(note_exam)  
                note_project = int(note_project)  
                if (0 <= (note_devoir) <= 20) and (0 <= (note_exam) <= 20) and ( 0 <= (note_project) <= 20):
                    infos_etudiant['note_devoir'] = note_devoir
                    infos_etudiant['note_exam'] = note_exam
                    infos_etudiant['note_project'] = note_project
                    break
                else:
                    print("Les notes doivent être comprises entre 0 et 20.")
            else:
                print("Veuillez entrer des chiffres valides.")

    while True:              
        numero = input("Entrez votre numero de telephone:")
        if simple_valid_number(numero):
            if numero not in liste_numeros:
                liste_numeros.append(numero)
                infos_etudiant['telephone'] = numero
                break
            else:
                print("Ce numero existe deja")
        else:
            print("Numero invalide")
            
    return infos_etudiant

def moyenne (infos_etudiant):
     moy = (
        ( infos_etudiant['note_devoir'] +
            infos_etudiant['note_exam'] +
            infos_etudiant['note_project']
        )/3
     )
     infos_etudiant['moyenne'] = moy
     return moy
 
def affichage(info_etudiant):
    print(f"{"Nom":<15} {"Prenom":<15}{"Classe":<15}{"Note devoir":<15}"
          f"{"Note Exam":15}{"Note projet":<15}{"Telephone":<15}{"Moyenne":<15}")
    for person in info_etudiant:
        print(f"{person['nom']:<15}{person['prenom']:<15}"
              f"{person['classe']:<15}{person['note_devoir']:<15}"
              f"{person['note_exam']:<15}{person['note_project']:<15}"
              f"{person['telephone']:<15}{person['moyenne']:<10.2f}")
        
def func_tri(infos_etudiant):
    taille = len(infos_etudiant)
    for i in range (taille):
        for j in range (i+1, taille):
            if infos_etudiant[i]['moyenne'] < infos_etudiant[j]['moyenne']:
                infos_etudiant[i], infos_etudiant[j] = infos_etudiant[j], infos_etudiant[i]
    return infos_etudiant

def func_recherche(infos_etudiant):
    critere = input("Entrez le critere de recherche:(nom, prenom, classe, telephone: )")
    critere = critere.lower()
    if critere not in ['nom', 'prenom', 'classe','telephone']:
        print("Critere invalide")
    else:
        valeur = input(f"Entrez la valeur de recherche:{critere}")
        valeur = valeur.lower()
        
        print(f"{'Nom':<15} {'Prenom':<15} {'Classe':<15}"
              f"{'Note devoir':<15} {'Note Exam':<15}"
              f"{'Note projet':<15} {'Telephone':<15} {'Moyenne':<15}")
        
        for element in infos_etudiant:
            if element[critere] == valeur:
                print(f"{element['nom']:<15}{element['prenom']:<15}"
                      f"{element['classe']:<15}{element['note_devoir']:<15}"
                      f"{element['note_exam']:<15}{element['note_project']:<15}"
                      f"{element['telephone']:<15}{element['moyenne']:<10.2f}")
        else:
            print("Aucune correspondance")
                
def modif_By_number (infos_etudiant):
    while True:
         numero = int(input("Entrez le numero telephone de l'étudiant:"))
         for element in infos_etudiant:
             if not (int(element["numero"] == numero)):
                print("Ce numero n'appartient à aucun etudiant")
         else:
            break
    for element in infos_etudiant:
        if numero == element['numero']:
            note = input ("Saisir la note à modifier(note_devoir,note_project,note_exam):")
            note = note.lower()
            if note not in ["note_devoir","note_project","note_exam"]:
                print("Vous devez choisir entre (note_devoir,note_project,note_exam)")
            else:
                try:
                    nouvel_note = int(input("Donner la nouvelle note:"))
                    element[note] = nouvel_note
                    print(f"La note {note} a été modifiée pour {nouvel_note}")
                except:
                    print("Veuillez entrer une valeur numérique valide pour la note")   

def sortir():
    print("Merci d'avoir utilisé l'application. Au revoir!")
    exit()
 
            
        
            
        

                    
                    


                    

        
        






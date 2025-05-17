#Exos 2:
def delet_espace(phrase):
    espace_trouve = False
    phrase_sans_espace = ""
    
    for element in phrase:
        if element != " ":
            phrase_sans_espace += element
            espace_trouve = False  # Caractère normal et qu'on peut ajouter un espace plus tard
        elif not espace_trouve:  # Si c'est un espace mais qu'on en a pas encore ajouté un
            phrase_sans_espace += " "
            espace_trouve = True
    return phrase_sans_espace.strip()  # Supprimer les espaces au début et à la fin de la phrase


#Exos 3:
def ctrl_display():
    caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .!?,:;-'"
    
    while True:
        paragraph = input("Donner une phrase: ").strip()
        if paragraph == '':
            print("La phrase ne peut pas être vide.")
            continue
        
        # Vérifier la longueur minimale de la phrase
        if len(paragraph) < 25:
            print("La phrase doit contenir au moins 25 caractères.")
            continue
        
        # Vérifier si la phrase contient un caractère speciaux
        for char in paragraph: 
            if char not in caracters:
                print(f"{char} est un caractère non autorisé.")
                return "Phrase invalide"
        
        # Vérifier si le premier mot commence par une majuscule
            if not paragraph[0].isupper():
                print(f"La phrase doit commencer par une lettrre en majuscule.")
                continue
                
        # Vérifier si la phrase se termine par ces points: " .!?"
        if paragraph[-1] not in ".!?":
            print("Une phrase doit toujours se terminer par '.', '?' ou '!'")
            return "Phrase invalide"
        
        # Corriger la phrase en supprimant les espaces inutiles
        paragraph = delet_espace(paragraph)
        
        print(f"Phrase corrigée: {paragraph}")
        #liste_phrase = []
        #liste_phrase.append(paragraph)
        #return liste_phrase
        return paragraph

# Appel de la fonction
ctrl_display()



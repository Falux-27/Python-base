def ctrl_display (*args):
    caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .!?"
    while True:
        paragraph = input("Donner une phrase:")
        if paragraph == '':
            continue
        else:
            for char in paragraph:
                if char not in caracters:
                    print(f"Caractère non autorisé: {char}")
                else:
                    if not char[0].isupper():
                        print(f"La première lettre de chaque mot doit être en majuscule")
                    else:
                        if not char[len(paragraph) - 1] != '.' or char[len(paragraph) - 1] != '?' or char[len(paragraph) - 1] != '!':
                            print(f"Une phrase doit toujours se terminer par . ou ? ou !")
                        else:
                            print(f"Phrase valide")
    return paragraph
print(ctrl_display("paragraph"))
    
                            
def replacements(*args):
    c = ""
    chaine  = input("Donner une chaine de caractères: :")
    caract = input("Donner un caractère à remplacer: ")
    for element in chaine:
        if element == caract :
            c += "*"
        else:
            c += element
    print(c)

replacements()
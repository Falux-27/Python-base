#Fonction isdigit
def func_isdigit (chiffre):
    list_chiffre = "1234567890"
    for element in chiffre:
        if element not in list_chiffre:
            return False
    return True
#Fonction pour verifier si le numero est valide
def valid_number(number, valid_numbers, invalid_numbers):
         number = number.replace(" ","")
         #Verifier si le numero est valide et contient 9 valeurs
         if len(number) !=9 or func_isdigit(number)== False:
             invalid_numbers.append(number)
             print("Numero invalide")
             return False
    #verifier si le prefixe du numero est valide 
         else:
            prefixes = ['77', '78', '76', '70', '75']
            if number [:2] not in prefixes:
                invalid_numbers.append(number)
                print("Numero invalide")
                return False
    #Si le numero est valide
            else:
                valid_numbers.append(number)
                print("Numero valide")
                return True
    
#Fonction pour recuperer les numeros de chaque operateurs
def retrieve_numbers(numbers):
    operateur = {"77": [], "78": [], "76": [], "70": [], "75": []}
    for elem in numbers:
            prefix = elem[:2]
            if prefix in operateur:
                operateur[prefix].append(elem)
            else:
                None
    return operateur ["77"], operateur["78"], operateur["76"], operateur["70"], operateur["75"]
#Fonction pour saisir les numeros
def writing_numb(*args):
    valid_numbers = []
    invalid_numbers = []
    print("Entrer le nombre de numero à saisir:")
    n = int(input())
    for num in range(n):
        print(f"Entrez le numéro {num + 1}:")
        number = input()
        valid_number(number, valid_numbers, invalid_numbers)
    #Affichage des numeros valides et invalides
    print("Numeros valides:")
    for num in valid_numbers:
        print(num)
    print("Numeros invalides:")
    for num in invalid_numbers:
        print(num)
    #Nombre de numero valide par operateur
    op_77, op_78, op_76, op_70, op_75 = retrieve_numbers(valid_numbers)
    print("Nombre de numeros valides par operateur:")
    
    print("Orange:", len(op_77))
    
    print("Kirene:", len(op_78))
    
    print("Yas:", len(op_76))
    
    print("Expresso:", len(op_70))
    
    print("Promobile:", len(op_75))
    
    
        
#Appel de la fonction      
#writing_numb() 


        
    
    
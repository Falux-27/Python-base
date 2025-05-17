
dict_letters = {
        "A": "2","B": "22","C":"222","D":"3","E":"33",
        "F":"333","G":"4","H":"44","I":"444",
        "J":"5","K":"55","L":"555","M":"6",
        "N":"66","O":"666","P":"7","Q":"77","R":"777",
        "S":"7777","T":"8","U":"88","V":"888","W":"9",
        "X":"99","Y":"999","Z":"9999"," ":"00"
        }

dict_numbers ={
    "0":"A","1":"B","2":"C",
    "3":"D","4":"E","5":"F",
    "6":"G","7":"H","8":"I",
    "9":"J"
}   

 
#Fonction isalnum
def fonction_isalnum (chaine):
    caracter_chaine = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for elt in chaine:
        if elt not in caracter_chaine :
            return False
    return True


def verifications(phrase):
    phrase = phrase.upper()
    correspondance = ""
    last_number = ""
    for letter in phrase:
        if letter in dict_letters:
            letter = dict_letters[letter]
            base_number = letter[0]
            if base_number == last_number:
                correspondance +="0"
            correspondance += letter
            last_number = base_number
        else:
            if letter in dict_numbers:
                letter = dict_numbers[letter]
                correspondance += letter
                last_number = ""
            else:
                if fonction_isalnum(letter) == False:
                    correspondance += letter
                    last_number = ""
    return correspondance

def main_function():
    phrase = input("veuillew saisir une phrase:")
    transformation = verifications(phrase)
    print("Transformation:", transformation)
    return transformation
#Appel de la fonction
main_function()





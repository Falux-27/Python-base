def func_isdigit (*args):
    for element in args:
        if type(element) == int:
            return True
        else:
            return f"veuiller saisir des chiffres"
func_isdigit ("sdfghjklhgf")
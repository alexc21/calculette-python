valeur = float(input())
signe = input()
valeur2 = float(input())


def multiplication (valeur, signe, valeur2):
    return valeur * valeur2
def soustraction (valeur, signe, valeur2):
    return valeur - valeur2
def division (valeur, signe, valeur2):
    return valeur / valeur2
def addition (valeur, signe, valeur2):
    return valeur + valeur2

if signe == "*":
    print(multiplication(valeur,signe,valeur2))
elif signe == "/":
    print(division(valeur,signe,valeur2))
elif signe == "+":
    print(addition(valeur,signe,valeur2))
else:
    print(soustraction(valeur,signe,valeur2))
    
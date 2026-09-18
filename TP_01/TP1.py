from random import *
#Exercise 01

def IMC():
    taille = float(input("Entrez votre taille en mètres : "))
    poids = float(input("Entrez votre poids en kilogrammes : "))
    imc = poids / (taille ** 2)
    print("Votre IMC est :", imc)

#Exercise 02

def tri():
    n=1
    lst = []
    while n>=0:
        n = int(input("Entrez un nombre entier positif, ou un nombre négatif pour terminer :"))
        if n >= 0:
            lst.append(n)
    lst.sort()
    print("Voici la liste triée :", lst)
    print("Le minimum est :", lst[0])
    print("Le maximum est :", lst[-1])
    print("La moyenne est :", sum(lst) / len(lst) if lst else 0)

#Exercise 03
def age_canine(age):
    assert age > 0, "age ne peut pas être négatif !!!"
    age_c = 0
    for i in range(0, age):
        if i <= 1:
            age_c += 10.5
        else:
            age_c += 4
    return age_c



#Exercise 4
def appro_pi(n):
    if n < 0:
        print("Le nombre d'approximation doit etre positif")
        return None
    
    pi = 3.0
    if n == 1:
        print(f"Approximation 1 : {pi}")

    for i in range(n - 1):
        k = i + 1
        denom = (2 * k) * (2 * k + 1) * (2 * k + 2)
        t = ((-1) ** i) * (4 / denom)
        pi += t
        
        print(f"Approximation {i + 2} : {pi}")
        
    return pi

#Exercise 5
def convertion(q):
    bin = []
    r=0
    while q!=0:
        r = q%2
        r = str(r)
        bin.append(r)
        q = q // 2
    bin.reverse()
    return bin


#Exercise 6
def calcul():
    type = str(input("type d'opération souhaité : (a)ddition, (s)oustraction, (m)ultiplication et (d)ivision  :"))
    if type == "a":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print("Le résultat de l'addition est :", a + b)
    elif type == "s":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print("Le résultat de la soustraction est :", a - b)
    elif type == "m":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print("Le résultat de la multiplication est :", a * b)
    elif type == "d":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        if b != 0:
            print("Le résultat de la division est :", a / b)
        else:
            print("Erreur : division par zéro")
    else:
        encore = str(input("Erreur : type d'opération inconnu  \nUn autre calcul ? o/n  :"))
        if encore == "o":
            calcul()
        else:
            print("Fin du programme")
            return

#Exercise 7
def immatriculation():
    alphabet="abcdefghjklmnpqrstvwxyz"
    plaque = alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper() + "-" + str(random.randint(000, 1000)).zfill(3) + "-" + alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper()
    return plaque if "SS" not in plaque else plaques()

print(immatriculation())

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

tri()

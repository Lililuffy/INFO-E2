#Exercise 01

def IMC():
    taille = float(input("Entrez votre taille en mètres : "))
    poids = float(input("Entrez votre poids en kilogrammes : "))
    imc = poids / (taille ** 2)
    print("Votre IMC est :", imc)

IMC()
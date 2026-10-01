import sys
import random

#Exercise 1

def factoriele(nbr):
    if nbr == 1:
        return 1
    else:
        return nbr * factoriele(nbr - 1)
    
#Exercise 2

lst = []
def syrracus(n):
    lst.append(n)
    if n == 1:
        return(lst)
    elif n % 2 == 0:
        return syrracus(n // 2)
    else:
        return syrracus(3 * n + 1)


#Exercise 3

def lire_fichier():
    try:

        if len(sys.argv) != 4:
            print("tu es censé donner 3 arguments!!!")
            return

        ou = sys.argv[1].lower()
        nb_lignes_str = sys.argv[2]
        chemin_fichier = sys.argv[3]

        if ou not in ["head", "tail"]:
            raise ValueError("Le premier paramètre doit être 'head' ou 'tail'.")

        if not nb_lignes_str.isdigit() or int(nb_lignes_str) <= 0:
            raise ValueError("Le nombre de lignes doit être un entier strictement positif.")

        nb_lignes = int(nb_lignes_str)

        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
        except (FileNotFoundError, OSError) as e:
            raise IOError(f"Fichier non trouvé ou inaccessible : '{chemin_fichier}'") from e

        if ou == "head":
            lignes_a_afficher = lignes[:nb_lignes]
        else:  # tail
            lignes_a_afficher = lignes[-nb_lignes:] if nb_lignes <= len(lignes) else lignes

        print("".join(lignes_a_afficher), end="")

    except (ValueError, IOError) as err:
        print(f"Erreur : {err}")


#Exercise 4

def pendu():

    with open("C:\\Users\\joyetlil\\Desktop\\INFO-E2\\TP_03\\dic.txt", "r", encoding="utf-8") as f:
        mots = [ligne.strip() for ligne in f if ligne.strip()]

    mot_choisi = random.choice(mots).upper()
    mot_masque = mot_choisi[0] + "_" * (len(mot_choisi) - 1)
    print("Voici ton pendu, bonne chance!!", mot_masque)


    gagne = False
    l_soumises = []
    essais = 10
    
    while gagne != True:
        if essais == 0:
            print("Vous avez perdu! Le mot était :", mot_choisi)
            break

        print("Vous avez déja soumis comme lettres :", ", ".join(l_soumises))
        lettre = str(input("Proposez une lettre : ")).upper()

        assert lettre not in l_soumises, "La lettre a déja été proposée."
        
        if lettre in mot_choisi:
            mot_masque = "".join([lettre if mot_choisi[i] == lettre else mot_masque[i] for i in range(len(mot_choisi))])
            if mot_masque == mot_choisi:
                print("bravo!!! vous avez trouvé le mot :", mot_choisi)
                gagne = True
            else:
                print("il y avait bien cette lettre dans le mot!!! : ", mot_masque)

        else : 
            print("il n'y avait pas cette lettre dans le mot!!! : ", mot_masque)
            print("il vous reste ", essais, " essais")
            essais -=1
        
        l_soumises.append(lettre)





pendu()
import copy
from random import randint

#Exercise 2

classDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

print(classDict["class"]["student"]["name"])
classDict["class"]["student"]["marks"]["physics"] = 89
classDict["class"]["student"]["average"] = (classDict["class"]["student"]["marks"]["physics"] + classDict["class"]["student"]["marks"]["history"])/2
classDict["class"]["student"] = [classDict["class"]["student"]]
classDict["class"]["student"].append({"name":"Ted", "marks" : {"physics": 34, "history":99}})
classDict["class"]["student"][1]["average"] = (classDict["class"]["student"][1]["marks"]["physics"] + classDict["class"]["student"][1]["marks"]["history"])/2
classDict["class"]["average_grade"] = (classDict["class"]["student"][0]["average"] + classDict["class"]["student"][1]["average"] )/ len(classDict["class"]["student"])


#Exercise 3
"""
n =  randint(2, 100)
lst = []
for _ in range(n):
    nbr = randint(0,500)
    lst.append(nbr)
print(lst)

vus = []
double = False
for nombre in lst:
    if nombre in vus:
        print("Doublon trouvé :", nombre)
        double = True
    vus.append(nombre)
if double == False:
    print("Aucun doublon trouvé")"""

#Exercise 4
def calculScore(p):
    score = []

    for i in p:
        if i == "C":
            score.pop()
        elif i == "D":
            score.append(score[-1] * 2)
        elif i == "+":
            score.append(score[-1] + score[-2])
        else:
            score.append(int(i))

    return sum(score)

print(calculScore(["10","2","C","D","+"]))
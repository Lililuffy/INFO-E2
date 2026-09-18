import copy
import random

#Exercise 2

classDict = {
 "class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

print(classDict["class"]["student"]["name"])
classDict["class"]["student"]["marks"]["physics"] = 89
classDict["class"]["student"]["average"] = (classDict["class"]["student"]["marks"]["physics"] + classDict["class"]["student"]["marks"]["history"])/2
classDict["class"]["student"] = [classDict["class"]["student"]]
classDict["class"]["student"].append({"name":"Ted", "marks" : {"physics": 34, "history":99}})
classDict["class"]["student"][1]["average"] = (classDict["class"]["student"][1]["marks"]["physics"] + classDict["class"]["student"][1]["marks"]["history"])/2
classDict["class"]["average_grade"] = (classDict["class"]["student"][0]["average"] + classDict["class"]["student"][1]["average"] )/ len(classDict["class"]["student"])
print(classDict)

#Exo
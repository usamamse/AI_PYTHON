import math 

def conversionTemps(secondes):
    heures = math.floor(secondes/3600)
    minutes = heures %60
    secondes = secondes %60
    return str(heures)+" heures "+str(minutes)+" minutes "+str(secondes)+" secondes"
print(conversionTemps(56263))
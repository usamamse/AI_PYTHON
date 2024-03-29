import math

def equation2deg(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        return "l'equation admet deux racine dans R : x1= "+ str((-b-math.sqrt(delta)/(2*a))) +" x2= " + str((-b+math.sqrt(delta)/(2*a)))  
    elif delta == 0:
        return "l'equation admet une seule racine dans R : x= " + -b/(2*a)
    else :
        return "l'equation n'admet pas une solution dans R"

print(equation2deg(3,-1,-10))
        
import os

nb1 = int(input("Veuillez entrez le 1ere nombre : "))
nb2 = int(input("Veuillez entrez la 2eme nombre : "))

os.system("cls")

print("*********** Menu ************")
print("        Addition")
print("        Soustraction")
print("        Multiplication")
print("        Division")
print("*****************************")

choix = str(input("Veuillez choissez une operation : "))

os.system("cls")
if choix == "+":
    print(str(nb1)+choix+str(nb2)+" = "+str(nb1+nb2))
elif choix == "/":
    print(str(nb1)+choix+str(nb2)+" = "+str(nb1/nb2))
elif choix == "-":
    print(str(nb1)+choix+str(nb2)+" = "+str(nb1-nb2))
elif choix == "x":
    print(str(nb1)+choix+str(nb2)+" = "+str(nb1*nb2))

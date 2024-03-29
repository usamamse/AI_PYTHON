sexe = str(input("Veuillez entrez le sexe :"));
age = int(input("Veuillez entrez l'age :"));

if sexe == "homme" and age > 20:
    print("Pay l'impot ")
elif sexe == "femme" and age >= 18 and age <= 35:
    print("Pay l'impot ")
else:
    print("Pas d'impot")


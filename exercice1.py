def mention(notes):
    somme = 0
    
    for note in notes:
        somme = note+somme
    
    nf = somme/3
    if nf >=10 and nf <12:
        return "Passable"
    elif nf >=12 and nf <14:
        return "Assez Bien"
    elif nf >=14 and nf <16:
        return "Bien"
    elif nf >16:
        return "Tres Bien"
    else:
        return "Insuffisant"
        
note1 =float(input("Veuillez entrer la note 1 :"))
note2 =float(input("Veuillez entrer la note 2 :"))
note3 =float(input("Veuillez entrer la note 3 :"))
    
notes = [note1,note2,note3]
    
print(mention(notes))
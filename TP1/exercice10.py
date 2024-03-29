def exercice10(tab):
    cmp = 0
    for i in range(9):
        print(tab[i+1])
        if tab[i] > tab[i+1]:
            cmp +=1
    if cmp == 0:
        return "Tableau est trie  dans un ordre croissant"
    else:
        return "Tableau n'est pas trie dans un ordre croissant"
    
tabl = [1,2,3,4,5,6,7,8,9,10]

print(exercice10(tabl))
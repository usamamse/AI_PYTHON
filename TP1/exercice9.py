def exo9(n):
    x=1
    somme = 0

    while x < 6:
        div = 6 % x
        print(div)
        if div == 0 :
            somme += x
        x+=1
    print(somme)
    if somme == n :
        return str(n)+" est un nombre parfait"
    else:
        return str(n)+" n'est pas un nombre parfait"
    
print(exo9(6))
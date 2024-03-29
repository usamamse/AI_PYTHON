def exo8(n):
    somme =0
    x=0
    while x<n:
        somme += 10**x
        x+=1
    return somme

print(exo8(5))
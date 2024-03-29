def exercice10p2(vec1,vec2):
    somme=0
    i=0
    while i < len(vec1):
        somme += vec1[i]*vec2[i]
        i+=1
    
    return somme

vec1=[2,5,3]
vec2=[7,1,0]

print(exercice10p2(vec1,vec2))
#Fonction qui recupere une matrice et retourne sa
#transposee
#(list)-> list

def transposee(M) :
    T = []
    for i in range(len(M[0])) :
        list =[]
        for j in range(len(M)) :
            a = M[j]
            b = a[i]
            list.append(b)
        T.append(list)
    return T

M = []
m = int(input("Nombre de rangees : "))
n = int(input("Nombre de colonnes : "))

for i in range(m) :
    list = []
    for j in range(n) :
        nb = int(input("Matrice["+str(i)+","+str(j)+"] : "))
        list.append(nb)
    M.append(list) 
print(M)

T = transposee(M)

print(T)














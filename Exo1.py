#Fonction qui recupere une matrice et retourne sa
#transposee
#(list)-> list
def transposee(M) :
    T = []
    for i in range(len(M[0])) :
        list =[]
        for j in range(len(M)) :
            liste_active = M[j]
            nb_actif = liste_active[i]
            list.append(nb_actif)
        T.append(list)
    return T

#Programme principal
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














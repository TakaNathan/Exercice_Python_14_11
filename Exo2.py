#Fonction qui va recuperer 2 matrices et retourner
#leurs sommes
#(list) -> list

def somme_matrice(A,B) :
    C = []

    for i in range(len(A)) :
        sum = 0
        sum_list = []
        for j in range(len(B)) :
            sum = A[i][j] + B[i][j]
            sum_list.append(sum)
        C.append(sum_list)
    return C

#Programme principal
matrice_1 = []
matrice_2 = []

m = int(input("Nombre de rangees des matrices: "))
n = int(input("Nombre de colonnes des matrices: "))
print("Premiere Matrice")
for i in range(m) :
    list = []
    for j in range(n) :
        nb = int(input("Matrice1["+str(i)+","+str(j)+"] : "))
        list.append(nb)
    matrice_1.append(list) 

print("Deuxieme matrice Matrice")
for i in range(m) :
    list = []
    for j in range(n) :
        nb = int(input("Matrice2["+str(i)+","+str(j)+"] : "))
        list.append(nb)
    matrice_2.append(list) 

Somme = somme_matrice(matrice_1,matrice_2)

print("Matrice 1 : \n",matrice_1)
print("Matrice 2 : \n",matrice_2,"\n *****")
print("La somme est : \n",Somme)

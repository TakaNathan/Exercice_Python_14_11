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
matrice_1 = [[1,2],[3,4]]
matrice_2 = [[1,1],[1,1]]

Somme = somme_matrice(matrice_1,matrice_2)

print("Matrice 1 : \n",matrice_1)
print("Matrice 2 : \n",matrice_2,"\n *****")
print("La somme est : \n",Somme)

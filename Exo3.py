#Fonction qui recupere deux matrices de meme taille
#et retourne leur produit
#(list)-> list

def produit_matrice(A,B) :
    
    C = []

    for i in range(len(A)) :
        liste = A[i]
        produit_list = []
        sum_pro = 0
        produit = 1
        for j in range(len(A)) :
            sum_pro = 0
            for k in range(len(liste)) :
                pro = liste[k] * B[k][j]
                sum_pro += pro
            produit_list.append(sum_pro)
        C.append(produit_list)

    return C

#Programme principal
matrice_1 = [[1,2,3],[4,5,6]]
matrice_2 = [[1,2],[3,4],[5,6]]


Produit = produit_matrice(matrice_1,matrice_2)

print("Matrice 1 : \n",matrice_1)
print("Matrice 2 : \n",matrice_2,"\n *****")
print("Le produit est : \n",Produit)

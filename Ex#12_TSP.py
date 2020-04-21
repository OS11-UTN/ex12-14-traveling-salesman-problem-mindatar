import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_usage_string, get_min_cut, get_selected_arcs
import random
# IMPORT THE DATA:
# TSP con algoritmo FMC ( flujo mínimo costo )
#
# Defino cantidad de sitios ó nodos.
x= 6
# Nodos 6 x 6
NI =np.zeros((x,x))

for i in range( len (NI)):
    for j in range ( len (NI)):
        if i != j :
            NI[i][j]= 1

print (" matriz nodo-nod" , NI)

NN= np.array(NI)

Aeq, arc_idxs = nn2na(NN)
AeqT = np.zeros((2*x,len(Aeq[0])))

# Inicializo del Vector de distancias C entre nodos.
C = []# formateo la AeqT
# voy a rellenar la AeqT , con los 1  y con los -1 , en cada posición

for i in range( len(Aeq)):

    for j in range(len(Aeq[0])):
        if Aeq[i][j] == 1 and j > i :
            AeqT[i][j] = 1


        else :
            if  Aeq[i][j] == -1 :
                AeqT[i+ 5][j]= 1

# lleno el vector C
for i in range( len(NI)):

    for j in range(len(NI)):
        if NI[i][j] ==  1 and j > i  :
            C.append(random.randint(1,20))

        #  Matriz AeqT , tendria lo que en la práctica es Aeq1 y Aeq2

## Replico los valores cambiados en  C , para tener el Vector C con costos con dim igual a Arcos.
for i in range ( len(C)):
    C.append(C[i])
print ( "primera corrida ", C)
#
#
# DATA MANIPULATION:
#
#

#for i in range (len(AeqT)):
#    for j in range(len(AeqT[0])):
#        bounds
bounds = tuple([(0,None)]*(len(AeqT[0])))
print ( "limites ", bounds)

vectroq = np.zeros(len(AeqT))
for i in range(len(vectroq)):
    vectroq[i]= 1

beq = np.array(vectroq)

print ( "matriz total ", AeqT)
print ( "beq ....; ", beq )
#
#c : es el vector de pesos o coeficientes de la funcion costo.
# A_ub: es la matriz de coeficientes para el sistema de restricciones “menos que”.
# b_u: es el vector de coeficientes libres en el sistema de ecuaciones.
# A_eq (opcional): es la matriz de coeficientes para el sistema de restricciones “igual que”.
# b_eq (opcional):es el vector de coeficientes libres en el sistema de ecuaciones de igualdad.
# bounds(opcional): lista de tuplas(min,max) para cada variable x
# method: cadena de texto del metodo a utilizar y tenemos 3 opciones
# ‘interior-point’ (en defecto)
# ‘revised simplex’ (recomendado)
# ‘simplex’ (obsoleto)
# x0: valores inciciales para inciar el proceso iterativo

# OPTIMIZE:
res = linprog(C, A_eq=AeqT, b_eq=beq, bounds=bounds, method='revised simplex' )

# GET THE SOLUTION:
#selarcs = get_selected_arcs(arc_idys,res.x )

#print('## Results ## ')
#print ('The row solution  will be : %s ' % res.x)
#print ('The arcs that make the shortest path will be (from , to ) : %s ' % selarcs)
#print ('The minimo cantidd de kmstr a caminar  will be : %0.2f ' % res.fun )

print( "solución total ", res)
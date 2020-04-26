import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_usage_string, get_min_cut, get_selected_arcs
import random
#from graph.Graph import Graph

# Importamos librerarias para ploteo de Grafos.
# IMPORT THE DATA:
# TSP con algoritmo FMC ( flujo mínimo costo )
#
# Defino cantidad de sitios ó nodos.
'''sources = [1, 2, 3, 0, 5, 1, 1, 3]
   targets = [0, 0, 0, 5, 0, 2, 3, 1]
   weights = [2, 2, 4, 1, 1, 3, 2, 2]

   graph = Graph(sources, targets, weights)

   graph.print_r()
   with_weight (boolean)[default=True][opcional]: Si muestra los pesos de cada arco (edge)
   graph.draw ( with_weight = False )
   '''

x= 6
# Nodos 6 x 6
NI =np.zeros((x,x))

for i in range( len (NI)):
    for j in range ( len (NI)):
        if i != j :
            NI[i][j]= 1

print (" matriz nodo-nod" , NI)

NN= np.array(NI)

AeqI, arc_idxs = nn2na(NN)

Aeq1 = (AeqI > 0 ).astype(int)
Aeq2 = (AeqI < 0 ).astype(int)

print ( " aeq 2 ", Aeq2)

Aeq = np.concatenate([Aeq1, Aeq2],axis= 0 )

print ( "matrix total ", Aeq)


# Inicializo del Vector de distancias C entre nodos.
C = []# formateo la AeqT

# lleno el vector C
for i in range( len(NI)):

    for j in range(len(NI)):
        if NI[i][j] ==  1 and j > i  :
            C.append(random.randint(1,20))


## Replico los valores cambiados en  C , para tener el Vector C con costos con dim igual a Arcos.
for i in range ( len(C)):
    C.append(C[i])
print ( "primera corrida ", C)

bounds = tuple([(0,None)]*(len(C)))
print ( "limites ", bounds)

vectroq = np.zeros(len(Aeq))
for i in range(len(vectroq)):
    vectroq[i]= 1

beq = np.array(vectroq)
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
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method='revised simplex' )


print( "solución total ", res)
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
NN =np.zeros((x,x))

for i in range( len (NN)):
    for j in range ( len (NN)):
        if i < j :
            NN[i][j]= 1

Aeq, arc_idxs = nn2na(NN)
AeqT = np.zeros((2*x,len(Aeq[0])))



# Inicializo del Vector de distancias C entre nodos.
C = np.zeros(len(Aeq[0]))
# formateo la AeqT
# voy a rellenar la AeqT , con los 1  y con los -1 , en cada posición

for i in range( len(Aeq)):
    for j in range(len(Aeq[0])):
        if Aeq[i][j] == 1 :
            AeqT[i][j] = 1
            C[i] = random.randint(0,20)
        elif  Aeq[i][j] == -1 :
            AeqT[i+ 5][j]= 1
            C[i+5] = random.randint(0, 20)

#  Matriz AeqT , tendria lo que en la práctica es Aeq1 y Aeq2
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

beq = vectroq

print ( "vector b ", len(beq))
print ( "vector b ", beq)
print ( "verctor c ", C)

print( "matriz Aeq", Aeq)
print ( "matriz total ", AeqT)

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
## Jose Ricardo Vasquez Vega
import math
import numpy as np
##Adición de vectores complejos.
def sum_complex_Vector(vec_a,vec_b):
    result = []
    if len(vec_a)==len(vec_b):
        for i in range(len(vec_a)):
            result.append(vec_a[i]+vec_b[i])
        return result
    return "Error, ajuste el tamaño de los vectores para que tengan el mismo tamaño"
##Inverso (aditivo) de un vector complejos
def inver_complex_Vector(vec_a):
    inver = []
    for i in range(len(vec_a)):
        inver.append(-1*vec_a[i])
    return inver
##Multiplicación de un escalar por un vector complejo.
def mult_escalar_complex_Vector(num,vec_a):
    mult = []
    for i in range(len(vec_a)):
        mult.append(num*vec_a[i])
    return mult
##Adición de matrices complejas.
def add_complex_matriz(matr_a, matr_b):
    colum_a = len(matr_a[0])
    colum_b = len(matr_b[0])
    fila_a = len(matr_a)
    fila_b = len(matr_b)
    add_matriz = []
    if fila_a == fila_b and colum_a == colum_b:
        for i in range(fila_a):
            fila = []
            for j in range(colum_a):
                fila.append(matr_a[i][j]+matr_b[i][j])
            add_matriz.append(fila)
    else:
        add_matriz = "Error, los tamaños son diferentes"
    return add_matriz

##Inversa (aditiva) de una matriz compleja.
def inv_add_complex_matriz(matr_a):
    fila_a = len(matr_a)
    colum_a = len(matr_a[0])
    for x in range(fila_a):
        for y in range(colum_a):
            matr_a[x][y] = -matr_a[x][y]
    return matr_a

##Multiplicación de un escalar por una matriz compleja.
def mult_complex_num_matriz(num, matr_a):
    fila_a = len(matr_a)
    colum_a = len(matr_a[0])
    for x in range(fila_a):
        for y in range(colum_a):
            matr_a[x][y] = num*matr_a[x][y]
    return matr_a

##Transpuesta de una matriz/vector
def transp_complex_matriz_vector(matr_a):
    if isinstance(matr_a[0], complex):
        return [[i] for i in matr_a]
    fila = len(matr_a)
    colum = len(matr_a[0])
    transp_matriz = [[0j] * fila for z in range(colum)]
    for x in range(fila):
        for y in range(colum):
            transp_matriz[y][x] = matr_a[x][y]
    return transp_matriz

##Conjugada de una matriz/vector
def conjugada_matriz(matr_a):
    if isinstance(matr_a[0], complex):
        return [z.conjugate() for z in matr_a]
    fila = len(matr_a)
    colum = len(matr_a[0])
    conjugada_matr = [[0j] * fila for v in range(colum)]
    for x in range(fila):
        for y in range(colum):
            conjugada_matr[x][y] = matr_a[x][y].conjugate()
    return conjugada_matr

##Adjunta (daga) de una matriz/vector
def adjunta_matriz(matr_a):
    conjugada_matr = conjugada_matriz(matr_a)
    adjunta = transp_complex_matriz_vector(conjugada_matr)
    return adjunta

##Producto de dos matrices (de tamaños compatibles)
def mult_matriz_compatibles(matr_a, matr_b):
    colum_a = len(matr_a[0])
    fila_a = len(matr_a)
    colum_b = len(matr_b[0])
    fila_b = len(matr_b)
    if colum_a != fila_b:
        return print("El tamaño de las matrices no es compatible")
    mult_matriz = [[0j] * colum_b for m in range(fila_a)]
    for x in range(fila_a):
        for y in range(colum_b):
            product_s = 0j
            for v in range(colum_a):
                product_s += matr_a[x][v] * matr_b[v][y]
            mult_matriz[x][y] = product_s
    return mult_matriz

def accion_matriz_vector(matr_a, vector):
    acción = mult_matriz_compatibles(matr_a, [[i] for i in vector])
    return [i[0] for i in acción]

#Producto interno de dos vectores
def produc_intern_cplx(vec_a,vec_b):
    if len(vec_a) == len(vec_b):
        suma = 0
        for i in range(len(vec_a)):
            suma += vec_a[i].conjugate()*vec_b[i]
    else:
        suma = "Error, tamaños erroneos"
    return suma

# Norma de un vector
def norma_vec_cplx(vec_a):
    Norma = produc_intern_cplx(vec_a,vec_a)
    Norma = round(math.sqrt(Norma.real),2)
    return Norma

#Distancia entre dos vectores
def dist_vec_cplx(vec_a,vec_b):
    sumvec = sum_complex_Vector(vec_a,inver_complex_Vector(vec_b))
    distan = norma_vec_cplx(sumvec)
    return distan


#Valores  y vectores propios de una matriz
def vec_propios(matr_a):
    matr_a = np.asarray(matr_a)
    tamaño = matr_a.shape
    fil_a = tamaño[0]
    col_a = tamaño[1]
    if fil_a == col_a:
        valoresp, vectoresp = np.linalg.eig(matr_a)
        vectoresp = np.transpose(vectoresp)
        valorpro = np.round(valoresp, 2)
        vectorpro = np.round(vectoresp, 2)
        return  vectorpro[0]
    else:
        return "Error,la matriz ingresada no es cuadrada"

def val_propios(matr_a):
    matr_a = np.asarray(matr_a)
    tamaño = matr_a.shape
    fil_a = tamaño[0]
    col_a = tamaño[1]
    if fil_a == col_a:
        valoresp, vectoresp = np.linalg.eig(matr_a)
        vectoresp = np.transpose(vectoresp)
        valorpro = np.round(valoresp, 2)
        vectorpro = np.round(vectoresp, 2)
        return  valorpro
    else:
        return "Error,la matriz ingresada no es cuadrada"

#Revisar si una matriz es unitaria
def matriz_unitaria(matr_a):
    if len(matr_a) == len(matr_a[0]):
            adjunt = adjunta_matriz(matr_a)
            checker = mult_matriz_compatibles(matr_a,adjunt)
            check = True
            for i in range(len(checker)):
                for j in range(len(checker)):
                    if (i == j and checker[i][j] != 1) or (i != j and checker[i][j] != 0):
                        check = False
                        break
            if check:
                resp = "La matriz ingresada es unitaria"
            else:
                resp = "La matriz ingresada NO es unitaria"
    else:
        resp = "Error, tamaño de matriz ingresada incorrecto"
    return resp

#Revisar si una matriz es Hermitiana

def matriz_hermitiana(matr_a):
    if len(matr_a) == len(matr_a[0]):
            adjunt = adjunta_matriz(matr_a)
            check = True
            for i in range(len(adjunt)):
                for j in range(len(adjunt)):
                    if matr_a[i][j] != adjunt[i][j]:
                        check = False
                        break
            if check:
                resp = "La matriz ingresada es hermitiana"
            else:
                resp = "La matriz ingresada NO es hermitiana"
    else:
        resp = "Error, tamaño de matriz ingresada es incorrecto"
    return resp

def produc_tensor_matriz_vec(matr_a, matr_b):
    lmatra = len(matr_a)
    lmatrb = len(matr_b)
    lmatra_1 = len(matr_a[0])
    lmatrb_1 = len(matr_b[0])
    fila = lmatra * lmatrb
    col = lmatrb_1 * lmatra_1
    result = [[0 for i in range (col)] for k in range(fila)]
    for j in range(fila):
        for k in range(col):
            result[j][k] = (matr_a[j//lmatrb][k//lmatrb_1])*(matr_b[j%lmatrb][k%lmatrb_1])
    return result




if __name__ == '__main__':

    print((sum_complex_Vector(([complex(-1,5),complex(3,6)]),([complex(-5,3),complex(-1,3)]))))
    print(inver_complex_Vector([complex(-2,4),complex(-5,7)]))
    print(mult_escalar_complex_Vector(6 ,[complex(-1, 4), complex(-6, 3)]))
    print(add_complex_matriz([[complex(3,8),complex(-3,8)],[complex(-1,8),complex(3,8)]],[[complex(2,6),complex(-3,7)],[complex(-1,8),complex(5,6)]]))
    print(inv_add_complex_matriz([[complex(8,6),complex(-8,3)],[complex(-8,5),complex(8,6)]]))
    print(mult_complex_num_matriz(4, [[complex(3, 2), complex(3, -1)],[complex(3, 4), complex(-3, 5)]]))
    print(transp_complex_matriz_vector([complex(3, 2), complex(3, -1)]))
    print(conjugada_matriz([[complex(3, 2), complex(3, -1)],[complex(3, 4), complex(-3, 5)]]))

    print(adjunta_matriz([[7-26j,9+24j,7-13j],[12-15j,-29+30j,8-25j],[17-16j,4+9j,5+18j]]))
    print((mult_matriz_compatibles([[3+14j,2j,-4+8j],[1j,9-10j,-6-7j],[11+2j,3-4j,9+5j]],[[7-26j,9+24j,7-13j],[12-15j,-29+30j,8-25j],[17-16j,4+9j,5+18j]])))
    print(accion_matriz_vector([[complex(6, 2), complex(5, 4)],
                                     [complex(5, 4), complex(-5, 5)]],
                                    [complex(-5, 1), complex(1, 3)]))


    print(produc_intern_cplx([3-8j,7,1,4+3j],[2j,5-4j,7j,3j]))
    print(norma_vec_cplx([3+2j,4-4j,-2j]))
    print(dist_vec_cplx([2j,3,4j],[1j,-3,-5j]))
    print(val_propios([[-6,-1j],[6j,1]]))
    print(vec_propios([[-6,-1j],[6j,1]]))

    print(matriz_unitaria([[2 / 3, (-8 + 1j) / 3], [(2 + 1j) / 3, 2 / 3]]))
    print(matriz_hermitiana([[9,2-8j,-5j],[2+1j,0,9-5j],[5j,9+5j,6]]))
    print(produc_tensor_matriz_vec([[2,3],[1,4]],[[5,3,2],[1,0,2],[-2,5,6]]))
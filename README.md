# LIBRERÍA CON OPERACIONES PARA VECTORES Y MATRICES DE NÚMEROS COMPLEJOS

Esta es una librería de Python que proporciona funciones para realizar operaciones de vertores y matrices de números complejos, incluyendo operaciones básicas, conversión de representaciones y cálculos de propiedades.

## Operaciones Soportadas en la libreria

La librería incluye las siguientes operaciones para vectores y matrices de numeros complejos, el la cual se uso la libreria numpy y el tipo de dato "complex":

- **Adición de vectores complejos:** `sum_complex_Vector(vec_a,vec_b)`
- **Inverso (aditivo) de un vector complejos:** `inver_complex_Vector(vec_a)`
- **Multiplicación de un escalar por un vector complejo:** `mult_escalar_complex_Vector(num,vec_a)`
- **Adición de matrices complejas:** `add_complex_matriz(matr_a, matr_b)`
- **Inversa (aditiva) de una matriz compleja:** `inv_add_complex_matriz(matr_a)`
- **Multiplicación de un escalar por una matriz compleja:** `mult_complex_num_matriz(num, matr_a)`
- **Transpuesta de una matriz/vector:** `transp_complex_matriz_vector(matr_a)`
- **Conjugada de una matriz/vector:** `conjugada_matriz(matr_a)`
- **Adjunta (daga) de una matriz/vector:** `adjunta_matriz(matr_a)`
- **Producto de dos matrices (de tamaños compatibles):** `mult_matriz_compatibles(matr_a, matr_b)`
- **Función para calcular la "acción" de una matriz sobre un vector.:** `accion_matriz_vector(matr_a, vector)`

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones proporcionadas para realizar operaciones con números complejos.

## Ejemplo de Uso

```python
import numpy as np
import Lib_Complex_Vec_y_Mat as lc

# Inverso (aditivo) de un vector complejos
vector_a = [complex(-5, 4), complex(-6, 7)]
inversoAdd = lc.inver_complex_Vector(vector_a)
print("Inverso (aditivo) :")
lc.print(inversoAdd)

# "Adición de vectores complejos"
vector_a = [complex(2, 9), complex(-1, 4)]
vector_b = [complex(4, -5), complex(0, 8)]
AdicionMatriz = lc.sum_complex_Vector(vector_a, vector_b)
print("Adición :")
lc.print(AdicionMatriz)
```
## Ejemplo de pruebas 

```python
import Lib_Complex_Vec_y_Mat as lc
import unittest

class Test_operations_complex_matriz_vector(unittest.TestCase):

## Prueba unitaria adicción de vectores complejos.
    def test_sum_complex_Vector(self):
        suma = lc.sum_complex_Vector([complex(-1,5), complex(3,6)],[complex(-5,3),complex(-1,3)])
        self.assertAlmostEqual(suma[0], complex(-6,8))
        self.assertAlmostEqual(suma[1], complex(2,9))
```

## Requisitos

- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)

## Versión
**Primera Versión**

## Autor
**Jose Ricardo Vasquez Vega**
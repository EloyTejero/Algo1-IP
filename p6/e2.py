#ej 1
def imprimir_saludo(nombre: str):
    print("Hola, ", nombre)

#imprimir_saludo(input())

#ej 2
import math
def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)

#print(raiz_cuadrada_de(2))

#ej 3
def fahrenheit_a_celsius(temp_far: float) -> float:
    return ((temp_far-32)*5)/9

#print(fahrenheit_a_celsius(75))

#ej 4
def imprimir_dos_veces(estribillo: str):
    print((estribillo+" ")*2)

#imprimir_dos_veces("hola")

#ej 5
def es_multiplo_de(n:int, m:int) -> bool:
    return n%m == 0 

#print(es_multiplo_de(4, 2))

#ej 6
def es_par(n:int) -> bool:
    return n%2 == 0

#print(es_par(56))

#ej 7
def cantidad_de_pizzas(comenzales: int, min_cant_de_porciones: int) -> int:
    cant_porciones:int = comenzales * min_cant_de_porciones
    cant_pizza:float = cant_porciones/8

    if(cant_pizza > round(cant_pizza) or cant_pizza < 1):
        cant_pizza = round(cant_pizza) + 1
    
    return cant_pizza

#print(cantidad_de_pizzas(1,10))


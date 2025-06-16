#ej 1
def imprimir_hola_mundo():
    print("Hola Mundo")

#ej 2
def imprimir_un_verso():
    print("holaaa")
    print("chauuu")

#ej 3
import math
def raizDe2() -> float:
    return round(math.sqrt(2), 2)

#print(raizDe2())

#ej 4
def factorial_de_dos() -> int:
    x : int = 4
    acum : int = 1
    for i in range(1, x+1):
        acum *= i

    return acum

#print(factorial_de_dos())

#ej 5
def perimetro() -> int:
    return 2*math.pi #perimetro radio 1

#print(perimetro())


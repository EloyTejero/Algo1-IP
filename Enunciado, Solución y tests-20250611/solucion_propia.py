#ej1
def maximas_cantidades_consecutivos(nums:list[int]) -> dict[int,int]:
    maximas_cantidades:dict[int,int] = {}
    ultimo:int
    for num in nums:
        if num in maximas_cantidades.keys():
            if num == ultimo:
                cant += 1
                if cant > maximas_cantidades[num]:
                    maximas_cantidades[num] = cant
            else:
                ultimo = num
                cant = 1
        else:
            maximas_cantidades[num] = 1
            ultimo = num
            cant = 1
    return maximas_cantidades

#ej2
def maxima_cantidad_primos(matriz:list[list[int]]) -> int:
    cant_max_primos:int = 0
    for i in range(len(matriz[0])):
        cant:int = 0
        for j in range(len(matriz)):
            if es_primo(matriz[j][i]):
                cant += 1
        if cant > cant_max_primos:
            cant_max_primos = cant
    return cant_max_primos
def es_primo(num:int) -> bool:
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

#ej3
from queue import Queue
def tuplas_positivas_y_negativas(cola:Queue[tuple[int,int]]) -> None:
    cola_positivos:Queue[tuple[int,int]] = Queue()
    cola_negativos:Queue[tuple[int,int]] = Queue()

    while not cola.empty():
        tupla:tuple[int,int] = cola.get()
        n1:int = tupla[0]
        n2:int = tupla[1]
        producto:int = n1 * n2
        if producto >= 1:
            cola_positivos.put(tupla)
        if producto <= -1:
            cola_negativos.put(tupla)
    while not cola_positivos.empty():
        tupla:tuple[int,int] = cola_positivos.get()
        cola.put(tupla)
    while not cola_negativos.empty():
        tupla:tuple[int,int] = cola_negativos.get()
        cola.put(tupla)

#ej4
def resolver_cuenta(s:str) -> float:
    numeros:list[float] = dividir_numeros(s)
    res:float = 0
    for i in numeros:
        res += i
    return res
def dividir_numeros(expresion:str)->list[float]:
    numeros:list[float] = []
    num:str = ""
    indice:int = 0
    if expresion[0] == "-" or expresion[0] == "+":
        num += expresion[0]
        indice = 1
    for i in range(indice,len(expresion)):
        if expresion[i] == '-' or expresion[i] == '+':
            numeros.append(float(num))
            num = ""
        num += expresion[i]
    numeros.append(float(num))
    return numeros
#ej 1
def alguno_es_cero(n:int, m:int) -> bool:
    suma:int = n + m
    return suma == n or suma == m

#print(alguno_es_cero(2,0))

#ej 2 
def ambos_son_0(n:int, m:int)->bool:
    return n + m == 0

#print(ambos_son_0(0,0))

#ej 3
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

#print(es_nombre_largo("123456789"))

#ej 4
def es_bisiesto(ano:int) -> bool:
    return ano%400 == 0 or (ano%4 == 0 and ano%100 != 0)

#print(es_bisiesto(1600))
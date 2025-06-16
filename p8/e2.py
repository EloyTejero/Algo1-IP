import random
from queue import Queue as Cola
#ejercicio 2
# COLAS
def copiar_cola(cola:Cola) -> Cola:
    new_cola:Cola = Cola()
    cola_aux:Cola = Cola()

    while not cola.empty():
        cola_aux.put(cola.get())
    while not cola_aux.empty():
        item:any = cola_aux.get()
        new_cola.put(item)
        cola.put(item)

    return new_cola

def mostrar_cola(cola:Cola) -> None:
    lista:list = []
    cola_aux:Cola = copiar_cola(cola)

    while not cola_aux.empty():
        lista.append(cola_aux.get())
    print(lista)

#punto 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola:
    cola:Cola[int] = Cola()
    for i in range(cantidad):
        cola.put(random.randint(desde, hasta))
    return cola

#mostrar_cola(generar_nros_al_azar(4,0,10))

#punto 9
def cantidad_elementos(cola:Cola) -> int:
    cola_aux:Cola = copiar_cola(cola)
    cont:int = 0

    while not cola_aux.empty():
        cola_aux.get()
        cont += 1
    return cont

#cola:Cola = generar_nros_al_azar(2,0,10)
#mostrar_cola(cola)
#print(cantidad_elementos(cola))
#mostrar_cola(cola)

#punto 10
def buscar_el_maximo(cola:Cola[int])->int:
    cola_aux:Cola[int] = copiar_cola(cola)
    max:int = cola_aux.get()

    while not cola_aux.empty():
        item:int = cola_aux.get()
        if item > max:
            max = item
    return max
# cola:Cola = generar_nros_al_azar(10,0,10)
# mostrar_cola(cola)
# print(buscar_el_maximo(cola))
# mostrar_cola(cola)

#punto 11
def buscar_nota_minima(c:Cola[tuple[str,int]]) -> tuple[str,int]:
    cola_aux:Cola[tuple[str,int]] = copiar_cola(c)
    mayor:tuple[str,int] = cola_aux.get()
    while not cola_aux.empty():
        item:tuple[str,int] = cola_aux.get()
        if item[1] > mayor[1]:
            mayor = item
    return mayor
# cola:Cola = Cola()
# cola.put(("hol",7))
# cola.put(("sadcas",10))
# cola.put(("tes",8))
# mostrar_cola(cola)
# print(buscar_nota_minima(cola))
# mostrar_cola(cola)

#punto 12
def intercalar(c1:Cola,c2:Cola) -> Cola:
    c1_aux:Cola = copiar_cola(c1)
    c2_aux:Cola = copiar_cola(c2)
    new_cola:Cola = Cola()

    while not c2_aux.empty():
        new_cola.put(c1_aux.get())
        new_cola.put(c2_aux.get())
    return new_cola
cola1:Cola = generar_nros_al_azar(2,0,10)
cola2:Cola = generar_nros_al_azar(2,0,10)
# mostrar_cola(cola1)
# mostrar_cola(cola2)
# mostrar_cola(intercalar(cola1,cola2))
# mostrar_cola(cola1)
# mostrar_cola(cola2)

#punto 13
#parte 1 generar 100 numeros aleatorios no repetidos
#el problema dice de generar 100 pero yo lo voy a hacer con parametro para generar cuantos yo quiera
def armar_secuencia_de_bingo(cant:int) -> Cola[int]:
    bingo:Cola[int] = Cola()
    numeros:list[int] = []
    for i in range(cant):
        numeros.append(i)
    for i in range(cant):
        indice_aleatorio:int = random.randint(0,len(numeros)-1)
        bingo.put(numeros.pop(indice_aleatorio))
    return bingo
#cola_bingo:Cola[int] = armar_secuencia_de_bingo(100)
#mostrar_cola(cola_bingo)
def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int]) -> int:
    cont:int = 0
    while len(carton) > 0:
        item:int = bolillero.get()
        if item in carton:
            carton.remove(item)
        cont +=1
    return cont
# carton:list[int] = [0,34,52,12,6,86,13,80,2,91,99,77]
# cola_bingo:Cola[int] = armar_secuencia_de_bingo(100)
# print(jugar_carton_de_bingo(carton, cola_bingo))

#punto 14
def pacientes_urgentes(cola:Cola[tuple[int,str]]) -> int:
    cola_copy:Cola[tuple[int,str]] = copiar_cola(cola)
    cont:int = 0
    while not cola_copy.empty():
        if cola_copy.get()[0] < 4:
            cont += 1
    return cont

# cola14:Cola[tuple[int,str]] = Cola()
# cola14.put((1,"a"))
# cola14.put((6,"b"))
# cola14.put((2,"c"))
# cola14.put((7,"d"))
# print(pacientes_urgentes(cola14))
# mostrar_cola(cola14)

#punto 15
def atencion_a_clientes(cola:Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    cola_aux:Cola[tuple[str,int,bool,bool]] = copiar_cola(cola)
    cola_comun:Cola[tuple[str,int,bool,bool]] = Cola()
    cola_preferencial:Cola[tuple[str,int,bool,bool]] = Cola()
    cola_prioridad:Cola[tuple[str,int,bool,bool]] = Cola()

    while not cola_aux.empty():
        elemento:tuple[str,int,bool,bool] = cola_aux.get()

        if elemento[3]:
            cola_prioridad.put(elemento)
        elif elemento[2]:
            cola_preferencial.put(elemento)
        else:
            cola_comun.put(elemento)
    
    while not cola_prioridad.empty():
        cola_aux.put(cola_prioridad.get())
    while not cola_preferencial.empty():
        cola_aux.put(cola_preferencial.get())
    while not cola_comun.empty():
        cola_aux.put(cola_comun.get())
    
    return cola_aux

# cola15:Cola[tuple[str,int,bool,bool]] = Cola()
# cola15.put(("a",1,False,False))
# cola15.put(("b",2,False,True))
# cola15.put(("c",3,True,True))
# cola15.put(("d",4,True,False))
# mostrar_cola(atencion_a_clientes(cola15))
# mostrar_cola(cola15)
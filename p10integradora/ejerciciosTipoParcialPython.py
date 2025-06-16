'''
el hospital se representa como una matriz, cada piso es una lista y cada lista es de bool donde cada valor representa si una cama esta ocupada o no
'''
from queue import Queue

def nivel_de_ocupacion(camas_por_piso:list[list[bool]])-> list[float]:
    res:list[float] = []
    for piso in camas_por_piso:
        ocupadas:int = 0
        total:int = len(piso)
        for cama in piso:
            if cama:
                ocupadas += 1
        res.append(ocupadas/total)
    return res

#print(nivel_de_ocupacion([[True,False,True],[False, False, True],[True, True, True]]))

def cambiar_matriz(matriz:list[list[int]]) -> None:
    ultima_fila:list[int] = matriz[len(matriz)-1]
    for i in range(len(matriz)-1,0,-1):
        matriz[i] = matriz[i-1]
    matriz[0] = ultima_fila

#matriz = [[1],[2]]
#cambiar_matriz(matriz)
#print(matriz)

def promedio_salidas(registro:dict[str, list[int]]) -> dict[str, tuple[int,float]]:
    promedios:dict[str, tuple[int,float]] = {}

    for nombre in registro.keys():
        tiempos:list[int] = registro[nombre]
        cant_tiempos:int = 0
        total_tiempos:int = 0
        for i in tiempos:
            if i > 0 and i < 61:
                cant_tiempos += 1
                total_tiempos += i
        if cant_tiempos == 0:
            promedios[nombre] = (0,0)
        else:
            promedios[nombre] = (cant_tiempos, total_tiempos/cant_tiempos)
    return promedios

#print(promedio_salidas({"a":[61,60,59,58], "b":[1,2,3,0]}))

def reordenar_cola_priorizando_vips(filaClientes:Queue[tuple[str,str]]) -> Queue[str]:
    copia_cola:Queue[tuple[str,str]] = Queue()
    res:Queue[str] = Queue()
    cola_vip:Queue[str] = Queue()
    cola_comun:Queue[str] = Queue()
    elementos:list[tuple[str,str]] = []

    while not filaClientes.empty():
        elementos.append(filaClientes.get())
    for i in elementos:
        copia_cola.put(i)
        filaClientes.put(i)
    
    while not copia_cola.empty():
        item:tuple[str,str] = copia_cola.get()
        if item[1] == "vip":
            cola_vip.put(item[0])
        else:
            cola_comun.put(item[0])

    while not cola_vip.empty():
        res.put(cola_vip.get())

    while not cola_comun.empty():
        res.put(cola_comun.get())

    return res

cola:Queue[tuple[str,str]] = Queue()
cola.put(("ana", "comun"))
cola.put(("juli", "vip"))
cola.put(("fede", "vip"))
cola_res:Queue[str] = reordenar_cola_priorizando_vips(cola)
while not cola_res.empty():
    print(cola_res.get())
#funciona god
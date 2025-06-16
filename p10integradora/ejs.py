from queue import Queue, LifoQueue

#veterinaria
#ej 1 
def stock_productos(stock_cambios:list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    productos:dict[str,tuple[int,int]] = {}
    for item in stock_cambios:
        producto:str = item[0]
        cantidad:int = item[1]
        if not producto in productos.keys():
            productos[producto] = (cantidad, cantidad)
        else:
            minmax:tuple[int,int] = productos[producto]
            if cantidad > minmax[1]:
                productos[producto] = (minmax[0],cantidad)
            elif cantidad < minmax[0]:
                productos[producto] = (cantidad,minmax[1])
    return productos

# stock_cambios:list[tuple[str,int]] = [("a",1),("b",2),("a",10),("b",1),("c",15)]
# print(stock_productos(stock_cambios))

#ej2
def es_primo(num:int) -> bool:
    if num < 2 and num > -2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
def obtener_ultimos_tres_digitos(num:int)->int:
    if num // 1000 == 0:
        return num
    return num % 1000
def filtrar_codigos_primos(codigos:list[int]) -> list[int]: #los ultimos tres digitos primos
    codigos_primos:list[int] = []
    for num in codigos:
        if es_primo(obtener_ultimos_tres_digitos(num)):
            codigos_primos.append(num)
    return codigos_primos

# codigos_primos:list[int] = filtrar_codigos_primos([1,2,34,5,6,7,101,1101])
# print(codigos_primos)

#ej3 
def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    indice_max:int = 0
    cant_max:int = 0
    cant:int = 0
    indice:int = 0
    paciente:str = tipos_pacientes_atendidos[0]
    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == paciente:
            cant += 1
            if cant > cant_max:
                cant_max = cant
                indice_max = indice
        else:
            indice = i
            cant = 1
            paciente = tipos_pacientes_atendidos[i]

    return indice_max

#print(subsecuencia_mas_larga(["gato","gato","hola","hola","hola"]))

#ej4
def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> list[tuple[True,True]]:
    res:list[tuple[bool,bool]] = []
    for i in range(len(grilla_horaria[0])):
        primer_encargado_primer_turno:str = grilla_horaria[0][i]
        primer_turno_igual:bool = True
        primer_encargado_segundo_turno:str = grilla_horaria[4][i]
        segundo_turno_igual:bool = True
        for j in range(len(grilla_horaria)):
            if j < 4:
                if grilla_horaria[j][i] != primer_encargado_primer_turno:
                    primer_turno_igual = False
            else:
                if grilla_horaria[j][i] != primer_encargado_segundo_turno:
                    segundo_turno_igual = False
        res.append((primer_turno_igual,segundo_turno_igual))
    return res

# print(un_responsable_por_turno([
#         ["a","a","c","a","a","a","a","a"],
#         ["a","a","c","a","a","x","x","a"],
#         ["a","a","c","a","a","a","a","c"],
#         ["a","a","c","a","a","a","a","a"],
#         ["b","d","b","b","b","b","b","b"],
#         ["b","d","d","b","b","x","b","b"],
#         ["b","d","b","b","b","x","b","b"],
#         ["b","d","b","b","b","b","b","b"],
#     ]
# ))

#Sala de Escape

#ej5 ya esta en el archivo de ejerciciosTipoParcial
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

#ej6
def tiempo_mas_rapido(tiempo_salas:list[int]) -> int:
    indice_mejor_tiempo:int = 0
    mejor_tiempo:int = tiempo_salas[0]
    for i in range(len(tiempo_salas)):
        tiempo:int = tiempo_salas[i]
        if tiempo < 1 or tiempo > 60:
            continue
        if tiempo < mejor_tiempo:
            indice_mejor_tiempo = i
            mejor_tiempo = tiempo
    return indice_mejor_tiempo

#print(tiempo_mas_rapido([61,31,0,1,55,2]))

#ej 7 
def racha_mas_larga(tiempos:list[int]) -> tuple[int,int]:
    comienzo_mejor_racha:int = 0
    final_mejor_racha:int
    cant_mejor_racha:int = 0
    indice:int = 0 
    cant:int = 0
    en_racha:bool = False

    for i in range(len(tiempos)):
        tiempo:int = tiempos[i]
        if not en_racha:
            indice = i
        if tiempo > 0 and tiempo < 61:
            en_racha = True
            cant += 1
            if cant > cant_mejor_racha:
                cant_mejor_racha = cant
                comienzo_mejor_racha = indice
                final_mejor_racha = i
        else:
            en_racha = False
            cant = 0

    return (comienzo_mejor_racha,final_mejor_racha)

#print(racha_mas_larga([0,1,0,1,1,1,1,0,1,1,1,1,1,1]))

#ej 8
def escape_en_solitario(amigos_por_sala:list[list[int]]) -> list[int]:
    res:list[int] = []
    for i in range(len(amigos_por_sala)):
        amigos:list[int] = amigos_por_sala[i]
        if amigos[2] == 0:
            continue
        if amigos[0] + amigos[1] + amigos[3] != 0:
            continue
        res.append(i)
    return res

# print(
#     escape_en_solitario(
#         [
#             [0,0,1,0],
#             [1,1,2,1],
#             [0,0,0,0],
#             [0,0,3,0]
#         ]
#     )
# )

#ej 9

def torneo_de_gallinas(estrategias:dict[str,str]) -> dict[str,int]:
    resultados:dict[str,int] = {}
    for jugador in estrategias.keys():
        estrategia_jugador:str = estrategias[jugador]
        resultados[jugador] = 0
        for otro_jugador in estrategias.keys():
            if otro_jugador != jugador:
                estrategia_otro_jugador:str = estrategias[otro_jugador]
                if estrategia_jugador == estrategia_otro_jugador:
                    if estrategia_jugador == "d":
                        resultados[jugador] -= 10
                    elif estrategia_jugador == "nd":
                        resultados[jugador] -= 5    
                else:
                    if estrategia_jugador == "d":
                        resultados[jugador] -= 15
                    else:
                        resultados[jugador] += 10
    return resultados
#print(torneo_de_gallinas({"n":"d", "n1":"nd","n2":"nd"}))

#ej10
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

#cola:Queue[tuple[str,str]] = Queue()
#cola.put(("ana", "comun"))
#cola.put(("juli", "vip"))
#cola.put(("fede", "vip"))
#cola_res:Queue[str] = reordenar_cola_priorizando_vips(cola)
#while not cola_res.empty():
#    print(cola_res.get())
#funciona god

#ej 11
def obtener_sufijos(palabra:str) -> list[str]:
    sufijos:list[str] = []
    for i in range(len(palabra)):
        sufijo:str = ""
        for j in range(i,len(palabra)):
            sufijo += palabra[j]
        sufijos.append(sufijo)
    return sufijos
def es_palindromo(texto:str) -> bool:
    for i in range(len(texto)):
        if texto[i] != texto[len(texto)-i-1]:
            return False
    return True
def cuantos_sufijos_son_palindromos(texto:str) -> int:
    sufijos:list[str] = obtener_sufijos(texto)
    cont:int = 0
    for i in sufijos:
        if es_palindromo(i):
            cont += 1
    return cont

#print(cuantos_sufijos_son_palindromos("lobo")) # palindromos "obo" y "o"

#ej12
def quien_gano_el_tateti_facilito(matriz:list[list[str]]) -> int:
    columnas_iguales:str = ""
    for i in range(len(matriz[0])):
        ultimo:chr = matriz[0][i]
        cont:int = 0
        for j in range(len(matriz)):
            if matriz[j][i] != ultimo:
                cont = 1
                ultimo = matriz[j][i]
            else:
                cont += 1
                if cont == 3:
                    columnas_iguales += matriz[j][i]
                    cont = 0
    if len(columnas_iguales) > 1:
        return 3
    if columnas_iguales == "x":
        return 1
    if columnas_iguales == "o":
        return 2
    if columnas_iguales == "":
        return 0
    
#print(quien_gano_el_tateti_facilito([
 #   ['x', '', '', 'o',''],
  #  ['' , '', '', '',''],
   # ['x', '', 'o', 'o',''],
    #['' , '', 'o', '',''],
    #['x', '', 'x', '','']
#]))

#ej 13
def orden_de_atencion(urgentes:Queue[int], postergables:Queue[int]) -> Queue[int]:
    res:Queue[int] = Queue()
    copia_urgentes:Queue[int] = Queue()
    copia_postergables:Queue[int] = Queue()
    aux:Queue[int] = Queue()
    while not urgentes.empty():
        aux.put(urgentes.get())
    while not aux.empty():
        e:int = aux.get()
        copia_urgentes.put(e)
        urgentes.put(e)
    while not postergables.empty():
        aux.put(postergables.get())
    while not aux.empty():
        e:int = aux.get()
        copia_postergables.put(e)
        postergables.put(e)
    while not copia_postergables.empty():
        res.put(copia_urgentes.get())
        res.put(copia_postergables.get())

    return res

#cola_urgentes:Queue[int] = Queue()
#cola_urgentes.put(1)
#cola_urgentes.put(2)
#cola_postergables:Queue[int] = Queue()
#cola_postergables.put(3)
#cola_postergables.put(4)
#cola_res:Queue[int] = orden_de_atencion(cola_urgentes, cola_postergables)
#while not cola_res.empty():
#    print(cola_res.get())

#ej 14
def alarma_epidemiologica(registros:dict[int,str], infecciosas:list[str], umbral:float) -> dict[str, float]:
    res:dict[str,float] = {}
    cant_por_enfermedad:list[tuple[str,int]] = []
    for enfermedad in infecciosas:
        cant_enfermedad:int = 0
        for paciente in registros.keys():
            if registros[paciente] == enfermedad:
                cant_enfermedad += 1
        if cant_enfermedad > 0:
            cant_por_enfermedad.append((enfermedad,cant_enfermedad))

    cant_registros:int = 0
    for i in registros.keys():
        cant_registros += 1
    
    for i in cant_por_enfermedad:
        porcentaje:float = i[1]/cant_registros
        if porcentaje >= umbral:
            res[i[0]] = porcentaje
    
    return res

#print(alarma_epidemiologica({1:"e1",2:"e2",3:"e1"},["e1","e2"],0.3))

#ej15
def empleados_del_mes(horas:dict[int,list[int]]) -> list[int]:
    res:list[int] = []
    horas_totales:dict[int,int] = {}
    max_horas:int = 0
    for empleado in horas.keys():
        horas_empleado:list[int] = horas[empleado]
        max_horas_empleado:int = 0
        for i in horas_empleado:
            max_horas_empleado += i
        if max_horas_empleado > max_horas:
            max_horas = max_horas_empleado
            horas_totales[empleado] = max_horas_empleado
        if max_horas_empleado == max_horas:
            horas_totales[empleado] = max_horas_empleado
    
    for empleado in horas_totales.keys():
        if horas_totales[empleado] == max_horas:
            res.append(empleado)

    return res

#print(empleados_del_mes({1:[1,2,3],2:[3,3],3:[1,1,1],4:[6]}))

#ej 16
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
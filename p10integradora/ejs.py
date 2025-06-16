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


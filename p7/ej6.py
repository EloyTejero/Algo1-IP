def ordenados(lista:list) -> bool:
        for i in range(len(lista)-1):
            if not lista[i] > lista[i+1]:
                return False
        return True

#ej1
def es_matriz(lista:list) -> bool:
    if len(lista) > 0:
        if(len(lista[0])>0):
            largo_fila:int = len(lista[0])
            for i in lista:
                if len(i) != largo_fila:
                    return False
            return True
    return False

#print(es_matriz([[1],[1,2]]))

#ej2
def filas_ordenadas(matriz:list, res:list)->None:
    if len(res)>0:
        res.clear()

    for fila in matriz:
        res.append(ordenados(fila))
     
res1:list = []
filas_ordenadas([[2,3,1],[2,1,0]],res1)
#print(res1)

#ej3
def columna(matriz:list, c:int) -> list:
    res:list = []
    for fila in matriz:
        for i in range(len(fila)):
            if i==c:
                res.append(fila[i])
    return res

#print(columna([[1,2,3],[4,5,6]], 2))

#ej4
def columnas_ordenadas(matriz:list) -> list:
    res:list = []
    for i in range(len(matriz[0])):
        res.append(ordenados(columna(matriz, i)))
    return res

#print(columnas_ordenadas([[5,2,7],[4,5,6]]))

#ej5 poner las columnas por filas
def trasponer(matriz:list) -> list:
    res:list = []
    for i in range(len(matriz[0])):
        res.append(columna(matriz,i))
    return res

#print(trasponer([[1,2,3],[4,5,6],[7,8,9]]))

#ej6
def quien_gana_tateti(matriz:list) -> int:
    
    #revisar columnas
    for i in range(len(matriz)):
        columnaValores:list = columna(matriz, i)
        marca:chr = columnaValores[0]
        #si es vacio ya sale de la busqueda
        if marca == ' ':
            continue

        todosIguales:bool = True
        for i in columnaValores:
            if i != marca:
                todosIguales = False
                #si encuentra uno que no es ya no vale la pena seguir buscando
                break
        if todosIguales:
            if marca == 'x':
                return 1
            if marca == 'o':
                return 0
    #revisar filas
    for fila in matriz:
        marca:chr = fila[0]
        #si es vacio ya sale de la busqueda
        if marca == ' ':
            continue

        todosIguales:bool = True
        for i in fila:
            if i != marca:
                todosIguales = False
                #si encuentra uno que no es ya no vale la pena seguir buscando
                continue
        if todosIguales:
            if marca == 'x':
                return 1
            if marca == 'o':
                return 0
    #revisar diagonales

    for i in range(3):
        if i == 0:
            todosIguales:bool = True
            marca:chr = matriz[i][i]
            for j in range(2):
                if not matriz[j+1][j+1] == marca:
                    todosIguales = False
        if i == 2:
            todosIguales:bool = True
            marca:chr = matriz[0][i]
            for j in range(2):
                if not matriz[j+1][j-1] == marca:
                    todosIguales = False
        if todosIguales:
            if marca == 'x':
                return 1
            if marca == 'o':
                return 0
    return 2

print(quien_gana_tateti([['o','o','o'],
                         ['x','o','x'],
                         ['o','x','o']]))
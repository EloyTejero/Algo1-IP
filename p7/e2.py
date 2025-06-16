#ej1 poner ceros en posiciones pares inout

def CerosEnPosicionesPares(nums:list):
    for i in range(len(nums)):
        if i%2 == 0:
            nums[i] = 0

lista:list = [1,2,3,4,5]
#CerosEnPosicionesPares(lista)
#print(lista)

#ej2 lo mismo del 1 pero solo in y devuelvo la lista
def CerosEnPosicionesPares2(nums:list) -> list:
    res:list = []
    for i in range(len(nums)):
        if i%2 == 0:
            print("reach",i)
            res.append(0)
        else:
            print("reachelse",i)
            res.append(nums[i])
        print(res)
    return res

lista2:list = [5,4,3,2,1]
lista3:list = CerosEnPosicionesPares2(lista2)
#print(lista3)

#ej3 in s:seq<Char>
def sin_vocales(palabra:str) -> str:
    palabra_sin_vocales:str = ""
    vocales:list = ['a','e','i','o','u']

    def pertenece(lista:list, e:chr) -> bool:
        for i in lista:
            if i == e:
                return True

        return False

    for i in palabra:
        if not pertenece(vocales, i):
            palabra_sin_vocales += i
    
    return palabra_sin_vocales

palabra:str = "skibidi"
palabra_sin_vocales:str = sin_vocales(palabra)
#print(palabra_sin_vocales)

#ej4 (in s:seq⟨Char⟩)
def reemplaza_vocales(palabra:str) -> str:
    vocales:list = ['a','e','i','o','u']
    def pertenece(lista:list, e:chr) -> bool:
        for i in lista:
            if i == e:
                return True

        return False
    
    palabra_reemplazada:str = ""

    for i in palabra:
        if pertenece(vocales, i):
            palabra_reemplazada += '-'
        else:
            palabra_reemplazada += i

    return palabra_reemplazada

palabra_reemplazada:str = reemplaza_vocales(palabra)
#print(palabra_reemplazada)

#ej5 in
def da_vuelta_str(palabra:str) -> str:
    palabra_reversa:str = ""
    for i in range(len(palabra)-1,-1,-1):
        print(i)
        palabra_reversa += palabra[i]
    return palabra_reversa

palabra1:str = "hola"
palabra_reversa:str = da_vuelta_str(palabra1)
#print(palabra1)
#print(palabra_reversa)

#ej6 in
def eliminar_repetidos(palabra:str) -> str:
    palabra_sin_repetidos:str = ""
    for i in palabra:
        cont:int = 0
        for j in palabra:
            if i == j:
                cont += 1
        if cont < 2:
            palabra_sin_repetidos += i
    return palabra_sin_repetidos

palabra_repetida:str = "holaa"
palabra_sin_repetidos:str = eliminar_repetidos(palabra_repetida) # si un elemento tiene repetidos elimina todos
#print(palabra_sin_repetidos)

#mismo pero solo eliminando los repetidos y dejando la primera aparicion
def eliminar_repetidos2(palabra:str)->str:
    def pertenece(lista:list, e:chr) -> bool:
        for i in lista:
            if i == e:
                return True

        return False
    
    palabra_aux:str = palabra
    nueva_palabra:str = ""

    for i in palabra_aux:
        if not pertenece(nueva_palabra, i):
            nueva_palabra += i
    return nueva_palabra

palabra_repetida2:str = "oholaa"
palabra_nueva:str = eliminar_repetidos2(palabra_repetida2) #deja la primera aparicion
#print(palabra_repetida2)
#print(palabra_nueva)

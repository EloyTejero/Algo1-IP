#e1
def pertenece(lista: list, elemento: int) -> bool: 
    for i in lista:
        if i == elemento:
            return True
        
    return False

def pertenece2(lista: list, elemento: int) -> bool:
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    
    return False

def pertenece3(lista: list, elemento: int) -> bool:
    i: int = 0
    while(i<len(lista)):
        if lista[i] == elemento:
            return True
        i+=1

    return False

#print(pertenece3([1,2,3,4], 7))

#e2
def divide_a_todos(nums:list, num:int) -> bool:
    for i in nums:
        if i%num != 0:
            return False
    
    return True

#print(divide_a_todos([2,6,4], 2))

#ej3
def sum_total(nums:list) -> int:
    sum:int = 0
    for i in nums:
        sum += i
    return sum

#print(sum_total([1,1,2,3]))

#ej4
def maximo(nums:list) -> int:
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

#print(maximo([1,2,3,4]))

#ej5
def minimo(nums:list)->int:
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return min

#print(minimo([1,2,3,4,0]))

#ej6
def ordenados(nums:list) -> bool:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    
    return True

#print(ordenados([1,2,3,4,0]))

#ej7
def pos_maximo(nums:list) -> int:
    indice:int = 0
    max:int
    
    if len(nums) == 0:
        return -1
    
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
            indice = i
    
    return indice

#print(pos_maximo([10,1,2,3,4,5]))

#ej8
def pos_minimo(nums:list) -> int:
    indice:int = 0
    min:int
    
    if len(nums) == 0:
        return -1
    
    min = minimo(nums)

    for i in range(len(nums)):
        if nums[i] == min:
            return i
        
#print(pos_minimo([1,2,0,3,4]))

#ej9
def long_mayorASiete(palabras:list) -> bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False

#print(long_mayorASiete(["ola","tal","12345678"]))

#ej10
def es_palindroma(palabra:str) -> True:
    for i in range(len(palabra)):
        if palabra[i] != palabra[len(palabra)-1-i]:
            return False
    return True

#print(es_palindroma("())("))

#ej 11

def iguales_consecutivos(nums:list) -> bool:
    cont:int = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            cont += 1
        else:
            cont = 0
        
        if cont == 2:
            return True
    return False

#print(iguales_consecutivos([1,1,2,1,3,2,2,2]))

#ej 12
def vocales_distintas(palabra:str) -> bool:
    vocales:list = ['a','e','i','o','u']
    cont:int = 0
    
    for vocal in vocales:
        if pertenece(palabra, vocal):
            cont += 1
        if cont == 3:
            return True
    
    return False

#print(vocales_distintas("holaau"))

#ej13
def pos_secuencia_ordenada_mas_larga(nums:list) -> int:
    max_contador:int = 0
    cont:int = 0
    indice:int = 0
    max_indice:int = indice

    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            cont += 1
            if cont > max_contador:
                max_contador = cont
                max_indice = indice
        else:
            cont = 0
            indice = i+1
    
    return max_indice

#print(pos_secuencia_ordenada_mas_larga([11, 2, 3, 1, 2, 3, 1, 2, 3, 4]))

#ej14
def cantidad_digitos_impares(nums:list) -> int:
    cont:int = 0
    for num in nums:
        while num > 0:
            if (num%10)%2 != 0:
                cont += 1
            num = num // 10
    return cont

print(cantidad_digitos_impares([57, 2383, 812, 246]))
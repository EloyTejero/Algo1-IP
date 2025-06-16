#ej1
'''problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { T rue }
asegura: { |res| ≥ |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }'''

def pertenece_a_cada_uno_version_1(matriz:list, e:int, res:list) -> None:
    if len(res) > 0:
        res.clear()
    
    for fila in matriz:
        for columna in fila:
            res.append(columna == e)

res1:list = [False]
pertenece_a_cada_uno_version_1([[5,5,5],[4,5,6],[7,8,5]], 5, res1)
#print(res1)

#ej2
'''problema pertenece a cada uno version 2 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}'''
#Realmente en el ej1 hice que la longitud de res sea mayor que s porque la longitud de s va a ser la cantidad de filas mientras que aca se me requiere que sea la longitud de res sea la cantidad de filas
def pertenece_a_cada_uno_version_2(matriz:list, e:int, res:list) -> None:
    def pertenece(lista:list, e:int)->bool:
        for i in lista:
            if i == e:
                return True
        return False
    
    if len(res) > 0:
        res.clear()
    
    for fila in matriz:
        res.append(pertenece(fila, e))

pertenece_a_cada_uno_version_2([[5,5,5],[4,5,6],[7,8,1]], 5, res1)
#print(res1)

'''problema pertenece a cada uno version 3 (in s:seq⟨seq⟨Z⟩⟩, in e:Z) : seq⟨Bool⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}'''
#la diferencia aca es que hay retorno, es una funcion.
def pertenece_a_cada_uno_version_3(matriz:list, e:int) -> list:
    def pertenece(lista:list, e:int)->bool:
        for i in lista:
            if i == e:
                return True
        return False
    
    res:list = []
    
    for fila in matriz:
        res.append(pertenece(fila, e))

    return res

print(pertenece_a_cada_uno_version_3([[1],[4,5,6],[7,8,1]], 5))

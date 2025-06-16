'''Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
por un/a alumno/a cumpliendo con la siguiente especificaci´on:
problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
requiere: { |notas| > 0 }
requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7 }
asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}'''

def resultadoMateria(notas:list) -> int:
    todasNotasAprobadas:bool = True
    promedio:int = 0
    for nota in notas:
        if nota < 4:
            todasNotasAprobadas = False
        promedio += nota
    
    promedio /= len(notas)

    if todasNotasAprobadas:
        if promedio >= 7:
            return 1
        if promedio < 7:
            return 2
    else:
        return 3
    
print(resultadoMateria([9, 4]))
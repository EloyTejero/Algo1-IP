longitud::[t]->Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo::[t]->t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio::[t]->[t]
principio [x] = []
principio (x:xs) = x : principio xs

reverso::[t]->[t]
reverso [] = []
reverso l = ultimo l : reverso (eliminarUltimo(l))

eliminarUltimo::[t]->[t]
eliminarUltimo [x] = []
eliminarUltimo (x:xs) = x : eliminarUltimo xs
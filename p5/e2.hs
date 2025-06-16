pertenece::(Eq t)=>t->[t]->Bool
pertenece _ [] = False
pertenece r (x:xs) = r == x || pertenece r xs

todosIguales::(Eq t)=>[t]->Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:ls) = x == y && todosIguales (y:ls) 

todosDistintos::(Eq t)=>[t]->Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) = verificarDistintosEnLista x xs && todosDistintos xs

verificarDistintosEnLista::(Eq t)=>t->[t]->Bool
verificarDistintosEnLista _ [] = True
verificarDistintosEnLista e [x] = e /= x
verificarDistintosEnLista e (x:xs) = e /= x && verificarDistintosEnLista e xs

{- forma larga y al pedo de hacer todos distintos
todosDistintos l = comprobarIgualdadEnLista l 1 
comprobarIgualdadEnLista::(Eq t)=>[t]->Integer->Bool
comprobarIgualdadEnLista l i    | cantidadElementos l < i = True
                                | otherwise = igualdadEnElemento (elementoNDeLista l i)  (eliminarPosicionN l i) && comprobarIgualdadEnLista l (i+1)

igualdadEnElemento::(Eq t)=>t->[t]->Bool
igualdadEnElemento q [x] = q /= x
igualdadEnElemento q (x:xs) = q /= x && igualdadEnElemento q xs
-}
cantidadElementos::[t]->Integer
cantidadElementos [] = 0
cantidadElementos (x:xs) = 1 + cantidadElementos xs

elementoNDeLista::[t]->Integer->t
elementoNDeLista (x:xs) 1 = x
elementoNDeLista (x:xs) n = elementoNDeLista xs (n-1)

eliminarPosicionN::[t]->Integer->[t]
eliminarPosicionN [] _ = []
eliminarPosicionN (x:xs) n | n==1 = xs | otherwise = x : eliminarPosicionN xs (n-1)

-- ej 4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:xs) = not (verificarDistintosEnLista x xs) || hayRepetidos xs

-- ej 5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e xs

-- punto 6
quitarTodos :: (Eq t)=> t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs

-- punto 7
eliminarRepetidos::(Eq t)=> [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)  
    | hayRepetidosDe x xs = eliminarRepetidos xs
    | otherwise = x : eliminarRepetidos xs

hayRepetidosDe::(Eq t)=>t->[t]->Bool
hayRepetidosDe _ [] = False
hayRepetidosDe e (x:xs) = e == x || hayRepetidosDe e xs

-- punto 8 
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos ls ts = tieneLosMismosElementos ls ts && tieneLosMismosElementos ts ls

tieneLosMismosElementos ::(Eq t)=> [t] -> [t] -> Bool
tieneLosMismosElementos [x] l = pertenece x l
tieneLosMismosElementos (x:xs) l = pertenece x l && tieneLosMismosElementos xs l

--punto 9
esCapicua :: (Eq t) => [t] -> Bool
esCapicua [] = True
esCapicua [x] = True
esCapicua l = head l == ultimo l && esCapicua (sacarPrimeroYUltimo l)

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

sacarPrimeroYUltimo :: [t] -> [t]
sacarPrimeroYUltimo (x:xs) = sacarUltimo xs

sacarUltimo :: [t] -> [t]
sacarUltimo [x] = []
sacarUltimo (x:xs) = x : sacarUltimo xs
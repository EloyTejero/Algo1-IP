type Fila = [Integer]
type Tablero = [Fila]
type Posicion = (Integer, Integer)
type Camino = [Posicion]


--5)
maximo :: Tablero -> Integer
maximo [f] = maximoFila f
maximo (f1:f2:fs)
    | maximoFila f1 >= maximoFila f2 = maximo (f1:fs)
    | otherwise = maximo (f2:fs)

maximoFila :: Fila -> Integer
maximoFila [x] = x
maximoFila (x:y:xs)
    | x >= y = maximoFila (x:xs)
    | otherwise = maximoFila (y:xs)

--6)
masRepetido :: Tablero -> Integer
masRepetido x = maximoDeRepetidos (agruparPorRepetidos (juntarValoresDeTabla x))

maximoDeRepetidos :: [(Integer, Integer)] -> Integer
maximoDeRepetidos [x] = fst x
maximoDeRepetidos (x:y:xs)
    | snd x >= snd y = maximoDeRepetidos (x:xs)
    | otherwise = maximoDeRepetidos (y:xs)

agruparPorRepetidos ::(Eq t)=> [t] -> [(t, Integer)]
agruparPorRepetidos [] = []
agruparPorRepetidos (x:xs) = (x, (vecesRepetido xs x)) : (agruparPorRepetidos (eliminarDeLista xs x))

vecesRepetido :: (Eq t) => [t] -> t -> Integer
vecesRepetido [] _ = 0
vecesRepetido (x:xs) e 
    | x == e = 1 + vecesRepetido xs e
    | otherwise = vecesRepetido xs e

eliminarDeLista :: (Eq t) => [t] -> t -> [t]
eliminarDeLista [] _ = []
eliminarDeLista (x:xs) e 
    | x == e = eliminarDeLista xs e
    | otherwise = x : eliminarDeLista xs e

juntarValoresDeTabla :: Tablero -> [Integer]
juntarValoresDeTabla [x] = x
juntarValoresDeTabla (x:xs) = x ++ juntarValoresDeTabla xs

--7)
valoresCamino :: Tablero -> Camino -> [Integer]
valoresCamino _ [] = []
valoresCamino t (x:xs) = obtenerValorPosicion t x : valoresCamino t xs

obtenerValorPosicion :: Tablero -> Posicion -> Integer
obtenerValorPosicion t (fila, columna) = obtenerColumna (obtenerFila t fila) columna

obtenerFila :: Tablero -> Integer -> Fila
obtenerFila (x:xs) 1 = x
obtenerFila (x:xs) n = obtenerFila xs (n-1)

obtenerColumna :: Fila -> Integer -> Integer
obtenerColumna (x:xs) 1 = x
obtenerColumna (x:xs) n = obtenerColumna xs (n-1)

--8)
esCaminoFibo :: [Integer] -> Integer -> Bool
esCaminoFibo [x] i = fibo(i) == x
esCaminoFibo (x:xs) i = fibo(i) == x && esCaminoFibo xs (i+1)

fibo :: Integer -> Integer
fibo 0 = 0
fibo 1 = 1
fibo n = fibo(n-1) + fibo(n-2)
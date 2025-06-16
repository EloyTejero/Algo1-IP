-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }

mediaMovilN :: [Integer] -> Integer -> Float
mediaMovilN lista n = promedio (ultimosNelementos lista n) n

promedio :: [Integer] -> Integer -> Float
promedio [x] n = fromInteger(x) / fromInteger(n)
promedio (x:y:xs) n = promedio ((x+y):xs) n

ultimosNelementos :: (Eq t) => [t] -> Integer -> [t]
ultimosNelementos (x:xs) n 
    | n == longitud (x:xs) = (x:xs)
    | otherwise = ultimosNelementos xs n

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3].

esAtractivo :: Integer -> Bool
esAtractivo n = esPrimo (longitud (factores n))

factores :: Integer -> [Integer]
factores 1 = []
factores n = primerPrimoDivisor n 2 : factores (div n (primerPrimoDivisor n 2))

primerPrimoDivisor :: Integer -> Integer -> Integer
primerPrimoDivisor n i 
    | mod n i == 0 = i
    | otherwise = primerPrimoDivisor n (siguientePrimo (i+1))

siguientePrimo :: Integer -> Integer
siguientePrimo p
    | esPrimo p = p
    | otherwise = siguientePrimo (p+1)

esPrimo :: Integer -> Bool
esPrimo n 
    | n < 2 = False
    | otherwise = recorrerHastaPrimo n 2

recorrerHastaPrimo :: Integer -> Integer -> Bool
recorrerHastaPrimo n i
    | n == i = True
    | mod n i == 0 = False -- otherwise = mod n i /= 0 && recorrerHastaPrimo n (i+1)
    | otherwise = recorrerHastaPrimo n (i+1)


-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True.

palabraOrdenada :: [Char] -> Bool
palabraOrdenada palabra = estaOrdenado (palabraSinBlancos palabra)

palabraSinBlancos :: [Char] -> [Char]
palabraSinBlancos [] = []
palabraSinBlancos (x:xs)
    | x == ' ' = palabraSinBlancos xs
    | otherwise = x : palabraSinBlancos xs

estaOrdenado :: [Char] -> Bool
estaOrdenado [] = False
estaOrdenado [x] = True
estaOrdenado (x:y:xs) = x <= y && estaOrdenado (y:xs)

-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}e
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }

similAnagrama :: [Char] -> [Char] -> Bool
similAnagrama p1 p2 = sonAnagramas (palabraSinBlancos (p1)) (palabraSinBlancos (p2))

sonAnagramas :: [Char] -> [Char] -> Bool
sonAnagramas p1 p2 
    | p1 == p2 = False
    | otherwise = (longitud p1 == longitud p2) && mismasAparicionesDeLetras p1 p2

mismasAparicionesDeLetras :: [Char] -> [Char] -> Bool
mismasAparicionesDeLetras [] _ = True
mismasAparicionesDeLetras (x:xs) p2 = (apariciones x (x:xs)) == (apariciones x p2) && mismasAparicionesDeLetras (sacar x xs) p2

apariciones :: (Eq t) => t -> [t] -> Integer
apariciones _ [] = 0
apariciones e (x:xs) 
    | x == e = 1 + apariciones e xs
    | otherwise = apariciones e xs

sacar :: (Eq t) => t -> [t] -> [t]
sacar _ [] = []
sacar e (x:xs)
    | e == x = sacar e xs
    | otherwise = x : sacar e xs
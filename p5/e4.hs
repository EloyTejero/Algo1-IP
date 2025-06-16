--a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) 
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

--b)
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras l = contarPalabrasSinEspaciosDobles (sacarBlancosDelPrincipio (sacarBlancosRepetidos l))

sacarBlancosDelPrincipio :: [Char] -> [Char]
sacarBlancosDelPrincipio [] = []
sacarBlancosDelPrincipio (x:xs) 
    | x == ' ' = sacarBlancosDelPrincipio xs
    | otherwise = (x:xs)

contarPalabrasSinEspaciosDobles :: [Char] -> Integer
contarPalabrasSinEspaciosDobles [x] = 1
contarPalabrasSinEspaciosDobles (x:xs) 
    | x == ' ' = 1 + contarPalabrasSinEspaciosDobles xs
    | otherwise = contarPalabrasSinEspaciosDobles xs

--c)
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras ls = primeraPalabra(sacarBlancosDelPrincipio ls) : palabras (eliminarPrimeraPalabra (sacarBlancosDelPrincipio(sacarBlancosRepetidos(ls))))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (' ':xs) = []
primeraPalabra (x:xs) = x : primeraPalabra xs

eliminarPrimeraPalabra :: [Char] -> [Char]
eliminarPrimeraPalabra [] = []
eliminarPrimeraPalabra (' ':xs) = xs
eliminarPrimeraPalabra (x:xs) = eliminarPrimeraPalabra xs

--d)
palabraMasLarga :: [[Char]] -> [Char]
palabraMasLarga [x] = x
palabraMasLarga (x:y:xs) 
    | longitud x >= longitud y = palabraMasLarga (x:xs)
    | otherwise = palabraMasLarga (y:xs)

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--e)
aplanar :: [[Char]] -> [Char]
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs

--f)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ " " ++ aplanar xs

--g)
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ generarNBlancos n ++ aplanar xs

generarNBlancos :: Integer -> [Char]
generarNBlancos 0 = []
generarNBlancos n = ' ' : generarNBlancos (n-1)
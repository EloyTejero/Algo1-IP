--9)
divisoresPropios :: Integer -> [Integer]
divisoresPropios n = buscarDivisoresPropios n 1

buscarDivisoresPropios :: Integer -> Integer -> [Integer]
buscarDivisoresPropios n i 
    | n == i = []
    | mod n i == 0 = i : buscarDivisoresPropios n (i+1)
    | otherwise = buscarDivisoresPropios n (i+1)

--10)
sonAmigos :: Integer -> Integer -> Bool
sonAmigos n m = (sumaLista (divisoresPropios n)) == m && (sumaLista (divisoresPropios m)) == n

sumaLista :: [Integer] -> Integer
sumaLista [] = 0
sumaLista (x:xs) = x + sumaLista xs

--11)
losPrimerosNPerfectos :: Integer -> [Integer]
losPrimerosNPerfectos 1 = [6]
losPrimerosNPerfectos n = enesimoPerfecto(n) : losPrimerosNPerfectos(n-1)

enesimoPerfecto :: Integer -> Integer
enesimoPerfecto 1 = 6
enesimoPerfecto n = siguientePerfecto(enesimoPerfecto (n-1) + 1)

siguientePerfecto :: Integer -> Integer
siguientePerfecto n 
    | esPerfecto n = n
    | otherwise = siguientePerfecto (n+1) 

esPerfecto :: Integer -> Bool
esPerfecto n = sumaLista (divisoresPropios n) == n

--12)
listaDeAmigos :: [Integer] -> [(Integer, Integer)]
listaDeAmigos [x] = []
listaDeAmigos (x:xs) = amigosDeNConLista x xs ++ listaDeAmigos xs

amigosDeNConLista :: Integer -> [Integer] -> [(Integer, Integer)]
amigosDeNConLista _ [] = []
amigosDeNConLista n (x:xs) 
    | sonAmigos n x = (n, x) : amigosDeNConLista n xs
    | otherwise = amigosDeNConLista n xs
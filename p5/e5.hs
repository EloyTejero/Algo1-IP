--1)
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = x : sumaAcumulada ((x+y):xs)

--2)
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponerNenPrimos x) : descomponerEnPrimos xs

descomponerNenPrimos :: Integer -> [Integer]
descomponerNenPrimos 1 = []
descomponerNenPrimos n = primerPrimoDivisor n 1 : descomponerNenPrimos (div n (primerPrimoDivisor n 1)) 

primerPrimoDivisor :: Integer -> Integer -> Integer
primerPrimoDivisor n m
    | mod n (enesimoPrimo m) == 0 = enesimoPrimo m 
    | otherwise = primerPrimoDivisor n (m+1)  

enesimoPrimo :: Integer -> Integer
enesimoPrimo 1 = 2
enesimoPrimo n = siguientePrimo(enesimoPrimo(n-1) + 1)

siguientePrimo :: Integer -> Integer
siguientePrimo n    | esPrimo n = n
                    | otherwise = siguientePrimo (n+1)

esPrimo :: Integer -> Bool
esPrimo 2 = True
esPrimo n = recorrerHastaPrimo n 2

recorrerHastaPrimo :: Integer -> Integer -> Bool
recorrerHastaPrimo n i | n == i = True
                       | otherwise = mod n i /= 0 && recorrerHastaPrimo n (i + 1)

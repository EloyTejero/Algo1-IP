{-res = true <=> n es igual a la suma de los m primeros numeros primos para algun m-}

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n | n <= 1 = False
                        | otherwise = esSumaDePrimerosKPrimos n 1 

esSumaDePrimerosKPrimos :: Integer -> Integer -> Bool
esSumaDePrimerosKPrimos n i     | sumaKPrimos i > n = False
                                | sumaKPrimos i == n = True
                                | otherwise = esSumaDePrimerosKPrimos n (i+1)

sumaKPrimos :: Integer -> Integer
sumaKPrimos 1 = 2
sumaKPrimos n = enesimoPrimo n + sumaKPrimos (n - 1)

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
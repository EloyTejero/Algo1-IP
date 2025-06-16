{-a)menor divisor-}

--a)
menorDivisor :: Integer -> Integer
--menorDivisor 1 = 1 --porque el enunciado dice mayor a 1 sino seria valido
menorDivisor = buscarDivisor 2

buscarDivisor :: Integer -> Integer -> Integer
buscarDivisor i n   | mod n i == 0 = i
                    | otherwise = buscarDivisor (i+1) n
-- si bien el valor que vamos usando va creciendo, se va acercando al caso base (mod n i == 0). Entonces incrementalmente en algun momento va a llegar a ser n y n siempre divide a n entonces si o si se alcanza el caso base
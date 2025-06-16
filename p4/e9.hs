{-
problema esCapicua(n: Z): Bool {
    requiere { n>=0}
    asegura {True <=> para todo numero que sea capicua}
}
-}

{-
si el numero es de un digito es capicua, si es de dos digitos es capicua solo si ambos digitos son iguales.Applicative
si tiene mas de dos digitos entonces si el ultimo y primer digito son iguales sacarles ambos digitos y dejar el del medio y pasarlo por la funcion recursivamente
achicando la situacion a numeros cada vez mas chicos hasta llegar al caso base.
-}

esCapicua :: Integer -> Bool
esCapicua n 
    | cantDigitos n == 1 = True
    | cantDigitos n == 2 = sonPrimeroYultimoIguales n
    | otherwise = sonPrimeroYultimoIguales n && esCapicua (sacarPrimeroYultimo n)

sonPrimeroYultimoIguales :: Integer -> Bool
sonPrimeroYultimoIguales n = (mod n 10) == (div n (10 ^ (cantDigitos n - 1)))

{-
sacarPrimeroYultimo
-}

sacarPrimeroYultimo :: Integer -> Integer
sacarPrimeroYultimo n = div (mod n (10^((cantDigitos n) - 1))) 10

cantDigitos :: Integer -> Integer
cantDigitos 0 = 0
cantDigitos n = 1 + cantDigitos(div n 10)
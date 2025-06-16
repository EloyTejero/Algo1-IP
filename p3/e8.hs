{-
Implementar la función comparar :: Integer -> Integer -> Integer
problema comparar (a : Z, b : Z) : Z {
    requiere: {T rue}
    asegura: {(res = 1) ↔ (sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
    asegura: {(res = −1) ↔ (sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
    asegura: {(res = 0) ↔ (sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
}
problema sumaUltimosDosDigitos (x : Z) : Z {
    requiere: {T rue}
    asegura: {res = (|x| mód 10) + ( (|x|/10) mód 10)}
}
-}
comparar :: Integer -> Integer -> Integer
comparar a b
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos n = mod (abs n) 10 + mod (div (abs n) 10) 10  
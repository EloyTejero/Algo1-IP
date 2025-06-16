{-
Ejercicio 8. Especificar e implementar la funci´on sumaDigitos :: Integer->Integer que calcula la suma de d´ ıgitos de
 un n´ umero natural. Para esta funci´on pueden utilizar div y mod.
sumaDigitos (n: Z): Z{
    requiere: {True}
    asegura: {resultado = la sumatoria de todos los digitos de n}
}
-}

sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod (abs(n)) 10 + sumaDigitos (div (abs(n)) 10)
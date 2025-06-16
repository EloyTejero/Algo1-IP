{-Ej 2 a-}
{-
    funcion absoluto(n:Z) -> Z{
        requiere {True}
        Asegura {res>=0}
    }
-}

absoluto :: Integer -> Integer
absoluto 0 = 0
absoluto n 
    | n > 0 = n 
    | n < 0 = n * (-1)


{-
ejercicio 2b que numero es mas grand
    funcion maximoAbsoluto(n:Z) -> Z{
        requiere{True}
        Asegura{res pertenece a enteros}
    }
-}
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto a b
    | a == b = b
    | a < b = b
    | a > b = a 

{-
2c) maximo de tres numeros
-}

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c = maximoAbsoluto (maximoAbsoluto a b) c

{-
2d) algunoEsCero con y sin patternmatching
-}

algunoEsCeroPattern :: Integer -> Integer -> Bool
algunoEsCeroPattern 0 _ = True
algunoEsCeroPattern _ 0 = True
algunoEsCeroPattern _ _ = False

algunoEsCero :: Integer -> Integer -> Bool
algunoEsCero a b
    | a == 0 || b == 0 = True
    | otherwise = False

{- ambosSonCero con y sin patternmatching -}
-- sin pattern
ambosSonCero :: Integer -> Integer -> Bool
ambosSonCero a b
    | a == 0 && b == 0 = True
    | otherwise = False

--con pattern
ambosSonCeroPattern :: Integer -> Integer -> Bool
ambosSonCeroPattern 0 0 = True
ambosSonCeroPattern _ _ = False

{- f) enMismoIntervalo: dados dos n´umeros reales, indica si est´an relacionados por la relaci´on de equivalencia en R cuyas
clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞), o dicho de otra manera, si pertenecen al mismo intervalo.-}
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo a b
    | a > 7 && b > 7 = True
    | a <= 3 && b <= 3 = True
    | a > 3 && a <=7 && b>3 && b<=7 = True
    | otherwise = False

{- g) sumaDistintos: que dados tres n´umeros enteros calcule la suma sin sumar repetidos (si los hubiera)-}
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | a /= b && b /= c && c /= a = a + b + c

{- h) esMultiploDe: dados dos n´umeros naturales, decide si el primero es m´ultiplo del segundo. -}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b | (mod a b) == 0 = True | otherwise = False

{-i) digitoUnidades: dado un n´umero entero, extrae su d´ıgito de las unidades.-}
digitoUnidades :: Integer -> Integer 
digitoUnidades x = div x 10 -- Interprete de eliminar la cifra del numero y dejar lo que queda pero en realidad era devolver el valor de la unidad por lo que seria mod n 10

{-j) digitoDecenas: dado un n´umero entero mayor a 9, extrae su d´ıgito de las decenas.-}
digitoDecenas :: Integer -> Integer
digitoDecenas x = (div x 100) * 10 + (x - ((div x 10)*10)) -- aca lo mismo si queremos devolver unicamente el digito de la decenas haria el mod n 100 y lo pasaria a div n 10 cosa de que elimino la centena y saco la cantidad de decenas, tambien se podria directamente div n 10 y de eso devuelvo la unidad como en el ejercicio anterior, mod (div n 10) 10 o div (mod n 100) 10 esta ultima me parece mejor porque soporta si le pasas numeros menores a 100
-- (x - ((div x 10)*10) es la unidad, entonces con (div x 100) * 10 elimino de la decena para atras (y se suma un 0 por el * 10) y le sumo la unidad
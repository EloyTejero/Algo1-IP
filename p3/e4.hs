{-Especificar e implementar las siguientes funciones utilizando tuplas para representar pares y ternas de
 n´ umeros.-}

-- a) productoInterno: calcula el producto interno entre dos tuplas de R × R.
{- problema productoInterno(t1:(R, R), t2:(R, R):R){
        Requiere{True}
        Asegura{res = t1 x t2}
    }
-}

productoInterno :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer)
productoInterno (a,b) (c, d) = (a*c, b*d)

{-  b) esParMenor: dadas dos tuplas de R × R, decide si cada coordenada de la primera tupla es menor a la coordenada
 correspondiente de la segunda tupla.
-}

esParMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
esParMenor (a,b) (c,d) | a<c && b<d = True | otherwise = False

{-c) distancia: calcula la distancia eucl´ ıdea entre dos puntos de R^2-}
-- a^2 + b^2 = c^2 
-- sqrt(a^2 + b^2) = c

distancia :: (Integer, Integer) -> (Integer, Integer) -> Float
distancia (a,b) (c,d) = sqrt (fromIntegral (((c - a)^2) + ((d - b)^2)))

{-d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos-}
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a, b, c) = a+b+c

{- e) sumarSoloMultiplos: dada una terna de n´umeros enteros y un natural, calcula la suma de los elementos de la terna que
 son m´ ultiplos del n´ umero natural.-}

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n
    | mod a n == 0 && mod b n == 0 && mod c n == 0 = a+b+c
    | mod a n /= 0 = sumarSoloMultiplos (b,c,0) n
    | otherwise = sumarSoloMultiplos (b, c, a) n

{-f) posPrimerPar: dada una terna de enteros, devuelve la posici´on del primer n´umero par si es que hay alguno, o devuelve
 4 si son todos impares.-}

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | mod a 2 == 0 = 1 | mod b 2 == 0 = 2 | mod c 2 == 0 = 3 | otherwise = 4

{-g) crearPar :: a-> b-> (a, b): a partir de dos componentes, crea un par con esos valores. Debe funcionar para ele
mentos de cualquier tipo.-}

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

{- h) invertir :: (a, b)-> (b, a): invierte los elementos del par pasado como par´ametro. Debe funcionar para elementos
 de cualquier tipo.-}

invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

{-i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos:
 type Punto2D = (Float, Float)-}

type Punto2D = (Float, Float)
esParMenor2 :: Punto2D -> Punto2D -> Bool
esParMenor2 (a,b) (c,d) | a<c && b<d = True | otherwise = False

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (a,b) (c,d) = sqrt (((c - a)^2) + ((d - b)^2))
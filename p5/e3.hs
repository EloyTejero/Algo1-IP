-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

--2)
productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x:xs) = x * productoria xs

--3)
maximo::[Integer]->Integer
maximo [x] = x
maximo (y:x:xs)
    | y >= x = maximo (y:xs)
    | otherwise = maximo (x:xs)

--4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = n+x : sumarN n xs

--5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo l = sumarN (ultimo l) l

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | mod x 2 == 0 = x : pares xs
    | otherwise = pares xs

--8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN m (x:xs) 
    | mod x m == 0 = x : multiplosDeN m xs
    | otherwise = multiplosDeN m xs


--9)
--ordenar de forma creciente
ordenar::[Integer]->[Integer]
ordenar [] = []
ordenar l = minimo l : ordenar (quitar l (minimo l)) 
-- ordenar l = ordenar(quitar l maximo l) ++ [maximo l] -- con operador ++
-- ordenar l = ordenar maximo l : ordenar (quitar l (maximo l)) -- mayor a menor

--reverso pero con operador ++
reverso2::[t]->[t]
reverso2 [] = []
reverso2 (x:xs) = reverso2 xs ++ [x]

minimo::[Integer]->Integer
minimo [x] = x
minimo (y:x:xs) 
    | y <= x = minimo (y:xs)
    | otherwise = minimo (x:xs) 

quitar::(Eq t)=>[t]->t->[t]
quitar [] _ = []
quitar (x:xs) e | x == e = quitar xs e | otherwise = x : quitar xs e
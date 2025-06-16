module SolucionT2 where

--comprobande de parcial: 5xmt1JTZ

type Mapeo = [(Char, Char)]
type Frase = [Char]

--1)
hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar caracter ((char, reemplazo):xs)
    | caracter == char = True
    | otherwise = hayQueCodificar caracter xs

--2)
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar caracter frase mapeo 
    | not (hayQueCodificar caracter mapeo) = 0
    | otherwise = cantidadDeRepetidosDeK caracter frase

cantidadDeRepetidosDeK :: Char -> [Char] -> Int
cantidadDeRepetidosDeK _ [] = 0
cantidadDeRepetidosDeK c (x:xs)
    | c == x = 1 + cantidadDeRepetidosDeK c xs
    | otherwise = cantidadDeRepetidosDeK c xs

--3)
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar [] _ = ' '
laQueMasHayQueCodificar frase map = mayorCharEnTupla (separarEnTuplasPorRepetidos (dejarSoloLosMapeables frase map))

dejarSoloLosMapeables :: [Char] -> [(Char, Char)] -> [Char]
dejarSoloLosMapeables [] _ = []
dejarSoloLosMapeables (x:xs) map
    | hayQueCodificar x map = x : dejarSoloLosMapeables xs map
    | otherwise = dejarSoloLosMapeables xs map

separarEnTuplasPorRepetidos :: [Char] -> [(Char, Int)]
separarEnTuplasPorRepetidos [] = []
separarEnTuplasPorRepetidos (x:xs) = (x, cantidadDeRepetidosDeK x xs + 1) : separarEnTuplasPorRepetidos (eliminarKDeLista xs x)

eliminarKDeLista :: (Eq t) => [t] -> t -> [t]
eliminarKDeLista [] _ = []
eliminarKDeLista (x:xs) k
    | x == k = eliminarKDeLista xs k
    | otherwise = x : eliminarKDeLista xs k

mayorCharEnTupla :: [(Char, Int)] -> Char
mayorCharEnTupla [x] = fst x
mayorCharEnTupla ((x, cantx):(y, canty):xs)
    | cantx >= canty = mayorCharEnTupla ((x,cantx):xs)
    | otherwise = mayorCharEnTupla ((y,canty):xs)

--4)
codificarFrase :: [Char] -> [(Char,Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (x:xs) map = codificarChar x map : codificarFrase xs map

codificarChar :: Char -> [(Char, Char)] -> Char
codificarChar c [] = c
codificarChar c ((char, reemplazo):xs)
    | c == char = reemplazo
    | otherwise = codificarChar c xs
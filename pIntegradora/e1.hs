type Nombre = [Char]
type Mercaderia = [Nombre]
type Stock = [(Nombre, Integer)]
type Precios = [(Nombre, Float)]

--1)
generarStock :: Mercaderia -> Stock
generarStock [] = []
generarStock (x:xs) = (x, cantidadDeItemsXEnLista x (x:xs)) : generarStock (sacarXDeLista x xs)

cantidadDeItemsXEnLista :: (Eq t) => t -> [t] -> Integer
cantidadDeItemsXEnLista _ [] = 0
cantidadDeItemsXEnLista e (x:xs)
    | x == e = 1 + cantidadDeItemsXEnLista e xs 
    | otherwise = cantidadDeItemsXEnLista e xs

sacarXDeLista :: (Eq t) => t -> [t] -> [t]
sacarXDeLista _ [] = []
sacarXDeLista e (x:xs)
    | e == x = sacarXDeLista e xs
    | otherwise = x : sacarXDeLista e xs

--2)
stockDeProducto :: Stock -> Nombre -> Integer
stockDeProducto [] _ = 0
stockDeProducto ((nombre, cantidad):xs) producto
    | nombre == producto = cantidad
    | otherwise = stockDeProducto xs producto

--3)
dineroEnStock :: Stock -> Precios -> Float
dineroEnStock [] _ = 0
dineroEnStock ((nombreProducto, cantidad):xs) precios = (precioProducto nombreProducto precios) * fromIntegral(cantidad) + dineroEnStock xs precios 

precioProducto :: Nombre -> Precios -> Float
precioProducto _ [] = 0
precioProducto producto ((nombre, precio):xs)
    | nombre == producto = precio
    | otherwise = precioProducto producto xs

--4)
aplicarOferta :: Stock -> Precios -> Precios
aplicarOferta _ [] = []
aplicarOferta stock ((nombre, precio):xs)
    | stockDeProducto stock nombre > 10 = (nombre, (precio*0.8)) : aplicarOferta stock xs
    | otherwise = (nombre,precio) : aplicarOferta stock xs
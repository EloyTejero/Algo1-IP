type Identificacion = Integer
type Ubicacion = [Char]
type Disponibilidad = Bool
type Estado = (Ubicacion, Disponibilidad)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]

existeElLocker::Identificacion->MapaDeLockers->Bool
existeElLocker _ [] = False
existeElLocker id (x:xs) = fst x == id || existeElLocker id xs

ubicacionDelLocker::Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker id ((i, (ubi, disp)):xs) 
    | id == i = ubi
    | otherwise = ubicacionDelLocker id xs

estaDisponibleElLocker::Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker id ((i, (ubi, estado)):xs)
    | id == i = estado
    | otherwise = estaDisponibleElLocker id xs

ocuparLocker::Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker id ((i, (ubi, estado)):xs)
    | id == i  && not estado = (i, (ubi, True)):xs
    | otherwise = (i, (ubi, estado)) : ocuparLocker id xs
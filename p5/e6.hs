type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos::Nombre->ContactosTel->Bool
enLosContactos _ [] = False
enLosContactos nombre (x:xs) = nombre == fst x || enLosContactos nombre xs

agregarContacto::Contacto->ContactosTel->ContactosTel
agregarContacto contacto [] = [contacto]
agregarContacto (nombre, tel) (x:xs) --tambien se puede ((n,t):xs)
    | fst x == nombre = (nombre, tel) : xs 
    | otherwise = x : agregarContacto (nombre, tel) xs

eliminarContacto::Contacto->ContactosTel->ContactosTel
eliminarContacto _ [] = []
eliminarContacto (n, t) ((nom, tel):xs)
    | n == nom = xs
    | otherwise = (nom, tel): eliminarContacto (n, t) xs
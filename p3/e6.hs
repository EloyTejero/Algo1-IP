{-
type Anio = Integer
type EsBisiesto = Bool
Programar la función bisiesto :: Anio -> EsBisiesto según la siguiente especificación:
problema bisiesto (año : Z) : Bool {
    requiere: {T rue}
    asegura: {(res = f alse) ↔ (año no es múltiplo de 4, o bien, año es múltiplo de 100 pero no de 400)}
}
-}

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto n = (mod n 4 == 0) && (mod n 400 == 0 || mod n 100 /= 0)

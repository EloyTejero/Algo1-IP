{-
a) Implementar la función:
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
    requiere: {T rue}
    asegura: {res = sumatoria desde i=0 hasta 2 tal que |pi − qi |}
}
-}

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = abs(a-d) + abs(b-e) + abs(c-f)
-- taria bueno hacerlo con recursion

--b) Reimplementar la función teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
type Punto3D = (Float, Float, Float)
distanciaManhattan2 :: Punto3D -> Punto3D -> Float
distanciaManhattan2 (a,b,c) (d,e,f) = abs(a-d) + abs(b-e) + abs(c-f)
{-
Implementar una funci´on estanRelacionados :: Integer -> Integer -> Bool
problema estanRelacionados (a : Z, b : Z) : Bool {
requiere: {a ̸= 0 ∧ b ̸= 0}
asegura: {(res = true) ↔ (a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k ̸= 0)}
}
-}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b
    | ((a*a) - ((div((a*a))(a*b))*(a*b))) == 0 = True
    | otherwise = False
-- al buscar k = (-(a*a))/(a*b)
-- si mi numero es con coma entonces no habia resultado para los enteros
-- entonces hago la division entera y multiplico por el divisor, lo que deberia dar el dividendo
-- por lo que al restarle eso al dividendo deberia dar 0, sino, era un numero con coma, siempre que los numeros iniciales son enteros (pero ya lo tenemos por las precondiciones)
-- si se siguiera la ecuacion deberia ser la division entera de -(a*a), y habria que sumar, en lugar de restar ya que el cociente seria negativo, por eso con los signos invertidos da el mismo resultado, no hace diferencia.
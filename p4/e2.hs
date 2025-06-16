parteEntera :: Float -> Integer
parteEntera n 
    | n < 1 = 0 
    | otherwise = 1 + parteEntera(n-1)

{-
parteEntera :: Float -> Integer
parteEntera x = parteEnteraAux 0 x

parteEnteraAux :: Integer -> Float -> Integer
parteEnteraAux n x
    | n <= x && (n+1) > x = n
    | otherwise = parteEnteraAux (n + 1) x
este ejemplo no terminaría siendo recursion porque no estas pensando en reduccion, en ir a un caso base. Se vuelve mas complejo en vez de mas simple para reducir,
es decir, hacer operaciones como ir incrementando los valores es abarcar conjuntos mas grandes, ademas que la definicion de caso base aca esta ligada a una variable
por una cuestion de reduccion y complejidad no entra en recursividad, aunque si funciona.
-}

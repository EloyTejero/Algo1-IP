{-
problema esDivisible(a,b:R):Bool{
    requiere{true}
    asegura{res=true <=> a = kb, b e Z }
}
-}

esDivisible :: Integer -> Integer -> Bool
esDivisible a b 
    | a == b = True 
    | b > a = False 
    | otherwise = esDivisible (a-b) (b)
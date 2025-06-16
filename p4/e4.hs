{- Especificar e implementar la funci´on sumaImpares :: Integer->Integer que dado n ∈ N sume los primeros
 n n´ umeros impares. Por ejemplo: sumaImpares 3 
1+3+5 ⇝ 9.-}

sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = sumaImpares(n-1) + n * 2 - 1 
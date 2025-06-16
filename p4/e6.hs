{-
6. Implementar la funci ́on todosDigitosIguales :: Integer ->Bool que determina si todos los d ́ıgitos de un
n ́umero natural son iguales, es decir:
problema todosDigitosIguales (n: Z) : B {
requiere: { n > 0 }
asegura: { resultado = true ↔ todos los d ́ıgitos de n son iguales }
}
-}

todosDigitosIguales::Integer->Bool
todosDigitosIguales n | div n 10 == 0 = True
todosDigitosIguales n = (mod n 10 == (mod (div n 10) 10)) && todosDigitosIguales (div n 10)

obtenerPrimerDigito :: Integer -> Integer
obtenerPrimerDigito n = mod n 10
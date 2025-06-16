f1::Integer->Integer
f1 0 = 1
f1 n = 2^(n) + f1(n-1)

f2::Integer->Float->Float
f2 1 q = q
f2 n q = q^n + f2 (n-1) q

f3::Integer->Float->Float
f3 n q = f3aux (2*n) q

f3aux::Integer->Float->Float
f3aux 1 q = q
f3aux n q = q^n + f3aux (n-1) q

f4::Integer->Float->Float
f4 n q = f4aux (2*n) n q

f4aux::Integer->Integer->Float->Float
f4aux n r q 
    | n == r = q
    | otherwise = q^n + f2 (n-1) q

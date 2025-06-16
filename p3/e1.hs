a1f :: Integer -> Integer
a1f 1 = 8
a1f 4 = 131
a1f 16 = 16

b1f :: Integer -> Integer
b1f 8 = 16
b1f 131 = 1
b1f 16 = 4

c1f :: Integer -> Integer
c1f n = a1f (b1f n)

d1f :: Integer -> Integer
d1f n = b1f (a1f n)
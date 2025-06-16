#ej 1
def uno_al_diez():
    i:int = 0
    while(i<10):
        i += 1
        print(i)
    
#uno_al_diez()

#ej 2
def pares_entre_10_y_40():
    i:int = 10
    while(i<=40):
        if(i%2==0):
            print(i)
        i += 1

#pares_entre_10_y_40()

#ej 3
def eco_10_veces():
    i:int = 10
    while(i>0):
        print("eco")
        i -= 1

#eco_10_veces()

#ej 4
def cuenta_regresiva(n:int):
    while(n>0):
        print(n)
        n -= 1
    print("Despegue")
#cuenta_regresiva(10)
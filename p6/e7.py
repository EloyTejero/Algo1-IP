import time
#ej 2
def pares_entre_10_y_40():
    for i in range (10, 41, 2):
        print(i)

pares_entre_10_y_40()

#ej 3
def cuenta_regresiva(n:int):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("Despegue")
cuenta_regresiva(10)
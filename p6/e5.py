#ej 1
def devolver_el_doble_si_es_par(n:int)->int:
    res:int = n
    if(n%2==0):
        res *= 2
    return res

#print(devolver_el_doble_si_es_par(9))

#ej 2
def devolver_valor_si_es_par_si_no_el_que_sigue(n:int)->int:
    res:int = n
    if(not n%2==0):
        res += 1
    
    return res

#print(devolver_valor_si_es_par_si_no_el_que_sigue(3))

#ej 3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int)->int:
    res:int = n
    if(n%3==0):
        if(n%9==0):
           res *= 3
        else:
            res *= 2
    return res

#print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))

#ej 4
def lindo_nombre(nombre:str):
    if(len(nombre)<5):
        print("Tu nombre tiene menos de 5 caracteres")
    else:
        print("Tu nombre tiene muchas letras")

#ej 5
def elRango(num:int):
    if(num<5):
        print("Menor a 5")
    elif(num>20):
        print("Mayor a 20")
    elif(num>=10 and num<=20):
        print("Entre 10 y 20")

#ej 6

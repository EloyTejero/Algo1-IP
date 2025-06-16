import random
from queue import LifoQueue as Pila

#PILAS
def copiar_pila(pila:Pila) -> Pila:
    new_pila:Pila = Pila()
    elementos:list = []
    while not pila.empty():
        elementos.append(pila.get())
    
    for i in range(len(elementos)-1, -1, -1):
        new_pila.put(elementos[i])
        pila.put(elementos[i])
    
    return new_pila

def mostrar_pila(pila:Pila) -> None:
    pila_copy:Pila = copiar_pila(pila)

    elementos:list = []
    while not pila_copy.empty():
        elementos.append(pila_copy.get())
    
    print(elementos)

def ver_siguiente_elemento(pila:Pila[any]) -> any:
    if not pila.empty():
        elemento:any = pila.get()
        pila.put(elemento)
        return elemento
    return None


#punto1
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res:Pila[int] = Pila()
    for i in range(cantidad):
        random_num:int = random.randint(desde, hasta)
        res.put(random_num)
    
    return res

#mostrar_pila(generar_nros_al_azar(5, 0, 10))

#punto 2
def cantidad_elementos(pila:Pila) -> int:
    #como es parametro in hay que copiar primero la pila

    pila_aux:Pila = copiar_pila(pila)
    cont:int = 0

    while not pila_aux.empty():
        pila_aux.get()
        cont += 1
    
    return cont

#pila2:Pila[int] = generar_nros_al_azar(2,0,10)
#mostrar_pila(pila2) #previo a la funcion
#print(cantidad_elementos(pila2))
#mostrar_pila(pila2) #previo a la funcion

#punto 3 pila de tipo IN
def buscar_el_maximo(pila:Pila[int]) -> int:
    pila_aux:Pila[int] = copiar_pila(pila)
    max = pila_aux.get()
    while not pila_aux.empty():
        elemento:int = pila_aux.get()
        if elemento > max:
            max = elemento 
    return max

#pila3:Pila[int] = generar_nros_al_azar(5,0,10)
#mostrar_pila(pila3)
#print(buscar_el_maximo(pila3))
#mostrar_pila(pila3)

#punto 4 pila tipo IN
def buscar_nota_maxima(pila:Pila[(str,int)]) -> tuple[str,int]:
    pila_aux:Pila[(str,int)] = copiar_pila(pila)
    mayor_nota:tuple[str,int] = pila_aux.get()
    while not pila_aux.empty():
        elemento:tuple[str,int] = pila_aux.get()
        if elemento[1] > mayor_nota[1]:
            mayor_nota = elemento
    
    return mayor_nota

# pila_notas:Pila[tuple[str,int]] = Pila()
# pila_notas.put(("1", 10))
# pila_notas.put(("2", 25))
# pila_notas.put(("xd", 20))
# print(buscar_nota_maxima(pila_notas))

#punto 5
def esta_bien_balanceado(ecuacion:str)->bool:
    pila_parentesis_de_apertura:Pila[chr] = Pila()
    pila_parentesis_de_cierre:Pila[chr] = Pila()
    contador_balance:int = 0
    for char in ecuacion:
        if char == '(':
            contador_balance += 1
            pila_parentesis_de_apertura.put(char)
        if char == ')':
            contador_balance -= 1
            pila_parentesis_de_cierre.put(char)
            if cantidad_elementos(pila_parentesis_de_apertura) < cantidad_elementos(pila_parentesis_de_cierre): #se podria haber usado un lista tranquilamente
                return False

    return contador_balance == 0 #si hay los mismos ( ) deberia quedar en 0

#print(esta_bien_balanceado("1 + ) 2 x 3 ( ( )"))
#print(esta_bien_balanceado("(()+())"))

#punto 6
#postfix
def evaluar_expresion(expresion:str) -> int:
    operando:str = ""
    pila_operandos:Pila[int] = Pila()
    expresion_lista:list = []
    for i in range(len(expresion)):
        if expresion[i] == '-':
            op2:int = pila_operandos.get()
            op1:int = pila_operandos.get()
            pila_operandos.put(op1 - op2)
        elif expresion[i] == '+':
            op2:int = pila_operandos.get()
            op1:int = pila_operandos.get()
            pila_operandos.put(op1 + op2)
        elif expresion[i] == '*':
            op2:int = pila_operandos.get()
            op1:int = pila_operandos.get()
            pila_operandos.put(op1 * op2)
        elif expresion[i] == '/':
            op2:int = pila_operandos.get()
            op1:int = pila_operandos.get()
            pila_operandos.put(op1 / op2)
        elif expresion[i] == ' ':
            if operando != "":
                pila_operandos.put(int(operando))
            operando=""
        else:
            operando+=expresion[i]
    
    return pila_operandos.get()

#print(evaluar_expresion("3 4 + 5 * 2 -"))

#punto 7 p1 y p2 son de tipo IN
def intercalar(p1:Pila, p2:Pila) -> Pila:
    p1_aux:Pila = copiar_pila(p1)
    p2_aux:Pila = copiar_pila(p2)
    p1_aux_invert:Pila = Pila()
    p2_aux_invert:Pila = Pila()
    res:Pila = Pila()

    while not p1_aux.empty():
        p1_aux_invert.put(p1_aux.get())
        p2_aux_invert.put(p2_aux.get())

    while not p2_aux_invert.empty():
        res.put(p1_aux_invert.get())
        res.put(p2_aux_invert.get())
    
    return res

p7:Pila = Pila()
p8:Pila = Pila()
p7.put(1)
p7.put(2)
p8.put(3)
p8.put(4)

#mostrar_pila(intercalar(p7,p8))
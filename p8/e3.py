#DICCIONARIOS
from queue import LifoQueue as Pila
from e1 import mostrar_pila

#punto 16
def calcular_promedio_por_estudiante(notas:list[tuple[str,float]]) -> dict[str,float]:
    promedios:dict[str,float] = {}
    for nota in notas:
        if not nota[0] in promedios.keys():
            promedio:int = calcular_promedio(notas,nota[0])
            promedios[nota[0]] = promedio
    return promedios

def calcular_promedio(notas:list[tuple[str,float]],nombre:str)->float:
    total:float = 0
    cont:int = 0
    for nota in notas:
        if nota[0] == nombre:
            total += nota[1]
            cont += 1
    return total/cont

# print(calcular_promedio_por_estudiante([("a",10),("u",10),("a",8),("a",5),("u",5)]))

#punto 17
def visitar_sitio(historiales:dict[str,Pila[str]], usuario:str, sitio:str) -> None:
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        pila:Pila[str] = Pila()
        pila.put(sitio)
        historiales[usuario] = pila

def navegar_hacia_atras(historiales:dict[str,Pila[str]], usuario:str) -> str:
    ultimo_sitio:str = historiales[usuario].get()
    return ultimo_sitio

# historiales:dict[str, Pila[str]] = {}
# pilaU1:Pila[str] = Pila()
# pilaU1.put("sitio1")
# historiales["user1"] = pilaU1
# pilaU2:Pila[str] = Pila()
# pilaU2.put("sitio2")
# historiales["user2"] = pilaU2
# for k in historiales.keys():
#     print("user:", k)
#     mostrar_pila(historiales[k])
# visitar_sitio(historiales, "user1", "sitio2")
# visitar_sitio(historiales, "user1", "sitio3")
# visitar_sitio(historiales, "user3", "sitiohola")
# visitar_sitio(historiales, "user2", "sitio3")
# for k in historiales.keys():
#     print("user:", k)
#     mostrar_pila(historiales[k])

# print(navegar_hacia_atras(historiales, "user3"))
# for k in historiales.keys():
#     print("user:", k)
#     mostrar_pila(historiales[k])

#Punto 18
def agregar_producto(inventario:dict[str,dict[str,float|int]],nombre:str,precio:float,cantidad:int) -> None:
    inventario[nombre] = {"precio":precio, "cantidad":cantidad}

def actualizar_stock(inventario:dict[str,dict[str,float|int]],nombre:str,cantidad:int) -> None:
    inventario[nombre]["cantidad"] = cantidad

def actualizar_precio(inventario:dict[str,dict[str,float|int]],nombre:str,precio:float) -> None:
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario:dict[str,dict[str,float|int]]) -> float:
    sum:float = 0
    for k in inventario.keys():
        sum += inventario[k]["precio"] * inventario[k]["cantidad"]
    return sum

# inventario:dict[str,dict[str,float|int]] = {}
# inventario["item1"] = {"precio":12, "cantidad":2}
# print(inventario)
# agregar_producto(inventario, "itemt", 5, 10)
# print(inventario)

# actualizar_stock(inventario, "itemt", 100)
# print(inventario)

# actualizar_precio(inventario, "itemt", 15.2)
# print(inventario)

# print(calcular_valor_inventario(inventario))
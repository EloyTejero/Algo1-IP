def peso_pino(cm:int) -> int:
    peso:int = 0
    if cm >= 300:
        peso = 900
        cm -= 300
        peso += cm *2
        cm = 0
    peso += cm * 3
    return peso

def es_peso_util(kg:int) -> bool:
    return kg >= 400 and kg <=1000

def sirve_pino(altura_pino:int)->bool:
    return es_peso_util(peso_pino(altura_pino))

print(peso_pino(500))
print(es_peso_util(1000))
print(sirve_pino(300))

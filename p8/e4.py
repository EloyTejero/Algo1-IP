from typing import TextIO
#ARCHIVOS
def contar_lineas(nombre_archivo:str) -> int:
    archivo:TextIO = open(nombre_archivo, 'r')
    lineas:list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)
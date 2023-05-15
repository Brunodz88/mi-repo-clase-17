def validar_opcion(opcion:str):
    if opcion.isdecimal():
        opcion_entero=int(opcion)
        if opcion_entero > 0 and opcion_entero < 5:
            return opcion_entero        
    return False
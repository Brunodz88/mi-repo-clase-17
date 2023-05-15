from .validaciones import validar_opcion

def menu_cuenta_bancaria():
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion=int(input("Ingrese una opción: "))
    validacion=validar_opcion(opcion)
    return validacion

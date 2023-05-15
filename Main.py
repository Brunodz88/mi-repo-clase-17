#esta es una importancion absoluta 

#Alternativa 1

#from banco import cuenta_bancaria

#cuenta_1=cuenta_bancaria.CuentaBancaria(1000)

#Alternativa 2 

#from banco import cuenta_bancaria as bank

#Alternativa 3

from banco.cuenta_bancaria  import CuentaBancaria
from banco.menu import menu_cuenta_bancaria

opcion=menu_cuenta_bancaria()
print (validacion)

cuenta= CuentaBancaria(0)

if opcion ==1:  
    monto=float(input("Ingrese el monto a depositar: "))
    cuenta.depositar(monto)
elif opcion ==2:
    monto=float(input("Ingrese el monto a retirar: "))
    cuenta.retirar(monto)
elif opcion ==3:
    cuenta.consultar_saldo()
else:
    print("Saliendo del programa")



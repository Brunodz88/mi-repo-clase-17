class CuentaBancaria:
    def __init__(self,saldo_inicial) -> None:
        self.saldo=saldo_inicial
        
    def depositar (self,monto):
        self.saldo +=monto
        print(f"Se depositó $ {monto}. Saldo actual:${self.saldo}")
    
    def retirar (self,monto):
        self.saldo -= monto
        print( f"Se retiró ${monto}. Saldo actual:{self.saldo}")
        pass
    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")
        
Cuenta_1= CuentaBancaria(1000)
Cuenta_1.depositar(2000)
Cuenta_1.retirar(500)
Cuenta_1.consultar_saldo()

cuenta_2= CuentaBancaria(0)
cuenta_2.consultar_saldo
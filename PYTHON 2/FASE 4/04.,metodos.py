class CuentaBancaria:
    def __init__(self,titular: str, saldo_inicial: float ):
        self.titular : str = titular
        self.saldo: str = saldo_inicial
    def depositar (self,cantidad: float) -> None:
        self.saldo += cantidad
        print(f"Deposito exitoso. Nuevo saldo  de {self.titular}: ${self.saldo}")
    def retirar (self,cantidad: float) ->None:
        if cantidad > self.saldo:
            print(f"ERROR:{self.titular} no tiene fondos suficientes.")
        else:
            self.saldo -= cantidad
            print (f"retiro  exitoso. Saldo restante: $ {self.saldo}")

Cuenta_ana = CuentaBancaria ("Ana Lopez",50000.0)


Cuenta_ana.depositar(20000.0)
Cuenta_ana.retirar(100000.0)
Cuenta_ana.retirar(15000.0)



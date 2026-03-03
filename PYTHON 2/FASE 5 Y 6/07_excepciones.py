class CajeroAutomatico :
    def __init__(self):
        self.efectivo_disponible :float = 10000.0
    def solicitar_retiro(self) -> None:
        print("--- Bienvenido al cajero ---")

        try:
            monto_str: str = input("Ingrese la cantidad a retirar (solo numero)")
            monto = float(monto_str) 
            if monto == 0:
                raise ValueError("no pede retirar cero pesos. etc")
            self.efectivo_disponible -= monto
            print(f"retiro exitoso. quedan $ {self.efectivo_disponible} en el  cajero")
        except ValueError as e:
            print(f"Error del formato: usted ingreso caracteres invalidos.({e})")

        except Exception as e :
                print(f"error  critico desconocido:contacte soporte.detalle {e}")
        finally:
                print("expulsando tarjeta... gracias  por utilizar  nuestra red \n" )

mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()

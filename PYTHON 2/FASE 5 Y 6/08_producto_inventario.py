
class Producto:
    
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")
            
            self.stock = self.stock - cantidad 

            print(f"Venta exitosa de {cantidad} unidades de {self.nombre}.")
            print(f"Stock restante: {self.stock}")
        
        except ValueError as e:
            print(f"Error: {e}")


class ProductoPerecedero(Producto):

    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int) -> None:
        
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.dias_vencimiento = dias_vencimiento



producto1 = Producto("chocolate", 3500.0, 48)
producto2 = ProductoPerecedero("Leche", 3.5, 10, 7)


producto1.vender(2)


producto1.vender(10)


producto2.vender(5)
producto2.vender(20)


        
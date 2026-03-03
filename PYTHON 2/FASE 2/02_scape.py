impuestos_nacional: float = 0.19
def  calcular_descuento (precio: float) -> float :
    descuento_local: float = precio * 0.10
    precio_con_impuestos : float  = precio +( precio * 0.10) 
    precio_con_impuestos: float = precio +(precio* impuestos_nacional)
    return precio_con_impuestos - descuento_local
resultado:float = calcular_descuento(1000.0)
print(f"precio final:{resultado}")
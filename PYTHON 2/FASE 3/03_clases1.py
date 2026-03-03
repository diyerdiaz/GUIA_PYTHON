class Vehiculo:
    def __init__(self,marca:str,modelo:str, anio:int):
        self.marca : str  = marca 
        self.modelo : str  = modelo
        self.anio : int  = anio 

Vehiculo_1 = Vehiculo ("toyota","corolla",2022)
Vehiculo_2 = Vehiculo("bulgatti","chiron",2022)

print(f"Expecificaciones del carro 1  en venta. MARCA: {Vehiculo_1.marca}, MODELO: {Vehiculo_1.modelo} AÑO: {Vehiculo_1.anio}")
print(f"Expecificaciones del carro 2  en venta. MARCA: {Vehiculo_2.marca}, MODELO: {Vehiculo_2.modelo} AÑO: {Vehiculo_2.anio}")
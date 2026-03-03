class carro:
    def __init__(self, modelo: str, bateria: int = 100) -> None:
        self.modelo: str = modelo
        self.bateria: int = bateria
    
    def conducir(self):
        if self.bateria >= 15:
            self.bateria -= 15 
            print(f"vas conduciendo {self.modelo}")
            
            # LLAMADA CORRECTA: Guardamos el resultado de la función en 'km'
            km = self.tiempo_restante() 
            # IMPRIMIMOS LA VARIABLE 'km'
            print(f"kilometros que puedes recorrer: {km} km")
        else:
            print("bateria insuficiente")

    def cargar(self):
        if self.bateria <= 75:
            self.bateria += 25 
            print(f"cargando bateria....")
        else:
            print("debe tener minimo 75 % pa ponerlo cargar")

    def ver_estado(self):
        print(f"EL estado de la bateria es .... {self.bateria}")
    
    # CORRECCIÓN: Quitamos el parámetro 'km' porque no lo necesitas pedir
    def tiempo_restante(self):
        resultado = self.bateria * 5
        return resultado

vehiculo = carro("TT-034")
vehiculo.conducir()
vehiculo.cargar()
vehiculo.ver_estado()
vehiculo.conducir()

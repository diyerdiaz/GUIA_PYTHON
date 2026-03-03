class MascotaVirtual:

    def __init__(self, nombre: str , energia: int = 10):
        self.nombre : str = nombre
        self.energia : int = energia
    def jugar (self) -> None:
        
        if self.energia>=3:
             self.energia -=  3
             print(f"la mascota esta  jugando ,NOMBRE {self.nombre} ESTADO ACTUAL: {self.energia}")
        else : 
            
            
            print(f"LA MASCOTA ESTA DESCARGADO , NOMBRE: {self.nombre}, ENERGIA: {self.energia}")

            
    def dormir (self,) -> None:
            self.energia +=  5

            print(f"LA MASCOTA ESTA dormido, NOMBRE: {self.nombre}, ENERGIA: {self.energia}")

mascota = MascotaVirtual ("ROBY")

mascota.jugar()
mascota.jugar()
mascota.jugar()
mascota.jugar()
mascota.dormir()



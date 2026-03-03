class SistemaSeguridad :
    def __init__(self,pin_acceso: int):

        self.usuario : str = "Admin"
        self.__pin_secreto: int = pin_acceso
        self.__alarma_activada : bool = True
    def desactivar_alarma_activada (self,intento_pin:int) -> None:
        if intento_pin == self.__pin_secreto:
            self.__alarma_activada = False
            print("Alarma desactivada.")
        
        else:
            print("INTRUSO DETECTADO.LLAMANDO A LA POLICIA.")

casa_central = SistemaSeguridad (1234)
casa_central.desactivar_alarma_activada(9999)
casa_central.desactivar_alarma_activada(1234)



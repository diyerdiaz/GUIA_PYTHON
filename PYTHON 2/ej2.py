class coche_inteligente :
    def __init__(self,modelo: str ,velocidad:int, bateria:int)-> None:
        self.modelo = modelo 
        self.__bat = 100
        self.__vel = 0
    
    def acelerar(self, incremento: int):
    # 1. ¿Hay batería?
        if self.__bat > 0:
        # 2. Intentamos subir la velocidad
            self.__vel += incremento
        
        # 3. APLICAMOS LA REGLA (Encapsulamiento en acción)
        if self.__vel > 200:
            self.__vel = 200  # No dejamos que pase de 200
            print("⚠️ Límite de velocidad alcanzado.")
        
        # 4. Gastamos batería
            self.__bat -= 5
            if self.__bat < 0:
                self.__bat = 0
        else:
            print("🪫 Sin batería. No puedes acelerar.")
        def mostrar_tablero(self) : 
            print (f"tablero actual: BATERIA:{self.__bat} , VELOCIDAD: {self.__vel}")   

nom = coche_inteligente("TT-3")
nom.acelerar(300)
class Empleado :
    def __init__(self,nombre:str, salario:float):
        self.nombre:str = nombre
        self.salario:float = salario
    def trabajar(self)-> None:
        print(f"{self.nombre} esta cumpliendo  su horario regular.")
    
class Desarrollador(Empleado):
    def programar (self) -> None:
        print(f"{self.nombre} esta escribiendo codigo python.")
        
class Gerente (Empleado):
    def  trabajar(self) -> None:
        print(f"{self.nombre} esta en una reunion  estrategica.")
dev = Desarrollador ("Carlos",3500.0)
jefe = Gerente ("Ana",6000.0)

dev.trabajar()
dev.programar()

jefe.trabajar()

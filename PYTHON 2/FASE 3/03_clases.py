class Servidor:
    def __init__(self,nombre:str, ip:str, ram_gb: int):
        self.nombre: str = nombre
        self.ip: str = ip
        self.ram: int = ram_gb
        self.estado: str = "apagado"
server_ventas = Servidor("Ventas-01","192.168.1.10",16)
server_bd = Servidor("Database-main","10.0.0.5",64)
print(f"El servidor{server_ventas.nombre} tiene {server_ventas.ram}GB de RAM.")
print(f"El servidor{server_bd.nombre} actualmente esta: {server_bd.estado}")
def crear_perfil(nombre: str, rol: str) -> None:
    """REGISTRA UN NUEVO PERFIL EN EL SISTEMA """

    print(f"registrando en base de datos: {nombre} | permisos: {rol}")

crear_perfil("carlos","admin")
crear_perfil("ana","ventas")
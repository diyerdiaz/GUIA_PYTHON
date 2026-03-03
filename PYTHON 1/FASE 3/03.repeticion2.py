print("--- filtro de seguridad ---")

edades_acceso = [15 ,22 ,17,30,14]
for  edad in edades_acceso:
    if edad >=18:
        print(f"persona  de {edad} años: acceso PERMITIDO.")

    else:
        print(f"persona de {edad} años: Bloqueada")
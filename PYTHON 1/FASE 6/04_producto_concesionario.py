concesionario = []

for i in range(3):
    print(f"Registro de vehículo #{i + 1}")
    

    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    precio = input("Ingrese el precio del vehículo: ")
    

    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }
    
    concesionario.append(vehiculo)



print("----- REPORTE DE VEHÍCULOS REGISTRADOS -----")


for auto in concesionario:
    print(f"Vehículo registrado: Marca {auto['marca']}, "
          f"Modelo {auto['modelo']}, "
          f"Precio ${auto['precio']}")
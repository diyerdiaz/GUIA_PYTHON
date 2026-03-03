tiene_licencia = input("¿tienes licencia de conducir? (si/no): ")
esta_sobrio= input("¿haz bebido alcohol hoy? (si/no): ")

if tiene_licencia == "si" and esta_sobrio == "no":
    print("puedes conducir el vehiculo")
else:
    print("entregue las  llaves.NO puede conducir.")
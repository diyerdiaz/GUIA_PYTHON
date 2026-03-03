total_ahorrado = 0

for mes in range  (1,4 ):
    consignacion = int  (input(f"¿cuantos  dinero vas a ahorrar  en el mes {mes}?: "))
    total_ahorrado = total_ahorrado + consignacion
    print (f"¡ahorro  completado ! tiene  un total  de $ {total_ahorrado}")
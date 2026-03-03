print("---DIAGNOTICO DE RED ---")

hay_internet = input("'¿el modem tiene luces encendidas? (si/no): ") 

if hay_internet == "si":
    print("paso 1 El equipo  recibe energia.")
    lus_roja = input("Algunas de las luces es color ROJO(si/no): ")
    if lus_roja == "si":
        print ("fallo detectado: problema en la fibra optica . llame a soporte.")
    else :
        print ("Todo normal : su conexion  esta operando  al 100%.")
else:
    print("fallo critico: verifique que el  equipo este conectado  a  la corriente.")

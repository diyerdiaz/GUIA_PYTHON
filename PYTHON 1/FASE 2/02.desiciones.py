edad_usuario = int(input(" por favor, ingresa tu edad en numerós: ")) 
print("evaluando permisos   de acceso...")
if  edad_usuario>= 18:
    print("Acceso concedido : Eres mayor  de edad.")
elif edad_usuario>=13:
    print("acceso restringido : eres adoloecente ,necesitas permiso de un tutor ")
else:
    print("Acceso  denegados : Eres menor de edad.")
print("gracias por utilizar el sitema")
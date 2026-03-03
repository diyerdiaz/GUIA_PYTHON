estudiantes = [
    {"nombre": "Ana","nota": 90},
    {"nombre": "luis","nota": 50}
     
]
for persona in estudiantes:
     if persona["nota"] >=60:
        print (f"{persona['nombre']} ha APROBADO")

def convertir_moneda(cantidad:float , moneda : str = "COP") -> None :
    print(f"procesando transaccion: {cantidad} en moneda {moneda}")
convertir_moneda(5000.0, "USD")
convertir_moneda(150000.0)
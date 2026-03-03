
def calcular_salario_neto(salario_base: float, bonificacion : float = 0.0) -> float :
    descuento : float =  salario_base * 0.08
    descuento_final : float = bonificacion +(salario_base - descuento)
    return descuento_final
salario_1:  float = calcular_salario_neto(1000000,300000)
salario_2:  float = calcular_salario_neto(1000000)

print(f"El salario 1 final: {salario_1}")
print(f"El salario 2 final: {salario_2}")
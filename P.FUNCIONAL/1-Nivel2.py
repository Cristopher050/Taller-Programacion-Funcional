def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)

    return operar


# Prueba
multiplicar = crear_operador(
    5,
    lambda valor, factor: valor * factor
)

print(multiplicar(4))
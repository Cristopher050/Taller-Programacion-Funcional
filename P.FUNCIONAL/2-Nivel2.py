def crear_acumulador_validado(criterio_lambda):
    total = 0

    def acumular(valor):
        nonlocal total

        if criterio_lambda(valor):
            total += valor

        return total

    return acumular


# Prueba
acumulador = crear_acumulador_validado(
    lambda valor: valor > 10
)

print(acumulador(5))
print(acumulador(15))
print(acumulador(20))
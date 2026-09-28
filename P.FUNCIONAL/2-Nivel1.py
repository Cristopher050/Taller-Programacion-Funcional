def crear_contador_paso(fn_paso):
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)

        return cuenta

    return incrementar


# Prueba
contador = crear_contador_paso(
    lambda actual: actual + 3
)

print(contador())
print(contador())
print(contador())
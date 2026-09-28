def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0

    def ejecutar():
        nonlocal intentos
        intentos += 1

        if intentos > max_intentos:
            fn_alerta(intentos)
            return False

        return True

    return ejecutar


# Prueba
alerta = lambda intento: print(
    f"ALERTA: límite superado en intento {intento}"
)

limitador = crear_limitador_avanzado(3, alerta)

print("Intento 1:", limitador())
print("Intento 2:", limitador())
print("Intento 3:", limitador())
print("Intento 4:", limitador())
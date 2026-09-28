def crear_conmutador(lista_estados):
    indice = 0

    def cambiar():
        nonlocal indice

        estado = lista_estados[indice]

        indice = (indice + 1) % len(lista_estados)

        return estado

    return cambiar


# Prueba
conmutador = crear_conmutador(
    ["ROJO", "VERDE", "AZUL"]
)

print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())
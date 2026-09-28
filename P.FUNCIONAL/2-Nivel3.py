def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []

    def agregar(valor):
        nonlocal datos

        if not filtro_ruido_lambda(valor):
            datos.append(valor)

        if not datos:
            return 0

        return sum(datos) / len(datos)

    return agregar


# Prueba
promediador = crear_promediador_filtrado(
    lambda valor: valor > 100 or valor < 0
)

print(promediador(10))
print(promediador(20))
print(promediador(150))
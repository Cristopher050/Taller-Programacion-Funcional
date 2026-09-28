def crear_descuento_dinamico(regla_condicional_lambda):
    descuento = 0.10

    def calcular(precio):
        if regla_condicional_lambda(precio):
            return precio * (1 - descuento)

        return precio

    return calcular


# Prueba
descuento = crear_descuento_dinamico(
    lambda precio: precio >= 100
)

print("Precio $150:", descuento(150))
print("Precio $80:", descuento(80))
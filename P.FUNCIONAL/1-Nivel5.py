def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        convertido = monto * tasa
        margen = margen_lambda(convertido)

        return convertido + margen

    return convertir


# Prueba
conversor = crear_conversor(
    1.10,
    lambda valor: valor * 0.02
)

print("Resultado:", round(conversor(100), 2))
def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        return prefijo + fn_transformacion(texto)

    return formatear


# Prueba
formateador = crear_formateador(
    "Usuario: ",
    lambda texto: texto.upper()
)

print(formateador("crist"))
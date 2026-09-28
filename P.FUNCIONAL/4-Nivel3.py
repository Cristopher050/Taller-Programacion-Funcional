def crear_pipeline(*funciones_transformacion):

    def ejecutar(dato):

        resultado = dato

        for funcion in funciones_transformacion:
            resultado = funcion(resultado)

        return resultado

    return ejecutar


pipeline = crear_pipeline(
    lambda x: x.strip(),
    lambda x: x.lower(),
    lambda x: x.replace(" ", "_"),
    lambda x: "usuario_" + x
)


print(pipeline("  Juan Perez  "))
def crear_consultor(campo):

    def generar_filtro(operador, valor):

        if operador == "==":
            return lambda lista: list(
                filter(
                    lambda obj: obj.get(campo) == valor,
                    lista
                )
            )

        if operador == ">":
            return lambda lista: list(
                filter(
                    lambda obj: obj.get(campo, 0) > valor,
                    lista
                )
            )

        if operador == "<":
            return lambda lista: list(
                filter(
                    lambda obj: obj.get(campo, 0) < valor,
                    lista
                )
            )

        raise ValueError("Operador no soportado")

    return generar_filtro


# Datos
productos = [
    {"nombre": "Laptop", "precio": 900},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Monitor", "precio": 300}
]


# Crear consulta
consultar_precio = crear_consultor("precio")

filtro = consultar_precio(">", 100)

resultado = filtro(productos)

print(resultado)
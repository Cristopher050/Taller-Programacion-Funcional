def procesar_coleccion(
    lista,
    fn_predicado,
    fn_transformacion
):
    return list(
        map(
            fn_transformacion,
            filter(fn_predicado, lista)
        )
    )


# Prueba
numeros = [1, 2, 3, 4, 5, 6]

resultado = procesar_coleccion(
    numeros,
    lambda x: x % 2 == 0,
    lambda x: x * 10
)

print(resultado)